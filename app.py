import streamlit as st
from cleaning_data import load_clean_data
from customer_analysis import customer_analysis
from orders_analysis import analyze_order,monthly_orders
from delivery_analysis import analyze_delivery,delivery_status

st.set_page_config(page_title="Food Delivery Analysis",layout="wide")

st.title("Food Delivery Analysis App 📊")


try:
   data=load_clean_data()
   customer=data['customers']
   menu=data['Menu_item']
   order=data['Orders']
   rest=data['Rest']
   delivery=data['Delivery']
   
except Exception as e:
    st.error("Failed to load data.")
    st.exception(e)
    

CA,OA,DA=st.tabs(['Customer Analysis','Order Analysis','Delivery Analysis'])

with CA:
  st.header("Customer Analysis Report")
  st.divider()
  
  col1,col2,col3=st.columns(3)
  customer_analysis_data=customer_analysis(customer,order)
  col1.header("Total Customer")
  col1.subheader(customer_analysis_data['Total_customers'])
  col2.header("Repeated Customer")
  col2.subheader(customer_analysis_data['repeated_customers'])
  col3.header("New Customer")
  col3.subheader(customer_analysis_data['new customers'])
  
  st.divider()
  
  st.header("Gender Analysis")
  st.bar_chart(customer_analysis_data['Gender count'])
  
  st.divider()
  
  st.header("Area Analysis")
  st.bar_chart(customer_analysis_data['city count'])  

with OA:
  st.header("Order Analysis Report")
  st.divider()
  
  order_analysis_data=analyze_order(order)
  col1,col2,col3=st.columns(3)
  
  col1.header("Total Revenuer")
  col1.subheader(order_analysis_data['Revenue'])
  
  col2.header("Total Orders")
  col2.subheader(order_analysis_data['Total_Orders'])
  
  col3.header("Average Order value")
  col3.subheader(order_analysis_data['Average Order value'])
  st.divider()
  
  monthly_order_data=monthly_orders(order)
  st.header("Monthly Order Analysis")
  st.divider()
  st.line_chart(monthly_order_data)
  
with DA:
  st.header("Delivery Analysis Report🚘")
  st.divider()
  st.header("Delivery Status")
  d_m=analyze_delivery(order,delivery)['delivery_minutes']
  average_delivery_minutes=d_m.mean()
  st.header("Average delivery time")
  st.subheader(average_delivery_minutes)
  
  st.divider()

  status=delivery_status(delivery)
  st.bar_chart(status)
  st.divider()
  st.subheader("Delivery Data Record")
  st.dataframe(analyze_delivery(order,delivery))

st.sidebar.header("Food Delivery Database")
st.sidebar.subheader