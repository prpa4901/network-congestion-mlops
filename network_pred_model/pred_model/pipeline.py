# file used for defining the stages of processing the data

from sklearn.pipeline import Pipeline
from pathlib import Path
import os
import sys

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from pred_model.config import config
from pred_model.processing import preprocessing as pp
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier



pipeline = Pipeline([
    ('MeanImputation', pp.MeanImputer(config.NUM_COLS)),
    ('ModeImputation', pp.ModeImputer(config.CAT_COLS)),
    ('FeatureEngineering', pp.NewFeatureEngg(config.EXISTING_COLS_FOR_NEW_FEATURES)),
    ('DropFeatures', pp.DropColums(config.FEATURES_TO_DROP)),
    ('LabelEncoding', pp.CustomLabelEncoder(config.CAT_COLS)),
    ('LogTransform', pp.LogTransformer(config.LOG_TRANSFORM_COLS)),
    ('Scaling', MinMaxScaler()),
    ('RandomForestClassifier', RandomForestClassifier(n_estimators=100, random_state=0))
    ]
)