
from cleaning_data import load_clean_data

def customer_analysis(customer_df, orders_df):
  
    total_customers = customer_df['customer_id'].nunique()
    gender_count = customer_df['gender'].value_counts()

    # Total unique orders
    total_orders = orders_df['order_id'].nunique()
    
    # Extract city from address
    customer_df = customer_df.copy()
    customer_df['city'] = customer_df['Address'].apply(
        lambda address: address.split(',')[-1].strip()
        if isinstance(address, str) else 'Unknown'
    )

    city_count = customer_df['city'].value_counts()
    # repeated_customer=orders['customer_id'].value.counts()>1
    # total_repeted_customers=repeated_customer.sum()

    return {
        'Total_customers': total_customers,
        'Gender count': gender_count,
        'city count': city_count,
        'order_count': total_orders,
        # 'repeted_customers':int(total_repeted_customers)
    }


# Load data
data = load_clean_data()

# Select DataFrames
customer_df = data['customers']
orders_df = data['Orders']

# Run customer analysis
result = customer_analysis(customer_df, orders_df)

# Display results
print("\nTotal Customers:", result['Total_customers'])
print("Total Orders:", result['order_count'])


print("\nGender Count:")
print(result['Gender count'])

print("\nCity Count:")
print(result['city count'])