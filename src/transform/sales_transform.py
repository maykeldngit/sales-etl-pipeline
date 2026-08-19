from src.extract.customers import extract_customers
from src.extract.products import extract_products
from src.extract.categories import extract_categories
from src.extract.orders import extract_orders
from src.extract.order_details import extract_order_details

def transform_sales():
    customers = extract_customers()
    products = extract_products()
    categories = extract_categories()
    orders = extract_orders()
    order_details = extract_order_details()

    sales = orders.merge(
        customers,
        on="customer_id",
        how="inner"
    )

    sales = sales.merge(
        order_details,
        on="order_id",
        how="inner"
    )

    sales = sales.merge(
        products,
        on="product_id",
        how="inner"
    )

    sales = sales.merge(
        categories,
        on="category_id",
        how="inner"
    )

    sales["subtotal"] = sales["quantity"] * sales["unit_price"]

    sales = sales[
        [
            "order_detail_id",
            "order_id",
            "customer_id",
            "product_id",
            "category_id",
            "order_date",
            "quantity",
            "unit_price",
            "subtotal"
        ]
    ]

    return sales

if __name__ == "__main__":
    sales = transform_sales()

    print("Sales transformed successfully:")
    print(sales)

    print("\nValidation:")
    print("Rows:", len(sales))
    print("Null values:", sales.isnull().sum().sum())
    print("Invalid quantities:", (sales["quantity"] <= 0).sum())
    print(
        "Invalid subtotals:",
        (sales["subtotal"] != sales["quantity"] * sales["unit_price"]).sum()
    )