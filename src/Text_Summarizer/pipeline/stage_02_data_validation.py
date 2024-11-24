from src.Text_Summarizer.config.configuration import ConfigurationManager
from src.Text_Summarizer.components.data_validation import DataValidation

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validation_all_files_exist()
