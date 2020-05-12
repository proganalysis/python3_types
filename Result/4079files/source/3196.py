import os
import datetime
import asyncio
import hashlib
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from slick.logger import logger


class Certificate:
    def __init__(self, app):
        self.app = app
        self.server_key_path = os.path.join(self.app.base, "server.key")
        self.server_cert_path = os.path.join(self.app.base, "server.crt")
        self.public_cert_bytes_result = asyncio.Future()

    @property
    def _name(self):
        return "certificate"

    async def start(self):
        logger.debug("starting certificate")
        if not os.path.isfile(self.server_key_path):
            name = await self.app.identity.name()
            logger.debug(f"no key exists in {self.server_key_path}, generating one")
            key = rsa.generate_private_key(
                public_exponent=65537, key_size=4096, backend=default_backend()
            )

            service_host = await self.app.identity.service_host()

            with open(self.server_key_path, "wb") as f:
                f.write(
                    key.private_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                        encryption_algorithm=serialization.NoEncryption(),
                    )
                )

            subject = issuer = x509.Name(
                [
                    x509.NameAttribute(NameOID.COMMON_NAME, service_host),
                    x509.NameAttribute(NameOID.GIVEN_NAME, name),
                ]
            )

            cert = (
                x509.CertificateBuilder()
                .subject_name(subject)
                .issuer_name(issuer)
                .public_key(key.public_key())
                .serial_number(x509.random_serial_number())
                .not_valid_before(datetime.datetime.utcnow())
                .not_valid_after(
                    datetime.datetime.utcnow() + datetime.timedelta(weeks=520)
                )
                .add_extension(
                    x509.SubjectAlternativeName([x509.DNSName(service_host)]),
                    critical=False,
                )
                .add_extension(
                    x509.BasicConstraints(ca=False, path_length=None), critical=True
                )
                .sign(key, hashes.SHA256(), default_backend())
            )

            public_cert_bytes = cert.public_bytes(serialization.Encoding.PEM)
            with open(self.server_cert_path, "wb") as f:
                f.write(public_cert_bytes)
        else:
            logger.debug(f"a key exists in {self.server_key_path}, reading it")
            with open(self.server_cert_path, "rb") as f:
                public_cert_bytes = f.read()
                logger.debug(f"done reading key from {self.server_key_path}")

        self.public_cert_bytes_result.set_result(public_cert_bytes)
        logger.debug(f"finished certificate")

    async def stop(self):
        pass

    async def public_cert_bytes(self):
        await self.public_cert_bytes_result
        return self.public_cert_bytes_result.result()

    async def digest(self) -> bytes:
        m = hashlib.sha256()
        m.update(await self.public_cert_bytes())
        return m.digest()
