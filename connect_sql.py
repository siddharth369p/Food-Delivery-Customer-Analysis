
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL


def connect_database():
    """Create and test the SQL Server connection."""

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

    try:
        with engine.connect() as connection:
            connection.exec_driver_sql("SELECT 1")

        print("Database connected successfully!")
        return engine, True

    except Exception as error:
        engine.dispose()
        print(f"Database connection failed: {error}")
        return None, False


def connect_tables():
    """Fetch all five database tables as Pandas DataFrames."""

    engine, status = connect_database()

    if not status or engine is None:
        raise ConnectionError(
            "Could not connect to SQL Server. "
            "Check your server name and database."
        )

    try:
        customers = pd.read_sql_query(
            "SELECT * FROM customers", engine
        )

        menu_item = pd.read_sql_query(
            "SELECT * FROM Menu_item", engine
        )

        orders = pd.read_sql_query(
            "SELECT * FROM Orders", engine
        )

        rest = pd.read_sql_query(
            "SELECT * FROM Restaurants", engine
        )

        delivery = pd.read_sql_query(
            "SELECT * FROM Delivery", engine
        )

        print("All five tables loaded successfully.")

        return customers, menu_item, orders, rest, delivery

    except Exception as error:
        print(f"Failed to load database tables: {error}")
        raise

    finally:
        engine.dispose()