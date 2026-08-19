import pandas as pd


def extract_customers():
    file_path = "data/raw/customers.csv"

    customers = pd.read_csv(file_path)

    return customers


if __name__ == "__main__":
    customers = extract_customers()

    print("Customers extracted successfully:")
    print(customers)