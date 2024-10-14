# src/features/build_features.py
import pandas as pd

def build_features(input_path, output_path):
    df = pd.read_csv(input_path)
    # Example feature: add a new feature
    df['feature3'] = df['feature1'] * df['feature2']
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path')
    parser.add_argument('output_path')
    args = parser.parse_args()
    build_features(args.input_path, args.output_path)
