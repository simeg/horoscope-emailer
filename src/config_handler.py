#!/usr/bin/env python

import os
import yaml

isProduction = bool(os.environ.get('IS_PRODUCTION', False))


def get(config_var):
    return os.environ.get(config_var) if isProduction \
        else _get_private_config().get(config_var)


def get_default_config():
    return _get_config('src/config.yaml')


def _get_private_config():
    return _get_config('src/private_config.yaml')


def _get_config(file_path):
    with open(file_path, 'r') as cfg_file:
        return yaml.load(cfg_file)
