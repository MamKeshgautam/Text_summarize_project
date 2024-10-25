import os
from box.exceptions import BoxValueError
import yaml
from src.textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any




@ensure_annotations
def read_yaml(path_to_yaml: Path):
    try:
        with path_to_yaml.open('r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            if not content:
                raise ValueError(f"The YAML file at {path_to_yaml} is empty or improperly formatted.")

            # Extract relevant parts for the Config class
            artifacts_root = content.get('artifacts_root')
            data_ingestion_content = content.get('data_ingestion')

            # Create DataIngestionConfig object
            data_ingestion_config = DataIngestionConfig(
                root_dir=data_ingestion_content.get('root_dir'),
                source_URL=data_ingestion_content.get('source_URL'),
                local_data_file=data_ingestion_content.get('local_data_file'),
                unzip_dir=data_ingestion_content.get('unzip_dir'),
            )

            return Config(artifacts_root=artifacts_root, data_ingestion=data_ingestion_config)

    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {path_to_yaml} was not found.")
    except yaml.YAMLError as exc:
        raise ValueError(f"Error while parsing YAML file: {exc}")

# def read_yaml(path_to_yaml: Path):
#     try:
#         with path_to_yaml.open('r') as yaml_file:
#             content = yaml.safe_load(yaml_file)
#             if not content:
#                 raise ValueError(f"The YAML file at {path_to_yaml} is empty or improperly formatted.")
            
#             # Create a Config instance
#             return Config(**content)  # Unpacking dictionary keys as arguments
#     except FileNotFoundError:
#         raise FileNotFoundError(f"The file at {path_to_yaml} was not found.")
#     except yaml.YAMLError as exc:
#         raise ValueError(f"Error while parsing YAML file: {exc}")



@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create a list of directories.

    Args:
        path_to_directories (list): List of paths for the directories to create.
        verbose (bool, optional): Whether to log directory creation. Defaults to True.
    """
    for path in path_to_directories:
        try:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Created directory at: {path}")
        except Exception as e:
            logger.error(f"Error creating directory at {path}: {e}")




@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

    