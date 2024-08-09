# pipeline where actual training will be done
from pathlib import Path
import os
import sys

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
print(PACKAGE_ROOT)
sys.path.append(PACKAGE_ROOT)

from config import config
from processing.data_handling import save_pipeline, load_dataset
import pipeline as pipe

def perform_training():
    train_data = load_dataset(config.TRAIN_FILE)
    train_y = train_data[config.TARGET]
    pipe.cl_pipeline.fit(train_data[config.FEATURES], train_y)
    save_pipeline(pipe.cl_pipeline)

if __name__=='__main__':
    perform_training()
