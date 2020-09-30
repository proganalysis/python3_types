from datetime import datetime, timezone, timedelta

import pytest

from ocspresponder import CertificateStatus


def test_validate_noop(responder):
    assert responder._validate('salami') == (CertificateStatus.good, None)


@pytest.mark.parametrize('nonce', [True, False])
def test_parse_ocsp_request(responder, ocsp_request_builder, nonce):
    """
    An OCSP request should be parsed properly.
    """
    request_der = ocsp_request_builder(nonce=nonce)
    request = responder._parse_ocsp_request(request_der)

    # TBSRequest version 1 has no requestor name
    tbs_request = request['tbs_request']
    assert tbs_request['version'].native == 'v1'
    assert tbs_request['requestor_name'].native is None

    # There may be a nonce or not.
    if nonce is True:
        assert len(tbs_request['request_extensions']) == 1
        ext = tbs_request['request_extensions'][0]
        assert ext['extn_id'].native == 'nonce'
        assert ext['critical'].native is False
        assert ext['extn_value'].native
    else:
        assert tbs_request['request_extensions'].native is None

    # There is only one request
    request_list = tbs_request['request_list']
    assert len(request_list) == 1

    # There are no single request extensions
    single_request = request_list[0]
    assert single_request['single_request_extensions'].native is None

    req_cert = single_request['req_cert']

    # OCSP request in test fixture is created using MD5
    assert req_cert['hash_algorithm']['algorithm'].native == 'md5'
    assert req_cert['hash_algorithm']['parameters'].native is None

    # Verify serial of subject cert
    assert req_cert['serial_number'].native == 0x2000


def test_build_ocsp_response(responder, ocsp_request_builder):
    """
    An OCSP response should be built properly.
    """
    request_der = ocsp_request_builder(nonce=False)
    request = responder._parse_ocsp_request(request_der)
    response = responder._build_ocsp_response(request)

    # This should be a successful response
    assert response['response_status'].native == 'successful'

    # Test response type
    response_bytes = response['response_bytes']
    assert response_bytes['response_type'].native == 'basic_ocsp_response'

    # Response is signed by the root certificate (serial 0x1234)
    basic_response = response_bytes['response'].parsed
    assert basic_response['signature_algorithm']['algorithm'].native == 'sha256_rsa'
    assert basic_response['signature_algorithm']['parameters'].native is None
    assert len(basic_response['certs']) == 1
    assert basic_response['certs'][0]['tbs_certificate']['serial_number'].native == 0x1234

    # Test actual response data
    before = datetime.now(timezone.utc) - timedelta(minutes=1)
    after = datetime.now(timezone.utc) + timedelta(minutes=1)
    tbs_response_data = basic_response['tbs_response_data']
    assert tbs_response_data['version'].native == 'v1'
    assert before < tbs_response_data['produced_at'].native < after
    assert tbs_response_data['response_extensions'].native is None

    # Response is for the subject certificate (serial 0x2000)
    assert len(tbs_response_data['responses']) == 1
    single_response = tbs_response_data['responses'][0]
    assert single_response['cert_id']['serial_number'].native == 0x2000

    # Response is "good", no revocation info
    assert single_response['cert_status'].name == 'good'
    assert single_response['cert_status'].native is None

    # This update is at the same time as the response production datetime
    this_update = single_response['this_update'].native
    assert this_update == tbs_response_data['produced_at'].native

    # Next update is in 7 days
    assert single_response['next_update'].native == this_update + timedelta(days=7)

    # Response has an issuer extension
    assert len(single_response['single_extensions']) == 1
    issuer_ext = single_response['single_extensions'][0]
    assert issuer_ext['extn_id'].native == 'certificate_issuer'
    assert issuer_ext['critical'].native is False
    issuers = issuer_ext['extn_value'].parsed
    assert len(issuers) == 1
    assert issuers[0].native['country_name'] == 'CH'
    assert issuers[0].native['common_name'] == 'Test CA Root'


def test_verify_good(responder, ocsp_request_builder):
    """
    Test a successful / good response.
    """
    # Build request
    request_der = ocsp_request_builder(nonce=False)
    responder._validate = lambda serial: (CertificateStatus.good, None)
    request = responder._parse_ocsp_request(request_der)

    # Parse response
    response = responder._build_ocsp_response(request)
    response_bytes = response['response_bytes']
    basic_response = response_bytes['response'].parsed
    tbs_response_data = basic_response['tbs_response_data']
    assert len(tbs_response_data['responses']) == 1
    single_response = tbs_response_data['responses'][0]

    # This should be a successful response
    assert response['response_status'].native == 'successful'

    # Response is "good", no revocation info
    assert single_response['cert_status'].name == 'good'
    assert single_response['cert_status'].native is None


