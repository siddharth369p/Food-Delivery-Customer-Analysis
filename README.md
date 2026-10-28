# 🍔 Food Delivery Customer Analysis

A data analytics project designed to analyze food delivery customers, orders, restaurants, menu items, and delivery operations using Python, SQL, and an interactive dashboard.

## 📌 Project Overview

The **Food Delivery Customer Analysis** project focuses on transforming raw food delivery data into meaningful business insights. It organizes customer, order, restaurant, menu, and delivery datasets to support analysis of customer behavior, ordering patterns, and delivery performance.

Python is used for data processing and analysis, while SQL supports database querying. The application provides a central interface for exploring analytical results.

## 🎯 Project Objectives

- Analyze total and unique customers.
- Understand customer demographics and purchasing behavior.
- Examine order volume and ordering patterns.
- Evaluate restaurant and menu item performance.
- Analyze delivery operations and delivery status.
- Identify business trends and opportunities for improvement.
- Present analytical results through an interactive dashboard.

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Database & Querying:** SQL, SQL Server
- **Data Analysis:** Pandas, NumPy (where used)
- **Dashboard:** Streamlit
- **Data Sources:** CSV files and SQL database
- **Development Environment:** Visual Studio Code
- **Version Control:** Git and GitHub

## 📁 Project Structure

```text
Food_Delivery_Customer_Analysis/
│
├── sql/
│   ├── Data_SQL/
│   ├── food_delivery_customer_data/
│   │   ├── customers.csv
│   │   ├── Delivery.csv
│   │   ├── Menu_item.csv
│   │   ├── Orders.csv
│   │   ├── Restaurants.csv
│   │   └── README_IMPORT.md
│   ├── SQLQuery1.sql
│   └── Solution1.ssmssln
│
├── app.py
├── connect_sql.py
├── cleaning_data.py
├── customer_analysis.py
├── delivery_analysis.py
├── orders_analysis.py
├── requirements.txt
├── README.md
└── .gitignore
```

*Note: Folder and file names above are normalized for readability. Keep the actual names in your repository unchanged.*

## 📊 Dataset Description

The project includes the following datasets:

| Dataset | Purpose |
|---|---|
| `customers.csv` | Customer information and demographic analysis |
| `Orders.csv` | Order records and purchasing behavior |
| `Restaurants.csv` | Restaurant information and restaurant-level analysis |
| `Menu_item.csv` | Menu items and food item analysis |
| `Delivery.csv` | Delivery records and operational analysis |

The datasets can be loaded into a SQL database for querying and used in Python for data cleaning and analytical processing.

## ⚙️ Key Modules

### 1. Database Connectivity — `connect_sql.py`

Responsible for establishing a connection between Python and the SQL database. This module centralizes database connection logic so other modules can access the required data.

### 2. Data Cleaning — `cleaning_data.py`

Responsible for preparing the raw data for analysis. Depending on the implementation, this can include handling missing values, removing duplicate records, standardizing column values, and correcting data types.

### 3. Customer Analysis — `customer_analysis.py`

Focuses on customer-related metrics, such as unique customer counts, gender distribution, and new versus existing customer analysis, where supported by the dataset.

### 4. Delivery Analysis — `delivery_analysis.py`

Focuses on delivery-related information, such as delivery status, delivery performance, and delivery time, where the necessary fields are available.

### 5. Order Analysis — `orders_analysis.py`

Analyzes order-related information and supports the calculation of order metrics, trends, and other business KPIs defined in the source code.

### 6. Interactive Dashboard — `app.py`

Acts as the main application entry point. It brings together the database, data preparation, and analysis modules to present results through a user interface.

## 📈 Business Questions

The project can help answer questions such as:

1. How many unique customers are present in the dataset?
2. What is the distribution of customers by gender?
3. How many customers are new versus returning?
4. Which restaurants receive the most orders?
5. What are the most frequently ordered menu items?
6. How do order volumes vary across available time periods?
7. What proportion of deliveries are completed, pending, or cancelled?
8. What factors may contribute to delivery delays?
9. Which business areas could benefit from operational improvements?

The questions answered in the running application depend on the available columns and implemented queries.

## 🚀 Installation and Setup

### Prerequisites

- Python installed on your system
- Visual Studio Code
- SQL Server and SQL Server Management Studio, if using the SQL Server database
- Git, if cloning the repository

### Step 1: Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Food_Delivery_Customer_Analysis
```

Replace the placeholder with your actual repository URL.

### Step 2: Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 3: Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Step 4: Configure the database

1. Open SQL Server Management Studio.
2. Connect to your SQL Server instance.
3. Import the CSV datasets into the appropriate database tables, or execute your existing SQL setup scripts.
4. Update the connection settings used by `connect_sql.py`.
5. Verify that Python can connect to the database.

Do not commit database passwords or other credentials to GitHub.

### Step 5: Run the application

If `app.py` is implemented using Streamlit, launch the dashboard with:

```bash
python -m streamlit run app.py
```

Follow the local URL displayed in the terminal to open the dashboard in your browser.

## 🔍 Analysis Workflow

1. **Data ingestion:** Load CSV files or retrieve data from SQL Server.
2. **Data preparation:** Clean and validate the datasets.
3. **Database querying:** Execute SQL queries to retrieve relevant information.
4. **Data analysis:** Calculate customer, order, and delivery metrics.
5. **Visualization:** Present the results through the application.
6. **Business interpretation:** Use the findings to identify trends and potential improvements.

## 💼 Business Value

The analysis can help food delivery businesses better understand their customers, evaluate restaurant and order trends, monitor delivery operations, and make data-informed decisions about customer retention and service quality.

## 🧠 Skills Demonstrated

- SQL querying and relational data analysis
- Python programming
- Pandas-based data manipulation
- Data cleaning and validation
- Exploratory data analysis
- Business KPI analysis
- Database connectivity
- Dashboard development
- Analytical problem-solving

## 🔮 Future Enhancements

- Add advanced visualizations and date filters.
- Build customer retention and cohort analysis.
- Introduce restaurant performance rankings.
- Add delivery time and cancellation analysis.
- Implement automated data quality checks.
- Deploy the dashboard to a cloud platform.

## 👨‍💻 Author

**Siddharth Pathak**

Data Analytics | Python | SQL | Business Intelligence

---

*This project is intended for learning, portfolio development, and demonstrating practical data analytics skills.*

