import os

import pytest

try:
    import requests
    __has_requests = True
except ImportError:
    __has_requests = False

# Import our modules.

from configmaster.ConfigKey import ConfigKey

from configmaster.JSONConfigFile import JSONConfigFile

from configmaster.INIConfigFile import INIConfigFile
from configmaster import exc

try:
    from configmaster.YAMLConfigFile import YAMLConfigFile
    __has_yaml = True
except exc.FiletypeNotSupportedException:
    __has_yaml = False

from configmaster.JSONConfigFile import NetworkedJSONConfigFile



def test_loading_valid_json():
    cfg = JSONConfigFile("test_data/test.json")
    assert isinstance(cfg.config, ConfigKey)
    assert cfg.config.parsed

@pytest.mark.skipif(not __has_yaml, reason="Requires PyYAML to be installed.")
def test_loading_valid_yml():
    cfg = YAMLConfigFile("test_data/test.yml")
    assert isinstance(cfg.config, ConfigKey)
    assert cfg.config.parsed

def test_loading_valid_ini():
    cfg = INIConfigFile("test_data/test.ini")
    assert 'bitbucket_org' in cfg.config
    assert cfg.config.bitbucket_org.user == "hg"

def test_created_config_file():
    if os.path.exists("test_data/bleh.json"):
        os.remove("test_data/bleh.json")
    try:
        cfg = JSONConfigFile("test_data/bleh.json")
        # next line should happen
        parsed = True
    except:
        parsed = False
    assert parsed
    assert not cfg.config.parsed
    assert os.path.exists("test_data/bleh.json")

def test_initial_populate():
    cfg = JSONConfigFile("test_data/bleh.json")
    pop = cfg.initial_populate({"a": 1})
    assert pop
    cfg.dump() and cfg.reload()
    assert cfg.config.a == 1


def test_dumps():
    cfg = JSONConfigFile("test_data/bleh.json")
    assert cfg.dumps() == "{\"a\": 1}"

def test_dumpd():
    cfg = JSONConfigFile("test_data/test.json")
    assert cfg.dumpd() == {"hello": "goodbye", "qaz": 1, "wsx": 2, "edc": {"op": 4, "po": 6},
                                        "fruit": ["apples", "oranges", "bananas"],
                                        "houses": [{"red": False, "blue": True}, {"red": True, "blue": False}]}

def test_loaded_config_item():
    cfg = JSONConfigFile("test_data/test.json")
    assert cfg.config.hello == "goodbye"

def test_embedded_dict():
    cfg = JSONConfigFile("test_data/test.json")
    assert isinstance(cfg.config.edc, ConfigKey)
    assert cfg.config.edc.op == 4
    assert cfg.config.edc.po == 6


def test_embedded_dict_getitem():
    cfg = JSONConfigFile("test_data/test.json")
    assert isinstance(cfg.config['edc'], ConfigKey)
    assert cfg.config['edc'].op == 4
    assert cfg.config['edc'].po == 6

def test_embedded_list():
    cfg = JSONConfigFile("test_data/test.json")
    assert isinstance(cfg.config.fruit, list)
    assert cfg.config.fruit[0] == "apples"
    assert cfg.config.fruit[1] == "oranges"
    assert cfg.config.fruit[2] == "bananas"

def test_embedded_dict_inside_list():
    cfg = JSONConfigFile("test_data/test.json")
    assert isinstance(cfg.config.houses, list)
    assert isinstance(cfg.config.houses[0], ConfigKey)
    assert cfg.config.houses[0].red is False
    assert cfg.config.houses[0].blue is True
    assert cfg.config.houses[1].red is True
    assert cfg.config.houses[1].blue is False

def test_unsafe_load():
    cfg = JSONConfigFile("test_data/unsafe.json")
    assert tuple(cfg.config.keys()) == ("unsafe___dict__",)

