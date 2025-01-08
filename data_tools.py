import pandas as pd 
import numpy as np

class DataTools() :
    def __init__(self): 
        pass
    
    def clean_data(self, dataframe : pd.DataFrame) -> pd.DataFrame :
        dataframe2 = dataframe.copy()
        dataframe2["is_male"] = dataframe2["sex"].apply( lambda x : 1 if x == "male" else 0)
        dataframe2["is_smoker"] = dataframe2["smoker"].apply( lambda x : 1 if x == "yes" else 0)
        dataframe2["is_north"] = dataframe2["region"].apply( lambda x : 1 if str(x).startswith("north") else 0)
        dataframe2["is_west"] = dataframe2["region"].apply( lambda x : 1 if str(x).endswith("west") else 0)

        dataframe2 = dataframe2.drop("sex", axis=1)
        dataframe2 = dataframe2.drop("smoker", axis=1)
        dataframe2 = dataframe2.drop("region", axis=1)

        return dataframe2
