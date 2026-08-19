import pandas as pd


def extract_orders():
    file_path = "data/raw/orders.csv"

    orders = pd.read_csv(file_path)

    return orders


if __name__ == "__main__":
    orders = extract_orders()

    print("Orders extracted successfully:")
    print(orders)