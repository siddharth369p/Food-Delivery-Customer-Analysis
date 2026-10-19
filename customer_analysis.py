##customer Analysis
from cleaning_data import load_clean_data

def customer_analysis(customer_df):
  total_customers=customer_df['customer_id'].nunique()
  total_count=customer_df['Gender'].value_counts()
  city=[]
  for address in customer_df['Address']:
    city.append(address.split(',')[-1].strip())
  
  customer_df['city']=city
  city_count=customer_df['city'].value_counts() 
  
  return {'Total_customers':total_customers,
          'Gender count':gender_count,
          'city count':city_count}

customer_df=load_clean_data()['Customers']
customer_analysis(customer_df)

 
