
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
    def __init__(self, bins):
        self.bins = bins
    
    def fit(self, X, y=None):
        return self
    
    def get_feature_names_out(self, input_features = None) :
        return np.array['bmi2']

    def categorize(self, value) :
        current_category = 0 
        for category in self.bins :
            if value < category :
                return current_category
            else : current_category +=1
        return current_category

    def transform(self, X_initial):
        X = pd.DataFrame(X_initial)
        X["bmi"] = X_initial["bmi"].apply( lambda val : self.categorize(val))
        return X
