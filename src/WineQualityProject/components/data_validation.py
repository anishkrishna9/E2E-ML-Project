import os
from WineQualityProject import logger
import pandas as pd
from WineQualityProject.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    
    def validate_all_columns(self)-> bool:
        try:
<<<<<<< HEAD
            validation_status = True

            data = pd.read_csv(self.config.unzip_data_dir)
            if 'Id' in data.columns:
                data = data.drop(columns=['Id'])
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()
=======
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

>>>>>>> 4286e3ba86f1203d9507d357bf8e4e074ec06820
            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
<<<<<<< HEAD
                    break
            
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")
=======
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
>>>>>>> 4286e3ba86f1203d9507d357bf8e4e074ec06820

            return validation_status
        
        except Exception as e:
            raise e