def test_verify_revoked(responder, ocsp_request_builder):
    """
    Test a successful / revoked / unspecified response.
    """
    # Build request
    request_der = ocsp_request_builder(nonce=False)
    now = datetime.now(timezone.utc)
    responder._validate = lambda serial: (CertificateStatus.revoked, now)
    request = responder._parse_ocsp_request(request_der)

    # Parse response
    response = responder._build_ocsp_response(request)
    response_bytes = response['response_bytes']
    basic_response = response_bytes['response'].parsed
    tbs_response_data = basic_response['tbs_response_data']
    assert len(tbs_response_data['responses']) == 1
    single_response = tbs_response_data['responses'][0]

    # This should be a successful response
    assert response['response_status'].native == 'successful'

    # Response is "good", no revocation reason
    assert single_response['cert_status'].name == 'revoked'
    assert dict(single_response['cert_status'].native) == {
        'revocation_reason': 'unspecified',
        'revocation_time': now.replace(microsecond=0),
    }


def test_verify_exception(responder, ocsp_request_builder):
    """
    Test that the proper response_status is set if the validator raises an
    exception.
    """
    # Build request
    request_der = ocsp_request_builder(nonce=False)

    def validate(serial):
        raise ValueError('oh shitshitshit')

    responder._validate = validate
    request = responder._parse_ocsp_request(request_der)
    response = responder._build_ocsp_response(request)

    # This should be an error response
    assert response['response_status'].native == 'internal_error'


def test_nonce(responder, ocsp_request_builder):
    """
    The nonce extension should be supported.
    """
    request_der = ocsp_request_builder(nonce=True)
    request = responder._parse_ocsp_request(request_der)
    response = responder._build_ocsp_response(request)

    # This should be a successful response
    assert response['response_status'].native == 'successful'

    # Test response type
    response_bytes = response['response_bytes']
    assert response_bytes['response_type'].native == 'basic_ocsp_response'

    # There should be 1 extension
    tbs_response_data = response_bytes['response'].parsed['tbs_response_data']
    assert len(tbs_response_data['response_extensions']) == 1

    # Get request nonce
    request_ext = request['tbs_request']['request_extensions'][0]
    assert request_ext['extn_id'].native == 'nonce'
    request_nonce = request_ext['extn_value'].parsed

    # Get response nonce
    response_ext = tbs_response_data['response_extensions'][0]
    assert response_ext['extn_id'].native == 'nonce'
    response_nonce = response_ext['extn_value'].parsed

    # Compare
    assert request_nonce == response_nonce


def test_next_update_override(responder, ocsp_request_builder):
    """
    The "next update" date should be overrideable.
    """
    request_der = ocsp_request_builder(nonce=True)

    responder._next_update_days = 1

    # Get response
    request = responder._parse_ocsp_request(request_der)
    response = responder._build_ocsp_response(request)

    # This should be a successful response
    assert response['response_status'].native == 'successful'

    # Test actual response data
    tbs_response_data = response['response_bytes']['response'].parsed['tbs_response_data']
    before = datetime.now(timezone.utc) - timedelta(minutes=1)
    after = datetime.now(timezone.utc) + timedelta(minutes=1)
    assert before < tbs_response_data['produced_at'].native < after

    # Get single response
    single_response = tbs_response_data['responses'][0]

    # This update is at the same time as the response production datetime
    this_update = single_response['this_update'].native
    assert this_update == tbs_response_data['produced_at'].native

    # Next update is in 1 day
    assert single_response['next_update'].native == this_update + timedelta(days=1)


def test_get_cert_exception(responder, ocsp_request_builder):
    """
    Test that the proper response_status is set if the get_cert function raises
    an exception.
    """
    # Build request
    request_der = ocsp_request_builder(nonce=False)

    def get_cert(serial):
        raise ValueError('oh shitshitshit')

    responder._cert_retrieve = get_cert
    request = responder._parse_ocsp_request(request_der)
    response = responder._build_ocsp_response(request)

    # This should be an error response
    assert response['response_status'].native == 'internal_error'


def test_get_cert_invalid(responder, ocsp_request_builder):
    """
    Test that the proper response_status is set if the get_cert function
    returns an invalid certificate.
    """
    # Build request
    request_der = ocsp_request_builder(nonce=False)

    def get_cert(serial):
        return None

    responder._cert_retrieve = get_cert
    request = responder._parse_ocsp_request(request_der)
    response = responder._build_ocsp_response(request)

    # This should be an error response
    assert response['response_status'].native == 'internal_error'
