import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

from src.transform.sales_transform import transform_sales


def load_sales():
    load_dotenv()

    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")

    connection_string = (
        f"postgresql+psycopg2://{db_user}:{db_password}"
        f"@{db_host}:{db_port}/{db_name}"
    )

    engine = create_engine(connection_string)

    sales = transform_sales()

    sales.to_sql(
        "fact_sales",
        engine,
        if_exists="append",
        index=False
    )

    print("Sales loaded successfully.")
    print("Rows loaded:", len(sales))


if __name__ == "__main__":
    load_sales()