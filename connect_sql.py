
import pandas as pd
from pathlib import Path
from connect_sql import connect_tables


def load_data():
    """Load SQL tables and save copies as CSV files."""

    tables = connect_tables()

    table_names = [
        "customers",
        "Menu_item",
        "Orders",
        "Rest",
        "Delivery"
    ]

    if len(tables) != len(table_names):
        raise ValueError(
            f"Expected {len(table_names)} tables, "
            f"received {len(tables)}."
        )

    # Create the directory if it doesn't exist
    output_dir = Path("sql") / "Data_SQl"
    output_dir.mkdir(parents=True, exist_ok=True)

    data = {}

    for name, table in zip(table_names, tables):

        if not isinstance(table, pd.DataFrame):
            raise TypeError(
                f"{name} must be a Pandas DataFrame."
            )

        # Save each table to CSV
        csv_path = output_dir / f"{name}.csv"
        table.to_csv(csv_path, index=False)

        data[name] = table

    return data


def clean_data(df):
    """Clean duplicate rows and whitespace in text columns."""

    df = df.copy()

    # Remove duplicate records
    df = df.drop_duplicates()

    # Remove leading and trailing whitespace
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].str.strip()

    # Do not automatically drop missing rows or lowercase
    # every text value, as that may alter valid source data.

    return df


def load_clean_data():
    """Load and clean every table."""

    data = load_data()
    clean_df = {}

    for table_name, table_data in data.items():
        clean_df[table_name] = clean_data(table_data)

    return clean_df