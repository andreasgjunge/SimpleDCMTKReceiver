# File: read_config.py

import configparser


def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def print_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    for section in config.sections():
        print(f"[{section}]")
        for key, value in config[section].items():
            print(f"{key} = {value}")
