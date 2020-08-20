import os
from os import path
import pandas as pd



def get_train_features():
    if path.isfile('data/raw/h1n1_train_features.csv'):
        print('Training features already acquired.')
    else:
        train_features = pd.read_csv('https://drivendata-prod.s3.amazonaws.com/data/66/public/training_set_features.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARVBOBDCY3EFSLNZR%2F20200820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200820T223045Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d3321df4e95486ff27e43ee21e96626661fbf2edd573ce6564583b60c276805c')        
        train_features.to_csv('data/raw/h1n1_train_features.csv', index_label='respondent_id')
        print('Train features acquired!')
        
def get_train_labels():
    if path.isfile('data/raw/h1n1_train_labels.csv'):
        print('Training labels already acquired.')
    else:
        train_labels = pd.read_csv('https://drivendata-prod.s3.amazonaws.com/data/66/public/training_set_labels.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARVBOBDCY3EFSLNZR%2F20200820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200820T223045Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=82bd04bc861028a7cd3a5888f9dfce5c3840390cf1b453f6e0a714215373a27a')
        train_labels.to_csv("data/raw/h1n1_train_labels.csv", index_label='respondent_id')
        print('Train features acquired!')
        
def get_test_features():
    if path.isfile('data/raw/h1n1_test_features.csv'):
        print('Test features already acquired.')
    else:
        test_features = pd.read_csv('https://drivendata-prod.s3.amazonaws.com/data/66/public/test_set_features.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARVBOBDCY3EFSLNZR%2F20200820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200820T223045Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e6234d019d447d227bbaff3c48288ea38d54b76078422d6620934bffd86c149e')
        test_features.to_csv("data/raw/h1n1_test_features.csv", index_label='respondent_id')
        print('Test features acquired!')

def run():
    print('Acquiring train features...')
    get_train_features()
    print('Acquiring train labels...')
    get_train_labels()
    print('Acquiring test features...')
    get_test_features()
    print('Acquire completed!')