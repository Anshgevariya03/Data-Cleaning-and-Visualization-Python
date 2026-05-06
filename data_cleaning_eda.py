"""
Data Cleaning & Visualization using Python (Standalone Script)

This script contains the identical code logic found in `notebook.ipynb`. 
It performs end-to-end data cleaning and visualization.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")
sns.set_theme(style="darkgrid")
plt.rcParams['figure.figsize'] = (10, 6)

def main():
    print("====== 1. Load Dataset ======")
    try:
        df = pd.read_csv('supermarket_sales_dirty.csv')
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return
        
    print(df.head())
    print(f"\\nShape: {df.shape}")
    print(f"Missing Values Before Cleaning:\\n{df.isnull().sum()[df.isnull().sum() > 0]}")

    print("\\n====== 2. Data Cleaning ======")
    # 1. Invalid Data Types
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
    df['Quantity'] = df['Quantity'].apply(lambda x: x if x > 0 else np.nan)

    # 2. String Standardization
    df['Gender'] = df['Gender'].str.strip().str.capitalize().replace({'M': 'Male', 'F': 'Female'})
    df['City'] = df['City'].str.strip().str.title()

    # 3. Missing Values
    df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
    df['Product line'].fillna(df['Product line'].mode()[0], inplace=True)
    df['Rating'].fillna(df['Rating'].median(), inplace=True)
    df['Quantity'].fillna(df['Quantity'].median(), inplace=True)
    df['Quantity'] = df['Quantity'].astype(int)

    # 4. Remove Duplicates
    print(f"Duplicates before removal: {df.duplicated().sum()}")
    df.drop_duplicates(inplace=True)

    # 5. Column Renaming
    df['Date'] = df['Date'].astype(str).str.replace('-', '/')
    df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d')
    df.rename(columns={
        'Invoice ID': 'invoice_id', 'Customer type': 'customer_type',
        'Product line': 'product_line', 'Unit price': 'unit_price',
        'Tax 5%': 'tax_5_percent', 'gross margin percentage': 'gross_margin_pct'
    }, inplace=True)

    print("\\n====== 3. Outlier Handling ======")
    Q1, Q3 = df['Total'].quantile(0.25), df['Total'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound, upper_bound = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR

    outlier_count = df[(df['Total'] < lower_bound) | (df['Total'] > upper_bound)].shape[0]
    print(f"Capping {outlier_count} Outliers in Total.")
    df['Total'] = np.where(df['Total'] > upper_bound, upper_bound, df['Total'])
    df['Total'] = np.where(df['Total'] < lower_bound, lower_bound, df['Total'])

    print("\\n====== 4. Feature Engineering ======")
    df['Month'] = df['Date'].dt.month
    df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M').dt.hour

    print("\\n====== 5. Dashboard KPI ======")
    print(f"Total Revenue:              ${df['Total'].sum():,.2f}")
    print(f"Average Customer Rating:    {df['Rating'].mean():.2f} / 10")
    print(f"Total Number of Sales:      {df.shape[0]}")
    print(f"Highest Performing Branch:  {df.groupby('Branch')['Total'].sum().idxmax()}")

if __name__ == '__main__':
    main()
