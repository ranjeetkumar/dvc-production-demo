# src/models/evaluate.py
import joblib
import pandas as pd

def evaluate(model_path, input_path, metrics_path):
    model = joblib.load(model_path)
    df = pd.read_csv(input_path)
    X = df.drop('target', axis=1)
    y = df['target']
    score = model.score(X, y)
    with open(metrics_path, 'a') as f:
        f.write(f"Evaluation Accuracy: {score}\n")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('model_path')
    parser.add_argument('input_path')
    parser.add_argument ('metrics_path')
    args = parser.parse_args()
    evaluate(args.model_path, args.input_path, args.metrics_path)
