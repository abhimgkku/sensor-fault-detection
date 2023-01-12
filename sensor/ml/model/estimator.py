from sensor.constant.training_pipeline import SAVED_MODEL_DIR,MODEL_FILE_NAME
import os,sys
class TargetValueMapping:
    def __init__(self):
        self.neg:int = 0
        self.pos:int = 1
        
    def to_dict(self):
        return self.__dict__
    
    def reverse_mapping(self):
        mapping = self.to_dict()
        return dict(zip(mapping.values(),mapping.keys()))
    
class SensorModel:

    def __init__(self,preprocessor,model):
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e:
            raise e
    
    def predict(self,x):
        try:
            x_transform = self.preprocessor.transform(x)
            y_hat = self.model.predict(x_transform)
            return y_hat
        except Exception as e:
            raise e
class ModelResolver:
    def __init__(self,model_dir=SAVED_MODEL_DIR):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise e
    def get_best_model_path(self,):
        try:
            timestamps = list(map(int,os.listdir(self.model_dir)))
            latest_timestamp = max(timestamps)
            latest_model_path = os.path.join(self.model_dir,f"{latest_timestamp}",MODEL_FILE_NAME)
            return latest_model_path
        except Exception as e:
            raise e
    def is_model_exist(self)->bool:
        try:
            if not os.path.exists(self.model_dir):
                return False
            timestamp = os.listdir(self.model_dir)
            if len(timestamp) == 0:
                return False
            if not os.path.exists(self.get_best_model_path()):#to check if latest model is available
                return False
            return True
        except Exception as e:
            raise e