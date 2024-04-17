import pandas as pd 
import numpy as np 

from src.logger.logging import logging
from src.exception.exception import customexception

import os 
import sys 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts', 'preprocessor.pkl')
class DataTransformation:
    def __init__(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e, sys)