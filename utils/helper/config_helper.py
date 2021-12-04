import os
import configparser
from pathlib import PurePath, Path

from definition import ROOT_DIR

config_filepath = Path(ROOT_DIR / 'config.ini')

class ConfigMissingError(Exception):
    """missing config file"""
    pass

def get_config(filepath: PurePath = config_filepath) -> configparser.ConfigParser:

    if not os.path.isfile(filepath):
        raise ConfigMissingError(f"cannot find config file at {filepath}")

    config = configparser.ConfigParser()
    config.read(filepath)

    return config