@pytest.mark.xfail(raises=exc.LoaderException)
def test_invalid_yaml_data():
    cfg = YAMLConfigFile("test_data/invalid.data")

@pytest.mark.xfail(raises=exc.LoaderException)
def test_invalid_json_data():
    cfg = JSONConfigFile("test_data/invalid.data")

@pytest.mark.xfail(raises=AttributeError)
def test_invalid_key_get():
    cfg = JSONConfigFile("test_data/test.json")
    assert cfg.config.q == "w"

def test_configkey_dump():
    cfg = JSONConfigFile("test_data/test.json")
    assert cfg.config.dump() == {"hello": "goodbye", "qaz": 1, "wsx": 2, "edc": {"op": 4, "po": 6},
                                        "fruit": ["apples", "oranges", "bananas"],
                                        "houses": [{"red": False, "blue": True}, {"red": True, "blue": False}]}

def test_configkey_iter():
    cfg = JSONConfigFile("test_data/test.json")
    assert set(x for x in cfg.config) == {"hello", "qaz", "wsx", "edc", "fruit", "houses"}


if not __has_requests:
    __site_up = False
else:
    try:
        r = requests.get("http://echo.jsontest.com/k/v")
    except Exception:
        __site_up = False
    else:
        if r.status_code != 200:
            __site_up = False
        else:
            __site_up = True


# Test network JSON stuff.
@pytest.mark.skipif(not __site_up, reason="JSONTest site is not up - cannot perform tests currently.")
@pytest.mark.skipif(not __has_requests, reason="Requests must be installed to use Networked JSON tests.")
def test_network_json_get_url():
    cfg = NetworkedJSONConfigFile("http://echo.jsontest.com/k/v")
    assert cfg.config.k == "v"

@pytest.mark.skipif(not __site_up, reason="JSONTest site is not up - cannot perform tests currently.")
@pytest.mark.skipif(not __has_requests, reason="Requests must be installed to use Networked JSON tests.")
@pytest.mark.xfail
def test_network_json_get_bad_url():
    cfg = NetworkedJSONConfigFile("http://abc.def")

@pytest.mark.skipif(not __site_up, reason="JSONTest site is not up - cannot perform tests currently.")
@pytest.mark.skipif(not __has_requests, reason="Requests must be installed to use Networked JSON tests.")
def test_network_json_get_unsafe_data():
    cfg = NetworkedJSONConfigFile("http://echo.jsontest.com/__dict__/v/dump/lol")
    assert hasattr(cfg.config, "unsafe___dict__")
    assert cfg.config.unsafe___dict__ == "v"
    assert hasattr(cfg.config, "unsafe_dump")
    assert cfg.config.unsafe_dump == "lol"


@pytest.mark.skipif(not __site_up, reason="JSONTest site is not up - cannot perform tests currently.")
@pytest.mark.skipif(not __has_requests, reason="Requests must be installed to use Networked JSON tests.")
@pytest.mark.xfail(raises=exc.NetworkedFileException)
def test_network_json_dump():
    cfg = NetworkedJSONConfigFile("http://echo.jsontest.com/k/v")
    cfg.dump()

@pytest.mark.skipif(not __site_up, reason="JSONTest site is not up - cannot perform tests currently.")
@pytest.mark.skipif(not __has_requests, reason="Requests must be installed to use Networked JSON tests.")
@pytest.mark.xfail(raises=exc.NetworkedFileException)
def test_network_json_populate():
    cfg = NetworkedJSONConfigFile("http://echo.jsontest.com/k/v")
    cfg.initial_populate({})

@pytest.mark.skipif(not __site_up, reason="JSONTest site is not up - cannot perform tests currently.")
@pytest.mark.skipif(not __has_requests, reason="Requests must be installed to use Networked JSON tests.")
@pytest.mark.xfail(raises=exc.LoaderException)
def test_network_json_bad_data():
    cfg = NetworkedJSONConfigFile("http://google.com/robots.txt")


