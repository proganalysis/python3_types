import redis
import psycopg2
import raven
import riemann_client.client
import riemann_client.transport

from microservice import config


def get_psql(dbname=None):
    cfg = config.get_config()['psql'].copy()
    if dbname:
        cfg['database'] = dbname
    return psycopg2.connect(**cfg)


def get_redis():
    cfg = config.get_config()['redis'].copy()
    return redis.Redis(decode_responses=True, **cfg)


def get_riemann():
    cfg = config.get_config()['riemann'].copy()
    return riemann_client.client.Client(transport=riemann_client.transport.UDPTransport(cfg['host'], cfg['port']))


def get_raven():
    cfg = config.get_config()['sentry'].copy()
    return raven.Client(cfg['dsn'])
