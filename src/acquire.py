import os
from os import path
import pandas as pd



def get_train_features():
    if path.isfile('data/raw/h1n1_train_features.csv'):
        print('Training features already acquired.')
    else:
        train_features = pd.read_csv('https://s3.amazonaws.com/drivendata-prod/data/66/public/training_set_features.csv')        
        train_features.to_csv('data/raw/h1n1_train_features.csv', index=False)
        print('Train features acquired!')
        
def get_train_labels():
    if path.isfile('data/raw/h1n1_train_labels.csv'):
        print('Training labels already acquired.')
    else:
        train_labels = pd.read_csv('https://s3.amazonaws.com/drivendata-prod/data/66/public/training_set_labels.csv')
        train_labels.to_csv("data/raw/h1n1_train_labels.csv", index=False)
        print('Train features acquired!')
        
def get_test_features():
    if path.isfile('data/raw/h1n1_test_features.csv'):
        print('Test features already acquired.')
    else:
        test_features = pd.read_csv('https://s3.amazonaws.com/drivendata-prod/data/66/public/test_set_features.csv')
        test_features.to_csv("data/raw/h1n1_test_features.csv", index=False)
        print('Test features acquired!')

def run():
    print('Acquiring train features...')
    get_train_features()
    print('Acquiring train labels...')
    get_train_labels()
    print('Acquiring test features...')
    get_test_features()
    print('Acquire completed!')