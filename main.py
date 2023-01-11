from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.pipeline.training_pipeline import TrainingPipeline
import os,sys
from sensor.logger import logging
if __name__ == '__main__':
    try:
        training_pipeline = TrainingPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        logging.exception(e)  
    
    #mongodb_client = MongoDBClient()
    #print("collection name:"mongodb_client.database.list_collection_names())
    