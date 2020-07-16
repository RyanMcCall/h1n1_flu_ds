from os import path
import pandas as pd

def get_h1n1_features():
    if path.isfile('../data/raw/h1n1_features.csv'):
        return pd.read_csv('../data/raw/h1n1_features.csv')
    else:
        data = pd.read_csv('https://s3.amazonaws.com/drivendata-prod/data/66/public/training_set_features.csv')
        pd.to_csv('../data/raw/h1n1_features.csv', index=False)
        return data
        
def get_h1n1_labels():
    if path.isfile('../data/raw/h1n1_labels.csv'):
        return pd.read_csv('')

def run():
    "Obtain: downloading raw data files..."