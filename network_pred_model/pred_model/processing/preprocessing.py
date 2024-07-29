from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.base import BaseEstimator,TransformerMixin

from pathlib import Path
import os
import sys

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent.parent
sys.path.append(str(PACKAGE_ROOT))

from pred_model.config import config
import numpy as np

class MeanImputer(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        self.variables = variables

    def fit(self, X, y=None):
        self.mean_dict = {}
        for col in self.variables:
            self.mean_dict[col] = X[col].mean()
        return self

    def transform(self, X):
        X = X.copy()
        for col in self.variables:
            X[col].fillna(self.mean_dict[col], inplace=True)
        return X

class ModeImputer(BaseEstimator,TransformerMixin):
    def __init__(self,variables=None):
        self.variables = variables
    
    def fit(self,X,y=None):
        self.mode_dict = {}
        for col in self.variables:
            self.mode_dict[col] = X[col].mode()[0]
        return self
    
    def transform(self,X):
        X = X.copy()
        for col in self.variables:
            X[col].fillna(self.mode_dict[col],inplace=True)
        return X

#DROPPING THE COLUMNS
class DropColums(BaseEstimator, TransformerMixin):
    def __init__(self, variables_to_drop=None):
        self.variables_to_drop = variables_to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X = X.drop(self.variables_to_drop, inplace=True)
        return X

# FEATURE ENGINEERING
class NewFeatureEngg(BaseEstimator, TransformerMixin):
    def __init__(self, feat_map=None):
        self.feat_map = feat_map

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        for new_feat,cols in self.feat_map.items():
            if new_feat == 'combined_load':
                X[new_feat] = X[cols[0]] + X[cols[1]]
            elif new_feat == 'efficiency':
                X[new_feat] = X[cols[0]] / (X[cols[1]] + 1)
            elif new_feat == 'reliability_issues':
                X[new_feat] == X[cols[0]].fillna(0)+X[cols[1]].fillna(0)
            elif new_feat == 'signal_to_bandwidth':
                X[new_feat] = X[cols[0]] / (X[cols[1]])   
        return X

# LABEL ENCODING
class CustomLabelEncoder(BaseEstimator,TransformerMixin):
    def __init__(self, variables=None):
        self.variables=variables
    
    def fit(self, X,y):
        self.label_dict = {}
        for var in self.variables:
            t = X[var].value_counts().sort_values(ascending=True).index 
            self.label_dict[var] = {k:i for i,k in enumerate(t,0)}
        return self
    
    def transform(self,X):
        X=X.copy()
        for feature in self.variables:
            X[feature] = X[feature].map(self.label_dict[feature])
        return X


# LOG TRANSFORMING
class LogTransformer(BaseEstimator,TransformerMixin):
    def __init__(self, variables=None):
        self.variables=variables
    
    def fit(self, X,y):
        return self
    
    def transform(self,X):
        X = X.copy()
        for col in self.variables:
            if (X[col] <= 0).any():
                min_val = X[col].min()
                constant = abs(min_val) + 1
                X[col] += constant
            X[col] = np.log1p(X[col])
        return X