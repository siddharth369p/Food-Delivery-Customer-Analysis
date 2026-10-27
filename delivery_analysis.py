from cleaning_data import load_clean_data
import pandas as pd

orders=load_clean_data()['Orders']
delivery=load_clean_data()['Delivery']

print(orders,delivery)

# print(load_clean_data().keys())

def analyze_delivery(orders,delivery):
  df=pd.merge(orders,delivery[['order_id','delivery_time']],how='left',on=['order_id'])
  print(df)
  df['delivery_minutes']=df['delivery_time']-df['order_datetime']
  return df

def delivery_status(delivery):
  return delivery['status'].value_counts()


print(delivery_status(delivery))
print(analyze_delivery(orders,delivery))