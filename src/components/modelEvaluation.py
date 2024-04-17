import pandas as pd 
import numpy as np 

from src.logger.logging import logging
from src.exception.exception import customexception

import os 
import sys 
from sklearn.metrics import mean_absolute_error, median_absolute_error, mean_squared_error
import mlflow
import mlflow.sklearn
import numpy as np 
import pickle
from src.utils.utils import load_object
from dataclasses import dataclass
from pathlib import Path

@dataclass
class ModelEvaluationConfig:
    pass

class ModelEvaluation:
    def __init__(self):
        pass
    
    def initiate_model_evaluation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e, sys)