import pytest 

from pathlib import Path
import os
import sys

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
print("Test path:"+str(PACKAGE_ROOT))
sys.path.append(str(PACKAGE_ROOT))

from pred_model.config import config
from pred_model.processing.data_handling import load_dataset
from pred_model.predict import predict_congestion

@pytest.fixture
def single_entry():
    x = load_dataset(config.TEST_FILE)[:1]
    res = predict_congestion(x)
    return res

def test_single_pred_null(single_entry):
    assert single_entry is not None

def test_single_pred_format(single_entry):
    assert single_entry['prediction'] in (1,0)