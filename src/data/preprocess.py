# src/data/preprocess.py
import pandas as pd

def preprocess(input_path, output_path):
    df = pd.read_csv(input_path)
    # Example preprocessing: handle missing values
    df = df.fillna(method='ffill')
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path')
    parser.add_argument('output_path')
    args = parser.parse_args()
    preprocess(args.input_path, args.output_path)
