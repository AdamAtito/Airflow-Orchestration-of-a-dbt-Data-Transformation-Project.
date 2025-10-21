import requests
import pandas as pd 
import duckdb
import json

def load_data():
    url = 'https://fakestoreapi.com/products/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df_products = pd.json_normalize(data, sep="_")
        conn = duckdb.connect("dev.duckdb")
        conn.execute("CREATE OR REPLACE TABLE products AS SELECT * FROM df_products")
        conn.close()
    url = 'https://fakestoreapi.com/carts'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df_carts = pd.json_normalize(data, record_path=['products'], meta=['id', 'userId', 'date'], sep="_")
        df_carts.rename(
            columns={
                'id': 'cart_id',
                'userId': 'user_id',
                'date': 'cart_date',
                'productId': 'product_id',
                "quantity": "quantity"
            },
            inplace=True
        )
        
        conn = duckdb.connect("dev.duckdb")
        conn.execute("CREATE OR REPLACE TABLE carts AS SELECT * FROM df_carts")
        conn.close()
    url = 'https://fakestoreapi.com/users'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df_users = pd.json_normalize(data, sep="_")
        conn = duckdb.connect("dev.duckdb")
        conn.execute("CREATE OR REPLACE TABLE users AS SELECT * FROM df_users")
        conn.close()    
        