
# merci à ChatGPT
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# Créer un transformateur personnalisé utilisant numpy.digitize
class CustomDigitizer(BaseEstimator, TransformerMixin):
    def __init__(self, bins):
        self.bins = bins
    
    def fit(self, X, y=None):
        # Aucun apprentissage nécessaire, seulement l'enregistrement des bins
        return self
    
    def transform(self, X):
        # Applique digitize pour discrétiser les données
        return np.digitize(X, self.bins)  # Chaque valeur de X sera assignée à un bin