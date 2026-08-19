import pandas as pd

from src.extract.order_details import extract_order_details


def transform_order_details():
    order_details = extract_order_details()

    order_details["subtotal"] = (
        order_details["quantity"] * order_details["unit_price"]
    )

    return order_details


if __name__ == "__main__":
    transformed_data = transform_order_details()

    print("Order details transformed successfully:")
    print(transformed_data)