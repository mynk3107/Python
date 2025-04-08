note : use the orders and returns dataset 

1- write a program to get category wise sales of orders that were not returned

import pandas as pd

# Assuming you have two datasets: orders and returns

# Load the orders and returns datasets
orders = pd.read_csv('orders.csv')
returns = pd.read_csv('returns.csv')

# Merge the orders and returns datasets based on the order_id
merged_data = pd.merge(orders, returns, on='order_id', how='left')

# Filter out the orders that were not returned
non_returned_orders = merged_data[merged_data['return_reason'].isnull()]

# Calculate the category-wise sales of non-returned orders
category_sales = non_returned_orders.groupby('category')['sales'].sum()


2- write a program to get city wise count of return orders

import pandas as pd

# Assuming you have two datasets: orders and returns

# Load the orders and returns datasets
orders = pd.read_csv('orders.csv')
returns = pd.read_csv('returns.csv')

# Merge the orders and returns datasets based on the order_id
merged_data = pd.merge(orders, returns, on='order_id', how='inner')

# Calculate the city-wise count of return orders
city_return_count = merged_data['city'].value_counts()

# Print the city-wise count of return orders
print(city_return_count)


3- write a program to print cities where we have all 3 kinds of returns (others,bad quality,wrong items)

import pandas as pd


merged_data = pd.merge(orders, returns, on='order_id', how='inner')


city_return_ucounts = merged_data.groupby('city')['return_reason'].nunique()


city_return_ucounts[city_return_ucounts.values > 1]


4- write a program to find cities where not even a single order was returned.


merged_data = pd.merge(orders, returns, on='order_id', how='left')
city_return = merged_data.groupby('city')['return_reason'].count()
city_return[city_return.values==0]

5- write a program to find top 3 cities by sales
orders.groupby('city')['sales'].sum().sort_values(ascending=False).head(3)

6- write a program to get order ids whos return reason is not known (nan)

returns[returns['return_reason'].isna()]


7- write a program to fill unknown return reason to a default value 'others'
returns['return_reason'].fillna('others',inplace=True)


8- write a program to find avg sales and avg profit for each category
orders.groupby('category').agg({'sales':'mean','profit':'mean'})
