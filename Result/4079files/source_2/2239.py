import subprocess

import pytest

from ocspresponder import OCSPResponder, CertificateStatus


openssl_cnf = """
[ req ]
distinguished_name  = req_distinguished_name
string_mask         = utf8only
default_md          = sha1

[ req_distinguished_name ]
countryName                     = Country Name (2 letter code)
stateOrProvinceName             = State or Province Name
localityName                    = Locality Name
0.organizationName              = Organization Name
organizationalUnitName          = Organizational Unit Name
commonName                      = Common Name
emailAddress                    = Email Address

[ v3_root_ca ]
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid:always,issuer
basicConstraints = critical, CA:true
keyUsage = critical, digitalSignature, cRLSign, keyCertSign

[ ocsp ]
basicConstraints = critical, CA:FALSE
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid,issuer
keyUsage = critical, digitalSignature
extendedKeyUsage = critical, OCSPSigning

[ tls_cert ]
basicConstraints = critical, CA:FALSE
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid
keyUsage = critical, digitalSignature, keyEncipherment
extendedKeyUsage = serverAuth, clientAuth
"""


@pytest.fixture
def test_ca(tmpdir):
    """
    Initialize a test CA in a temporary directory.
    """
    # Temp directories
    cadir = tmpdir.mkdir('ca')
    dir_private = cadir.mkdir('private')
    dir_certs = cadir.mkdir('certs')
    dir_csr = cadir.mkdir('csr')

    # Write config
    configfile = cadir.join('openssl.cnf')
    configfile.write(openssl_cnf)

    # Create private keys
    def create_pkey(name):
        subprocess.check_call([
            'openssl', 'genpkey',
            '-algorithm', 'RSA',
            '-pkeyopt', 'rsa_keygen_bits:512',
            '-outform', 'PEM',
            '-out', str(dir_private.join(name)),
        ])
    create_pkey('ca.key.pem')
    create_pkey('ocsp.key.pem')

    # Create self signed root certificate
    subprocess.check_call([
        'openssl', 'req',
        '-config', str(configfile),
        '-key', str(dir_private.join('ca.key.pem')),
        '-new', '-x509', '-sha1',
        '-extensions', 'v3_root_ca',
        '-days', '14',
        '-subj', '/C=CH/CN=Test CA Root',
        '-out', str(dir_certs.join('ca.cert.pem')),
    ])

    # Create OCSP cert
    subprocess.check_call([
        'openssl', 'req',
        '-config', str(configfile),
        '-key', str(dir_private.join('ca.key.pem')),
        '-new', '-sha1',
        '-subj', '/C=CH/CN=Test CA OCSP',
        '-out', str(dir_csr.join('ocsp.csr.pem')),
    ])
    subprocess.check_call([
        'openssl', 'x509',
        '-req', '-sha1',
        '-extfile', str(configfile),
        '-extensions', 'ocsp',
        '-CA', str(dir_certs.join('ca.cert.pem')),
        '-CAkey', str(dir_private.join('ca.key.pem')),
        '-set_serial', '0x1234',
        '-days', '14',
        '-in', str(dir_csr.join('ocsp.csr.pem')),
        '-out', str(dir_certs.join('ocsp.cert.pem')),
    ])

    # Create subject cert
    subprocess.check_call([
        'openssl', 'req',
        '-newkey', 'rsa:512',
        '-nodes', '-sha1',
        '-subj', '/CN=example.com',
        '-out', str(dir_csr.join('example.com.csr.pem')),
        '-keyout', str(dir_private.join('example.com.key.pem')),
    ])
    subprocess.check_call([
        'openssl', 'x509',
        '-req', '-sha1',
        '-extfile', str(configfile),
        '-extensions', 'tls_cert',
        '-CA', str(dir_certs.join('ca.cert.pem')),
        '-CAkey', str(dir_private.join('ca.key.pem')),
        '-set_serial', '0x2000',
        '-days', '14',
        '-in', str(dir_csr.join('example.com.csr.pem')),
        '-out', str(dir_certs.join('example.com.cert.pem')),
    ])

    return cadir


@pytest.fixture
def responder(test_ca):
    """
    Return an OCSPResponder instance.
    """
    # No-op validation function
    def validate(serial):
        return (CertificateStatus.good, None)

    # Certificate retrieval function
    def get_cert(serial):
        subject_cert = str(test_ca.join('certs').join('example.com.cert.pem'))
        with open(subject_cert, 'r') as f:
            return f.read()

    # Instantiate responder
    issuer_cert = str(test_ca.join('certs').join('ca.cert.pem'))
    responder_cert = str(test_ca.join('certs').join('ocsp.cert.pem'))
    responder_key = str(test_ca.join('private').join('ocsp.key.pem'))
    return OCSPResponder(issuer_cert, responder_cert, responder_key, validate, get_cert)


@pytest.fixture
def ocsp_request_builder(test_ca, tmpdir):
    ocspdir = tmpdir.mkdir('ocsp')

    def _builder(nonce=False):
        args = [
            'openssl', 'ocsp',
            '-noverify',
            '-md5',
            '-reqout', str(ocspdir.join('example.com.req.der')),
            '-issuer', str(test_ca.join('certs').join('ca.cert.pem')),
            '-cert', str(test_ca.join('certs').join('example.com.cert.pem')),
        ]
        if nonce is True:
            args += ['-nonce']
        else:
            args += ['-no_nonce']
        subprocess.check_output(args)
        return ocspdir.join('example.com.req.der').read_binary()

    return _builder
