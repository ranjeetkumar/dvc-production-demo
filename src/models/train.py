# src/models/train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

def train(input_path, model_path, params):
    df = pd.read_csv(input_path)
    X = df.drop('target', axis=1)
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(C=params['train']['C'], max_iter=params['train']['max_iter'])
    model.fit(X_train, y_train)
    joblib.dump(model, model_path)

    # Save evaluation metrics
    score = model.score(X_test, y_test)
    with open('metrics.txt', 'w') as f:
        f.write(f"Accuracy: {score}\n")

if __name__ == "__main__":
    import argparse
    import yaml
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path')
    parser.add_argument('model_path')
    parser.add_argument('--params')

    #parser.add_argument '--params'
    args = parser.parse_args()
    
    with open(args.params, 'r') as f:
       params = yaml.safe_load(f)
    print (params)
    train(args.input_path, args.model_path, params)
