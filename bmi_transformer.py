
# merci à Victor
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

class BmiTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, bins : np.ndarray):
        self.bins = bins
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X_initial):
        X = pd.DataFrame(X_initial)
        X["bmi"] = pd.cut(X['bmi'], bins=self.bins, labels=False, right=False, include_lowest=True)
        return X