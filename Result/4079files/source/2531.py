# Copyright 2016 Threema GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import base64
import enum
from datetime import datetime, timezone, timedelta
from typing import Callable, Tuple, Optional

from asn1crypto.ocsp import OCSPRequest, OCSPResponse
from oscrypto import asymmetric
from ocspbuilder import OCSPResponseBuilder
from bottle import Bottle, HTTPResponse, request


logger = logging.getLogger(__name__)


# Enums

class ResponseStatus(enum.Enum):
    successful = 'successful'
    malformed_request = 'malformed_request'
    internal_error = 'internal_error'
    try_later = 'try_later'
    sign_required = 'sign_required'
    unauthorized = 'unauthorized'


class CertificateStatus(enum.Enum):
    good = 'good'
    revoked = 'revoked'
    key_compromise = 'key_compromise'
    ca_compromise = 'ca_compromise'
    affiliation_changed = 'affiliation_changed'
    superseded = 'superseded'
    cessation_of_operation = 'cessation_of_operation'
    certificate_hold = 'certificate_hold'
    remove_from_crl = 'remove_from_crl'
    privilege_withdrawn = 'privilege_withdrawn'
    unknown = 'unknown'


# Types

ValidateFunc = Callable[[int], Tuple[CertificateStatus, Optional[datetime]]]
CertRetrieveFunc = Callable[[int], str]


# API endpoints

class OCSPResponder:

    def __init__(self, issuer_cert: str, responder_cert: str, responder_key: str,
                       validate_func: ValidateFunc, cert_retrieve_func: CertRetrieveFunc,
                       next_update_days: int = 7):
        """
        Create a new OCSPResponder instance.

        :param issuer_cert: Path to the issuer certificate.
        :param responder_cert: Path to the certificate of the OCSP responder
            with the `OCSP Signing` extension.
        :param responder_key: Path to the private key belonging to the
            responder cert.
        :param validate_func: A function that - given a certificate serial -
            will return the appropriate :class:`CertificateStatus` and -
            depending on the status - a revocation datetime.
        :param cert_retrieve_func: A function that - given a certificate serial -
            will return the corresponding certificate as a string.
        :param next_update_days: The ``nextUpdate`` value that will be written
            into the response. Default: 7 days.

        """
        # Certs and keys
        self._issuer_cert = asymmetric.load_certificate(issuer_cert)
        self._responder_cert = asymmetric.load_certificate(responder_cert)
        self._responder_key = asymmetric.load_private_key(responder_key)

        # Functions
        self._validate = validate_func
        self._cert_retrieve = cert_retrieve_func

        # Next update
        self._next_update_days = next_update_days

        # Bottle
        self._app = Bottle()

        # Initialize routing
        self._route()

    def _route(self):
        self._app.get('/', callback=self._handle_root)
        self._app.get('/status/<request_data>', callback=self._handle_get)
        self._app.post('/status/', callback=self._handle_post)

    def _handle_root(self):
        return 'ocsp-responder'

    def _handle_get(self, request_data):
        """
        An OCSP GET request contains the DER-in-base64 encoded OCSP request in the
        HTTP request URL.
        """
        der = base64.b64decode(request_data)
        ocsp_request = self._parse_ocsp_request(der)
        return self._build_http_response(ocsp_request)

    def _handle_post(self):
        """
        An OCSP POST request contains the DER encoded OCSP request in the HTTP
        request body.
        """
        der = request.body.read()
        ocsp_request = self._parse_ocsp_request(der)
        return self._build_http_response(ocsp_request)

    def _fail(self, status: ResponseStatus) -> OCSPResponse:
        builder = OCSPResponseBuilder(response_status=status.value)
        return builder.build()

    def _parse_ocsp_request(self, request_der: bytes) -> OCSPRequest:
        """
        Parse the request bytes, return an ``OCSPRequest`` instance.
        """
        return OCSPRequest.load(request_der)

    def _build_ocsp_response(self, ocsp_request: OCSPRequest) -> OCSPResponse:
        """
        Create and return an OCSP response from an OCSP request.
        """
        # Get the certificate serial
        tbs_request = ocsp_request['tbs_request']
        request_list = tbs_request['request_list']
        if len(request_list) != 1:
            logger.warning('Received OCSP request with multiple sub requests')
            raise NotImplemented('Combined requests not yet supported')
        single_request = request_list[0]  # TODO: Support more than one request
        req_cert = single_request['req_cert']
        serial = req_cert['serial_number'].native

        # Check certificate status
        try:
            certificate_status, revocation_date = self._validate(serial)
        except Exception as e:
            logger.exception('Could not determine certificate status: %s', e)
            return self._fail(ResponseStatus.internal_error)

        # Retrieve certificate
        try:
            subject_cert_contents = self._cert_retrieve(serial)
        except Exception as e:
            logger.exception('Could not retrieve certificate with serial %s: %s', serial, e)
            return self._fail(ResponseStatus.internal_error)

        # Parse certificate
        try:
            subject_cert = asymmetric.load_certificate(subject_cert_contents.encode('utf8'))
        except Exception as e:
            logger.exception('Returned certificate with serial %s is invalid: %s', serial, e)
            return self._fail(ResponseStatus.internal_error)

        # Build the response
        builder = OCSPResponseBuilder(**{
            'response_status': ResponseStatus.successful.value,
            'certificate': subject_cert,
            'certificate_status': certificate_status.value,
            'revocation_date': revocation_date,
        })

        # Parse extensions
        for extension in tbs_request['request_extensions']:
            extn_id = extension['extn_id'].native
            critical = extension['critical'].native
            value = extension['extn_value'].parsed

            # This variable tracks whether any unknown extensions were encountered
            unknown = False

            # Handle nonce extension
            if extn_id == 'nonce':
                builder.nonce = value.native

            # That's all we know
            else:
                unknown = True

            # If an unknown critical extension is encountered (which should not
            # usually happen, according to RFC 6960 4.1.2), we should throw our
            # hands up in despair and run.
            if unknown is True and critical is True:
                logger.warning('Could not parse unknown critical extension: %r',
                        dict(extension.native))
                return self._fail(ResponseStatus.internal_error)

            # If it's an unknown non-critical extension, we can safely ignore it.
            elif unknown is True:
                logger.info('Ignored unknown non-critical extension: %r', dict(extension.native))

        # Set certificate issuer
        builder.certificate_issuer = self._issuer_cert

        # Set next update date
        builder.next_update = datetime.now(timezone.utc) + timedelta(days=self._next_update_days)

        return builder.build(self._responder_key, self._responder_cert)

    def _build_http_response(self, request_der: bytes) -> HTTPResponse:
        response_der = self._build_ocsp_response(request_der).dump()
        return HTTPResponse(
            status=200,
            body=response_der,
            content_type='application/ocsp-response',
        )

    def serve(self, port=8080, debug=False):
        logger.info('Launching %sserver on port %d', 'debug' if debug else '', port)
        self._app.run(port=port, debug=debug)
