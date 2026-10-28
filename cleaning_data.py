# import pandas as pd
# from connect_sql import connect_tables

# def load_data():
#   tables=connect_tables()
#   tablenames=['customers','Menu_item','Orders','Rest','Delivery']
#   i=0
#   for table in tables:
#     table.to_csv(f"sql/Data_SQl/{tablenames[i]}.csv")
#     i+=1
#   data={}
#   i=0
#   for table in tablenames:
#     data[table]=tables[i]
#     i+=1
#   return data

# print(load_data())

# def clean_data(df=pd.DataFrame()):
#    null_values=df.isnull().sum()
#   #  print(null_values)
#    df.dropna(inplace=True)
#    df.drop_duplicates(inplace=True)
#    for col in df.select_dtypes(include='object').columns:
     
#      df[col]=df[col].str.strip()
#      df[col]=df[col].str.lower()
     
#    return df 


# def load_clean_data():

#     data = load_data()

#     clean_df = {}

#     for table_name, table_data in data.items():
#         clean_df[table_name] = table_data

#     return clean_df
# # load_clean_data()


  


import pandas as pd
from connect_sql import connect_tables


def load_data():
    tables = connect_tables()

    # Validate SQL connection results
    if tables is None:
        raise ValueError(
            "connect_tables() returned None. "
            "Check your connect_sql.py function."
        )

    tablenames = [
        'customers',
        'Menu_item',
        'Orders',
        'Rest',
        'Delivery'
    ]

    # Convert results into a list
    tables = list(tables)

    if len(tables) != len(tablenames):
        raise ValueError(
            f"Expected {len(tablenames)} tables, "
            f"but received {len(tables)}."
        )

    data = {}

    for name, table in zip(tablenames, tables):
        if not isinstance(table, pd.DataFrame):
            raise TypeError(
                f"Expected a DataFrame for {name}, "
                f"got {type(table).__name__}."
            )

        # Save SQL data as CSV
        table.to_csv(
            f"sql/Data_SQl/{name}.csv",
            index=False
        )

        data[name] = table

    return data


def clean_data(df):
    df = df.copy()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Clean text columns
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip()
        df[col] = df[col].str.lower()

    return df


def load_clean_data():
    data = load_data()

    clean_df = {}

    for table_name, table_data in data.items():
        clean_df[table_name] = clean_data(table_data)

    return clean_df