

# from cleaning_data import load_clean_data

# def customer_analysis(customer_df, orders_df):

#     # 1. Total unique customers
#     total_customers = customer_df['customer_id'].nunique()

#     # 2. Gender analysis
#     gender = customer_df['gender'].astype('string').str.strip().str.lower()

#     total_male = gender.eq('male').sum()
#     total_female = gender.eq('female').sum()

#     gender_count = gender.value_counts()

#     # 3. Total unique orders
#     total_orders = orders_df['order_id'].nunique()

#     # 4. Extract city from address
#     customer_df = customer_df.copy()

#     customer_df['city'] = customer_df['Address'].apply(
#         lambda address: address.split(',')[-1].strip()
#         if isinstance(address, str) else 'Unknown'
#     )

#     city_count = customer_df['city'].value_counts()

#     # 5. Find repeat customers
#     customer_order_counts = orders_df['customer_id'].value_counts()

#     repeated_customer = customer_order_counts[
#         customer_order_counts > 1
#     ]

#     total_repeated_customers = len(repeated_customer)
    
#     # new customers
    
#     new_customers=total_customers-total_repeated_customers
   

#     # 6. Return all analysis results
#     return {
#         'Total_customers': total_customers,
#         'Total_male': int(total_male),
#         'Total_female': int(total_female),
#         'Gender count': gender_count,
#         'city count': city_count,
#         'order_count': total_orders,
#         'repeated_customers': total_repeated_customers,
#         'new customers':new_customers
    
#     }


# # # # Load data
# # # data = load_clean_data()

# # # # Select DataFrames
# # # customer_df = data['customers']
# # # orders_df = data['Orders']

# # # # Run customer analysis
# # # result = customer_analysis(customer_df, orders_df)

# # # # Display results
# # # print("\n========== CUSTOMER ANALYSIS ==========")

# # # print("\nTotal Unique Customers:", result['Total_customers'])

# # # print("Total Male Customers:", result['Total_male'])
# # # print("Total Female Customers:", result['Total_female'])

# # # print("\nGender Count:")
# # # print(result['Gender count'])

# # # print("\nCity-wise Customer Count:")
# # # print(result['city count'])

# # # print("\nTotal Unique Orders:", result['order_count'])

# # # print("Total Repeat Customers:", result['repeated_customers'])



# # import pandas as pd


# # def customer_analysis(customer_df, orders_df):

# #     # Work on copies to avoid modifying the original DataFrames
# #     customer_df = customer_df.copy()
# #     orders_df = orders_df.copy()

# #     # 1. Total unique customers
# #     total_customers = customer_df['customer_id'].nunique()

# #     # 2. Gender analysis
# #     gender = (
# #         customer_df['gender']
# #         .astype('string')
# #         .str.strip()
# #         .str.lower()
# #     )

# #     total_male = int(gender.eq('male').sum())
# #     total_female = int(gender.eq('female').sum())

# #     gender_count = gender.value_counts()

# #     # 3. Total unique orders
# #     total_orders = orders_df['order_id'].nunique()

# #     # 4. Extract city from customer address
# #     customer_df['city'] = customer_df['Address'].apply(
# #         lambda address: address.split(',')[-1].strip()
# #         if isinstance(address, str) and address.strip()
# #         else 'Unknown'
# #     )

# #     city_count = customer_df['city'].value_counts()

# #     # 5. Count unique orders for each customer
# #     customer_order_counts = (
# #         orders_df.dropna(subset=['customer_id', 'order_id'])
# #         .groupby('customer_id')['order_id']
# #         .nunique()
# #     )

# #     # Customers with more than one unique order
# #     repeated_customer = customer_order_counts[
# #         customer_order_counts > 1
# #     ]

# #     total_repeated_customers = int(len(repeated_customer))

# #     # 6. Customers who have placed exactly one order
# #     one_order_customers = customer_order_counts[
# #         customer_order_counts == 1
# #     ]

# #     # 7. Customers who have never ordered
# #     customers_with_orders = set(customer_order_counts.index)
# #     all_customers = set(customer_df['customer_id'].dropna().unique())

# #     customers_never_ordered = all_customers - customers_with_orders
# #     total_customers_never_ordered = len(customers_never_ordered)

# #     # 8. Return results
# #     return {
# #         'Total_customers': total_customers,
# #         'Total_male': total_male,
# #         'Total_female': total_female,
# #         'Gender count': gender_count,
# #         'city count': city_count,
# #         'order_count': total_orders,
# #         'repeated_customers': total_repeated_customers,
# #         'one_order_customers': len(one_order_customers),
# #         'customers_never_ordered': total_customers_never_ordered
# #     }






from cleaning_data import load_clean_data


def customer_analysis(customer_df, orders_df):

    customer_df = customer_df.copy()
    orders_df = orders_df.copy()

    # 1. Total unique customers
    total_customers = customer_df['customer_id'].nunique()

    # 2. Gender analysis
    gender = (
        customer_df['gender']
        .astype('string')
        .str.strip()
        .str.lower()
    )

    total_male = int(gender.eq('male').sum())
    total_female = int(gender.eq('female').sum())
    gender_count = gender.value_counts()

    # 3. Total unique orders
    total_orders = orders_df['order_id'].nunique()

    # 4. Extract city from address
    customer_df['city'] = customer_df['Address'].apply(
        lambda address: address.split(',')[-1].strip()
        if isinstance(address, str) and address.strip()
        else 'Unknown'
    )

    city_count = customer_df['city'].value_counts()

    # 5. Count unique orders per customer
    customer_order_counts = (
        orders_df.dropna(subset=['customer_id', 'order_id'])
        .groupby('customer_id')['order_id']
        .nunique()
    )

    # 6. Customers with multiple orders
    total_repeated_customers = int(
        (customer_order_counts > 1).sum()
    )

    # 7. Customers with exactly one order
    new_customers = int(
        (customer_order_counts == 1).sum()
    )

    # 8. Customers who never ordered
    customers_with_orders = set(customer_order_counts.index)
    all_customers = set(customer_df['customer_id'].dropna())

    customers_never_ordered = len(
        all_customers - customers_with_orders
    )

    # 9. Return analysis results
    return {
        'Total_customers': total_customers,
        'Total_male': total_male,
        'Total_female': total_female,
        'Gender count': gender_count,
        'city count': city_count,
        'order_count': total_orders,
        'repeated_customers': total_repeated_customers,
        'new customers': new_customers,
        'customers_never_ordered': customers_never_ordered
    }