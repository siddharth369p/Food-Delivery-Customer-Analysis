import pandas as pd
from connect_sql import connect_tables

def load_data():
  tables=connect_tables()
  tablenames=['customers','Menu_item','Orders','Rest','Delivery']
  i=0
  for table in tables:
    table.to_csv(f"sql/Data_SQl/{tablenames[i]}.csv")
    i+=1
  data={}
  i=0
  for table in tablenames:
    data[table]=tables[i]
    i+=1
  return data

print(load_data())

def clean_data(df=pd.DataFrame()):
   null_values=df.isnull().sum()
  #  print(null_values)
   df.dropna(inplace=True)
   df.drop_duplicates(inplace=True)
   for col in df.select_dtypes(include='object').columns:
     df[col]=df[col].str.strip()
   return df 

def load_clean_data():
  data=load_data()
  clean_df={}
  for table_name,table_data in data.items():
    clean_data[table_name]=clean_data[table_data]
  return clean_df

# load_clean_data()


  

