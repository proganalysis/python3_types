"""
utilities to help with creating chubby config file(.chubby) and writing and
reading it.
"""

import configparser
import os
import logging

logger = logging.getLogger(__name__)

def create_if_not_exists():
    """
    Create the config file if doesn't exist already.
    """

    # check if it exists
    if not os.path.exists(get_config_path()):
        logger.debug('.chubby file does not exist')
        logger.debug('Creating .chubby file at ' + os.path.expanduser('~') + '...')
        os.chdir(os.path.expanduser("~"))
        # create file
        with open(".chubby", 'a'):
            pass

def get_config_path():
    return os.path.join(os.path.expanduser("~"), ".chubby")

def read_config(config=configparser.ConfigParser(), path=get_config_path()):
    """
    :param path:
        Absolute path of the config file to be read.
    :returns:
        returns the config object.
    """
    logger.debug('Reading config: ' + path)

    create_if_not_exists()

    config.read(path)
    return config

def write_config(section_name: str,
                 section_content: dict,
                 path=get_config_path()):
    """
    :param section_name:
        The name of the section to be written to the config file
    :param section_content:
        The keys and values to be written in the section passed as a dict.
    """
    logger.debug('Writing config at ' + path + '...')

    config = read_config(path=path)
    # if present, modify
    if section_name in config:
        logger.debug('Overwriting/Appending to existing section ' + section_name + '...')
        for keys in section_content:
            # if already present, overwrite. If not create
            config[section_name][keys] = str(section_content[keys])
    # else create a new section
    else:
        logger.debug('Creating new section ' + section_name + '...')
        config[section_name] = section_content

    with open(path, 'w') as f:
        config.write(f)

    logger.info('Written to config successfully.')
