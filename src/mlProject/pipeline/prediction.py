from pathlib import Path
# import numpy as np
from joblib import load


class PredictionPipeline:
    def __init__(self):
        self.model_load = load(Path("artifacts/model_trainer/model.joblib"))

    
    def predict(self, data):
        predictions = self.model_load.predict(data)
        return predictions
