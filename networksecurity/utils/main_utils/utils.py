import yaml
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

import os,sys
import numpy as np
#import dill
import pickle

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return ymal.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e,sys) from e