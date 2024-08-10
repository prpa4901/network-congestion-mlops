# file used for doing actual test prediction
from pathlib import Path
import pandas as pd
import numpy as np
import os
import sys

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
print("Predict:"+str(PACKAGE_ROOT))
sys.path.append(str(PACKAGE_ROOT))
# sys.path.append(PACKAGE_ROOT)


from pred_model.config import config  
from pred_model.processing.data_handling import load_pipeline, load_dataset

classification_model = load_pipeline(config.MODEL_NAME)

def predict_congestion(data_input):
    try:
        data = pd.DataFrame(data_input)
    except Exception as e:
        data = load_dataset(data_input)
    pred = classification_model.predict(data[config.FEATURES])
    result = {'prediction': pred}
    return result

if __name__ == "__main__":
    predict_congestion()

