import pandas as pd 
from src.logger.logging import logging
from src.exception.exception import customexception
import os 
import sys 
from dataclasses import dataclass
from pathlib import Path
from src.utils.utils import save_object, evaluate_model
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model", "trained_model.pkl")
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()   
        
    def initiate_model_training(self, train_arr, test_arr):
        try:
            logging.info('Splitting Dependent and independent variable.')
            X_train, y_train, X_test, y_test =  (
                train_arr[:, :-1],
                train_arr[:, -1],
                test_arr[:, :-1],
                test_arr[:, -1]
            )
            
            models={
                "LinearRegression": LinearRegression(),
                "Lasso": Lasso(),
                "Ridge": Ridge(), 
                'Elasticnet':ElasticNet(), 
            }
            
            model_report: dict = evaluate_model(X_train, y_train, X_test, y_test, models)
            print(model_report)
            print('\n*________________________________________________*\n')
            logging.info(f'Model Report :{model_report}')
            
            # Select the best model based on the highest score
            best_model_name = max(model_report, key=model_report.get)  # This is a cleaner way to find the best model
            best_model = models[best_model_name]
            
            print(f'Best Model found, Model Name: {best_model}')
            print('\n======================================================')

            save_object(file_path=self.model_trainer_config.trained_model_file_path,
                        obj=best_model)
                        
        except Exception as e:
            logging.info('Exception occured while Model Training')
            raise customexception(e, sys)