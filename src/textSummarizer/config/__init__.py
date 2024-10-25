from src.textSummarizer.utils.common import read_yaml,create_directories
from src.textSummarizer.constant import *

from src.textSummarizer.entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        # Convert file paths to Path objects
        config_filepath = Path(config_filepath)
        # params_filepath = Path(params_filepath)

        # Reading YAML files and storing their contents
        self.config = read_yaml(config_filepath)
        # self.params = read_yaml(params_filepath)

        # Ensure the artifacts root directory exists
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        # Fetch the data_ingestion part from config
        config = self.config.data_ingestion

        # Ensure the root directory exists
        create_directories([config.root_dir])

        # Create DataIngestionConfig object with parameters from config
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
