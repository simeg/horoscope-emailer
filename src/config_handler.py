#!/usr/bin/env python

import os
import yaml

is_production = bool(os.environ.get('IS_PRODUCTION', failobj=False))


def get(key):
    return os.environ.get(key) if is_production \
        else _private_config().get(key)


def default_config():
    return _get_file('src/config.yaml')


def _private_config():
    return _get_file('src/private_config.yaml')


def _get_file(path):
    with open(path, 'r') as _file:
        return yaml.load(_file)
