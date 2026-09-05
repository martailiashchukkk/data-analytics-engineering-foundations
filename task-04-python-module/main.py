import pandas as pd

df = pd.read_csv("sneaker_sales_dataset.csv")

#1
print(f"Shape: {df.shape}")
print(df.info())

#2
print(f"Missing values:\n{df.isnull().sum()}")
print(f"Total duplicates: {df.duplicated().sum()}")
print(f"Transaction ID duplicates: {df['transaction_id'].duplicated().sum()}")
print(df.describe())

#3
entity = 'brand'
unique_count = df[entity].nunique()
counts = df[entity].value_counts()
print(f"Unique Brands Count: {unique_count}")
print(f"Number of Transactions per Brand:\n{counts}")

#4
df['transaction_date'] = pd.to_datetime(df['transaction_date'])

total_revenue = df.groupby('brand')['final_price'].sum().sort_values(ascending=False)
print("Total revenue connected with each brand:")
print(total_revenue)

top_3 = total_revenue.head(3)
print(f"\nTOP 3 Brands by Revenue:\n{top_3}")

df['month'] = df['transaction_date'].dt.to_period('M').astype(str)
monthly_dynamics = df.groupby(['month', 'brand'])['final_price'].sum().unstack().fillna(0)
print("\nMonthly dynamics (First 5 months summary):")
print(monthly_dynamics.head())
