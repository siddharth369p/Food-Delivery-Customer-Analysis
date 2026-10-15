import pandas as pd
from connect_sql import connect_tables

tables=connect_tables()
tablenames=['customers','Menu_item','Orders','Delivery','Rest']
i=0

for table in tables:
 table.to_csv(f"Data_SQl/{tablenames[i]}.csv")
 i+=1

