import pandas as pd

def summarize_data(file_path):
    df = pd.read_csv(file_path)

    print("Shape:", df.shape)
    print("\nColumns:", df.columns.tolist())
    print("\nMissing Values:\n", df.isnull().sum())
    print("\nSummary Stats:\n", df.describe())

# Example usage
# summarize_data("data.csv")