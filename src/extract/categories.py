import pandas as pd


def extract_categories():
    file_path = "data/raw/categories.csv"

    categories = pd.read_csv(file_path)

    return categories


if __name__ == "__main__":
    categories = extract_categories()

    print("Categories extracted successfully:")
    print(categories)