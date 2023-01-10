from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.pipeline.training_pipeline import TrainingPipeline
if __name__ == '__main__':
    training_pipeline = TrainingPipeline()
    training_pipeline.run_pipeline()
    
    
    #mongodb_client = MongoDBClient()
    #print("collection name:"mongodb_client.database.list_collection_names())
    