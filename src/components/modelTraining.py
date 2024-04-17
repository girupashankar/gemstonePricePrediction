import pandas as pd 
import numpy as np 

from src.logger.logging import logging
from src.exception.exception import customexception

import os 
import sys 
from dataclasses import dataclass
from pathlib import Path
from src.utils.utils import save_object, evaluate_model
@dataclass
class DataIngestionConfig:
    pass
class DataIngestion:
    def __init__(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e, sys)