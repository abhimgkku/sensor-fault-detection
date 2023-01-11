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