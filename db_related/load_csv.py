import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:postgres@localhost:5432/raw")

df_customers = pd.read_csv("https://dbt-tutorial-public.s3.amazonaws.com/jaffle_shop_customers.csv")

df_customers.to_sql("customers", engine, schema="raw_jaffle_shop", if_exists="replace", index=False)

df_orders = pd.read_csv("https://dbt-tutorial-public.s3.amazonaws.com/jaffle_shop_orders.csv")

df_orders.to_sql("orders", engine, schema="raw_jaffle_shop", if_exists="replace", index=False)

df_payment = pd.read_csv("https://dbt-tutorial-public.s3.amazonaws.com/stripe_payments.csv")

df_payment.to_sql("payment", engine, schema="raw_stripe", if_exists="replace", index=False)