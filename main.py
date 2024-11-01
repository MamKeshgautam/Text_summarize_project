# from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

from src.textSummarizer.utils.data_config import *

STAGE_NAME = "Data Ingestion Stage"

try:    
    # logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    url = "https://github.com/entbappy/Branching-tutorial/raw/master/summarizer-data.zip"
    download_and_unzip(url)
    # logger.info(f">>>>>>>>>>>>>>>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<")
except Exception as e:  
    # logger.exception(e) 
    raise e
