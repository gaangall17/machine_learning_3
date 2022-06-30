import pandas as pd
import joblib

def load_from_csv(path):
    return pd.read_csv(path)

def load_from_mysql():
    pass

def features_target(dataset, drop_cols, target):
    X = dataset.drop(drop_cols, axis=1)
    y = dataset[target]
    return X, y

def model_export(clf, score):
    joblib.dump(clf, './ml_pro/models/best_model.pkl')