import pandas as pd

def fill_all_with_missing(df):
    return df.fillna('missing')

def run():
    print("Prepare: cleaning obtained data...")
    
    acquired_train_features = pd.read_csv('data/raw/h1n1_train_features.csv')
    acquired_test_features = pd.read_csv('data/raw/h1n1_test_features.csv')
    acquired_train_labels = pd.read_csv('data/raw/h1n1_train_labels.csv')
    
    prepd_train_features = fill_all_with_missing(acquired_train_features)
    prepd_test_features = fill_all_with_missing(acquired_test_features)
    
    joined_train_data = prepd_train_features.merge(acquired_train_labels, on='respondent_id')
    
    joined_train_data.to_csv("data/interim/prepared_h1n1_train_features.csv", index_label='respondent_id')
    prepd_test_features.to_csv("data/interim/prepared_h1n1_test_features.csv", index_label='respondent_id')
    
    print("Completed Preparation")