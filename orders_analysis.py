from cleaning_data import  load_clean_data
orders=load_clean_data()['Orders']
print(orders)



def analyze_order(Orders):
  revenue=Orders['total_price'].sum()
  total_orders=orders['order_id'].nunique()
  average_order_value=Orders['total_price'].mean()
  
  return {'Revenue':revenue,'Total_Orders':int(total_orders),'Average Order value':float(average_order_value)}

print(analyze_order(orders))

def monthly_orders(orders):
   orders['month']=orders['order_datetime'].dt.to_period('M').astype('str')
   return orders.groupby(by ='month').count()
 
print(monthly_orders(orders))