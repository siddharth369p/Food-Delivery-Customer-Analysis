

from cleaning_data import load_clean_data

def customer_analysis(customer_df, orders_df):

    # 1. Total unique customers
    total_customers = customer_df['customer_id'].nunique()

    # 2. Gender analysis
    gender = customer_df['gender'].astype('string').str.strip().str.lower()

    total_male = gender.eq('male').sum()
    total_female = gender.eq('female').sum()

    gender_count = gender.value_counts()

    # 3. Total unique orders
    total_orders = orders_df['order_id'].nunique()

    # 4. Extract city from address
    customer_df = customer_df.copy()

    customer_df['city'] = customer_df['Address'].apply(
        lambda address: address.split(',')[-1].strip()
        if isinstance(address, str) else 'Unknown'
    )

    city_count = customer_df['city'].value_counts()

    # 5. Find repeat customers
    customer_order_counts = orders_df['customer_id'].value_counts()

    repeated_customer = customer_order_counts[
        customer_order_counts > 1
    ]

    total_repeated_customers = len(repeated_customer)
   

    # 6. Return all analysis results
    return {
        'Total_customers': total_customers,
        'Total_male': int(total_male),
        'Total_female': int(total_female),
        'Gender count': gender_count,
        'city count': city_count,
        'order_count': total_orders,
        'repeated_customers': total_repeated_customers
    }


# Load data
data = load_clean_data()

# Select DataFrames
customer_df = data['customers']
orders_df = data['Orders']

# Run customer analysis
result = customer_analysis(customer_df, orders_df)

# Display results
print("\n========== CUSTOMER ANALYSIS ==========")

print("\nTotal Unique Customers:", result['Total_customers'])

print("Total Male Customers:", result['Total_male'])
print("Total Female Customers:", result['Total_female'])

print("\nGender Count:")
print(result['Gender count'])

print("\nCity-wise Customer Count:")
print(result['city count'])

print("\nTotal Unique Orders:", result['order_count'])

print("Total Repeat Customers:", result['repeated_customers'])


