from WineQualityProject.config.configuration import ConfigurationManager
from WineQualityProject.components.data_transformation import DataTransformation
from WineQualityProject import logger
from pathlib import Path


STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()

            else:
<<<<<<< HEAD
                raise Exception("Your data schema is not valid")
=======
                raise Exception("You data schema is not valid")
>>>>>>> 4286e3ba86f1203d9507d357bf8e4e074ec06820

        except Exception as e:
            print(e)