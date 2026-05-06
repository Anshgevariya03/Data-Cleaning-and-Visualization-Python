import pandas as pd
import numpy as np
import random
from datetime import timedelta, date

np.random.seed(42)
random.seed(42)

# Number of rows
n = 1500

# Generate base data
invoice_ids = [f"INV-{str(i).zfill(5)}" for i in range(1, n+1)]
branches = np.random.choice(['A', 'B', 'C'], n, p=[0.3, 0.4, 0.3])
cities = np.where(branches == 'A', 'Yangon', np.where(branches == 'B', 'Mandalay', 'Naypyitaw'))
customer_types = np.random.choice(['Member', 'Normal'], n)
genders = np.random.choice(['Male', 'Female'], n)

product_lines = ['Health and beauty', 'Electronic accessories', 'Home and lifestyle',
                 'Sports and travel', 'Food and beverages', 'Fashion accessories']
product_line = np.random.choice(product_lines, n)

unit_price = np.round(np.random.uniform(10, 100, n), 2)
quantity = np.random.randint(1, 11, n)
tax_5 = np.round(unit_price * quantity * 0.05, 4)
total = unit_price * quantity + tax_5

# Generate random dates
start_date = date(2023, 1, 1)
end_date = date(2023, 12, 31)
date_generated = [start_date + timedelta(days=random.randint(0, (end_date - start_date).days)) for _ in range(n)]

time_generated = [f"{random.randint(10, 20)}:{str(random.randint(0, 59)).zfill(2)}" for _ in range(n)]
payment = np.random.choice(['Ewallet', 'Cash', 'Credit card'], n)
cogs = unit_price * quantity
gross_margin_percentage = [4.7619047619] * n
gross_income = tax_5
rating = np.round(np.random.uniform(4, 10, n), 1)

# Create DataFrame
df = pd.DataFrame({
    'Invoice ID': invoice_ids,
    'Branch': branches,
    'City': cities,
    'Customer type': customer_types,
    'Gender': genders,
    'Product line': product_line,
    'Unit price': unit_price,
    'Quantity': quantity,
    'Tax 5%': tax_5,
    'Total': total,
    'Date': date_generated,
    'Time': time_generated,
    'Payment': payment,
    'cogs': cogs,
    'gross margin percentage': gross_margin_percentage,
    'gross income': gross_income,
    'Rating': rating
})

# ----------------- INTRODUCE DATA ISSUES -----------------

# 1. Missing Values (Randomly make 5-10% missing in specific columns)
df.loc[np.random.choice(df.index, size=150, replace=False), 'Rating'] = np.nan
df.loc[np.random.choice(df.index, size=100, replace=False), 'Gender'] = np.nan
df.loc[np.random.choice(df.index, size=75, replace=False), 'Product line'] = np.nan

# 2. Add Duplicates (Add 50 exact copies of random rows)
duplicates = df.sample(n=50, random_state=1)
df = pd.concat([df, duplicates], ignore_index=True)

# 3. Add Outliers in 'Total' (Very large values)
outlier_indices = np.random.choice(df.index, size=20, replace=False)
df.loc[outlier_indices, 'Total'] = df.loc[outlier_indices, 'Total'] * np.random.uniform(5, 15, 20)
df.loc[outlier_indices, 'Unit price'] = df.loc[outlier_indices, 'Unit price'] * np.random.uniform(5, 10, 20)

# 4. Inconsistent Formatting and Typographical errors
# Gender: M, F, male, female
df['Gender'] = df['Gender'].replace({
    'Male': np.random.choice(['Male', 'M', 'male'], size=len(df), p=[0.8, 0.1, 0.1]),
    'Female': np.random.choice(['Female', 'F', 'female'], size=len(df), p=[0.8, 0.1, 0.1])
})

# City: Leading/trailing spaces, lowercase
df['City'] = df['City'].apply(lambda x: f" {x} " if random.random() < 0.1 else (x.lower() if random.random() < 0.05 else x))

# Date: few as different string format
df['Date'] = df['Date'].astype(str)
idx_date_issue = np.random.choice(df.index, size=30, replace=False)
df.loc[idx_date_issue, 'Date'] = df.loc[idx_date_issue, 'Date'].apply(lambda x: x.replace('-', '/'))

# Incorrect Data Types: Make 'Quantity' float instead of int for some rows, or let pandas infer incorrectly.
# Easiest way in CSV is add a decimal to few integers, so column becomes float. Or add string error
df.loc[np.random.choice(df.index, size=10, replace=False), 'Quantity'] = -1 # Invalid values!

# Shuffle dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save to CSV
df.to_csv("supermarket_sales_dirty.csv", index=False)
print("Dataset 'supermarket_sales_dirty.csv' created successfully with missing values, duplicates, and outliers.")
