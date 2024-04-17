import sys
from src.components.dataIngestion import DataIngestion
from src.components.dataTransformation import DataTransformation
from src.components.modelTraining import ModelTrainer
from src.logger.logging import logging
from src.exception.exception import customexception
import pandas as pd

dataIngestion = DataIngestion()
train_data_path, test_data_path = dataIngestion.initiate_data_ingestion()

dataTransformation = DataTransformation()
train_arr, test_arr = dataTransformation.initialize_data_transformation(train_data_path,test_data_path)

modelTraining = ModelTrainer()
modelTraining.initiate_model_training(train_arr, test_arr)

