# (generated with --quick)

from typing import Dict, Type, Union

basedir: str
configs: Dict[str, Type[Union[DevConfig, ProdConfig, TestConfig]]]
os: module

class BaseConfig:
    AUTH_HEADER_NAME: str
    MARSHMALLOW_DATEFORMAT: str
    MARSHMALLOW_STRICT: bool
    MAX_AGE: int
    OAUTH2_PROVIDER_TOKEN_EXPIRES_IN: int
    SECRET_KEY: str
    SECURITY_CONFIRMABLE: bool
    SECURITY_CONFIRM_URL: str
    SECURITY_LOGIN_SALT: str
    SECURITY_LOGIN_URL: str
    SECURITY_LOGOUT_URL: str
    SECURITY_PASSWORD_HASH: str
    SECURITY_PASSWORD_SALT: str
    SECURITY_POST_LOGIN_VIEW: str
    SECURITY_RECOVERABLE: bool
    SECURITY_REGISTERABLE: bool
    SECURITY_REGISTER_URL: str
    SECURITY_RESET_URL: str
    SECURITY_TRACKABLE: bool
    SQLALCHEMY_COMMIT_ON_TEARDOWN: bool
    SQLALCHEMY_RECORD_QUERIES: bool
    SQLALCHEMY_TRACK_MODIFICATIONS: bool
    WTF_CSRF_ENABLED: bool
    @staticmethod
    def init_app(app) -> None: ...

class DevConfig(BaseConfig):
    DEBUG: bool
    SQLALCHEMY_DATABASE_URI: str
    TESTING: bool

class ProdConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI: str

class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI: str
    TESTING: bool
