import pandas as pd


def extract_order_details():
    file_path = "data/raw/order_details.csv"

    order_details = pd.read_csv(file_path)

    return order_details


if __name__ == "__main__":
    order_details = extract_order_details()

    print("Order details extracted successfully:")
    print(order_details)