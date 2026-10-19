
import pandas as pd
import pyodbc
from sqlalchemy import create_engine


from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

# SQL Server connection details


# def connect_database():
#   try:
#     engine=create_engine(url="mssql+pyodbc://root:root@SID369/food_delivery")
  
   
#   except Exception as e:
#         print("Connection failed:", e)
#         return None
#   else:
#     return engine

from sqlalchemy import create_engine
from sqlalchemy.engine import URL

def connect_database():
    try:
        connection_url = URL.create(
            "mssql+pyodbc",
            query={
                "odbc_connect": (
                    "DRIVER={ODBC Driver 17 for SQL Server};"
                    "SERVER=SID369;"
                    "DATABASE=food_delivery;"
                    "Trusted_Connection=yes;"
                )
            }
        )

        engine = create_engine(connection_url)

        with engine.connect() as conn:
            print("Database connected successfully!")

        return engine

    except Exception as e:
        print("Database connection failed:", e)
        return None
    
# connecting the tables-----

def connect_tables():
    try:
        engine = connect_database()  # Call the function

        if engine is None:
            print("Database connection failed")
            return

        customers = pd.read_sql_query(
            "SELECT * FROM customers;",
            engine
        )

        Menu_item = pd.read_sql_query(
            "SELECT * FROM Menu_item;",
            engine
        )
        delivery=pd.read_sql_query(
            "SELECT * FROM Delivery;",
            engine)
        
        rest=pd.read_sql_query(
            "SELECT * FROM Restaurants;",
            engine)
        orders=pd.read_sql_query(
            "SELECT * FROM Orders;",
            engine)
        
        # print("Customers Table:")
        # print(customers)

        # print("\nMenu Item Table:")
        # print(Menu_item)

    except Exception as e:
        print("Connection failed to tables:", e)
    else:
      return customers,Menu_item,orders,rest,delivery

# connect_tables() ## call the function
   


