# Sales ETL Project

## 📌 Descripción

Este es un proyecto personal de Data Engineering en el que estoy construyendo un 
pipeline ETL utilizando Python y PostgreSQL.

La idea del proyecto es trabajar con datos de ventas y recorrer todo el proceso: extraer 
los datos desde PostgreSQL, transformarlos y validarlos con Python y Pandas, y finalmente cargarlos en una tabla `fact_sales`.

El proyecto está organizado por etapas para mantener cada parte del proceso separada y fácil de entender.

---

## 🛠️ Tecnologías utilizadas

- Python
- PostgreSQL
- SQL
- Pandas
- ETL
- SQLAlchemy
- python-dotenv
- Git & GitHub

---

## 📂 Estructura del proyecto

```text
sales-etl-project/
│
├── airflow/
├── config/
├── data/
│
├── sql/
│   ├── create_tables.sql
│   ├── insert_data.sql
│   └── fact_sales.sql
│
├── src/
│   ├── extract/
│   │   ├── customers.py
│   │   ├── products.py
│   │   ├── categories.py
│   │   ├── orders.py
│   │   └── order_details.py
│   │
│   ├── transform/
│   │   ├── order_details_transform.py
│   │   └── sales_transform.py
│   │
│   └── load/
│       └── load_sales.py
│
├── tests/
├── .env
├── .gitignore
└── requirements.txt
```

---

## 🔄 ETL

### Extract

En esta primera etapa se obtienen los datos desde PostgreSQL.
Se trabajan las siguientes tablas:
- `customers`
- `products`
- `categories`
- `orders`
- `order_details`

Los diferentes procesos de extracción están separados en `src/extract/`.

### Transform

Una vez extraídos los datos, se integran utilizando Pandas.
En esta etapa se realizan los joins entre las diferentes tablas, se calcula el subtotal de 
cada línea de venta y se realizan algunas validaciones básicas sobre los datos.

```text
subtotal = quantity × unit_price
```

La lógica de transformación se encuentra en `src/transform/`.

### Load

Por último, los datos ya transformados se cargan nuevamente en PostgreSQL.
El proceso utiliza Pandas y SQLAlchemy, y la información se almacena en la tabla `fact_sales`.

La lógica de carga se encuentra en `src/load/`.