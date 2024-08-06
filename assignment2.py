import pandas as pd

items_df = pd.read_csv('items.csv')
sales_df = pd.read_csv('sales.csv')

items_df['StartDate'] = pd.to_datetime(items_df['StartDate'])
items_df['EndDate'] = pd.to_datetime(items_df['EndDate'])
sales_df['SalesDate'] = pd.to_datetime(sales_df['SalesDate'])

merged_df = pd.merge(sales_df, items_df, on='ItemId')

filtered_df = merged_df[
    (merged_df['SalesDate'] >= merged_df['StartDate']) &
    (merged_df['SalesDate'] <= merged_df['EndDate'])
]

filtered_df['Revenue'] = filtered_df['NumSales'] * filtered_df['Price']

revenue_df = filtered_df.groupby('ItemId').agg(
    TotalRevenue=('Revenue', 'sum'),
    TotalUnitsSold=('NumSales', 'sum')
).reset_index()

result_df = revenue_df[['ItemId', 'TotalRevenue']]
result_df.to_csv('total_revenue.csv', index=False)

print("Total revenue calculation completed and saved to 'total_revenue.csv'.")
