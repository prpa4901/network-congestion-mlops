# pipeline where actual training will be done
from pathlib import Path
import os
import sys

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(PACKAGE_ROOT)

from pred_model.config import config
from pred_model.processing.data_handling import save_pipeline, load_dataset
from pred_model import pipeline as pipe

def perform_training():
    train_data = load_dataset(config.TRAIN_FILE)
    train_y = train_data[config.TARGET]
    pipe.cl_pipeline.fit(train_data[config.FINAL_FEATURES], train_y)
    save_pipeline(pipe.cl_pipeline)

if __name__=='__main__':
    perform_training()
