import pandas as pd


def extract_products():
    file_path = "data/raw/products.csv"

    products = pd.read_csv(file_path)

    return products


if __name__ == "__main__":
    products = extract_products()

    print("Products extracted successfully:")
    print(products)