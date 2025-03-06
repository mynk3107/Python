#use orders.txt dataset for below problems

#1
'''Program to fetch all the orders with indexes  multiple of 100 eg : 100,200,300,400..... . Display order_id , category and sales columns'''

import pandas as pd

orders = pd.read_csv('orders.txt')
# Fetch orders with indexes that are multiples of 100
orders = orders[orders.index % 100 == 0]
# Display 'order_id', 'category', and 'sales' columns
orders = orders[['order_id','category','sales']]
print(orders)


#2
'''program to find all orders in furniture category with sales amount between 1000 and 1200'''

import pandas as pd
# Read the 'orders.txt' file into a DataFrame
orders = pd.read_csv('orders.txt')
# Filter orders in the furniture category with sales between 1000 and 1200
fc = (orders['category'] == 'Furniture') & (orders['sales'] >= 1000) & (orders['sales'] <= 1200)
print(orders[fc]) 


#3
'''program to find all the orders where there was a loss (profit<0) in the city of new york , Los Angeles and Seattle'''

import pandas as pd
orders = pd.read_csv('orders.txt')
# Filter orders with a loss (profit < 0) in the cities of New York, Los Angeles, and Seattle
fc = (orders['profit'] < 0) & (orders['city'].isin(['New York City','Seattle','Los Angeles']))
print(orders[fc])


#4 
'''program to find unique list of cities where orders are placed for Office Supplies category.'''

import pandas as pd

orders = pd.read_csv('orders.txt')
# Filter orders in the Office Supplies category
fc = (orders['category'] == 'Office Supplies')

office_supplies = orders[fc]
unique = office_supplies['city'].unique()


#5
'''program to find new york city how many orders were placed in each of the category '''

import pandas as pd

orders = pd.read_csv('orders.txt')
# Filter orders placed in New York City
new_york_city_orders = orders[orders['city'] == 'New York City']
# Count the number of orders in each category
category_counts = new_york_city_orders['category'].value_counts()
print(category_counts)


#6
'''set the index of orders dataframe to order_id and fetch order details(all columns) of following list of orders : 
CA-2019-115742
CA-2020-111682
CA-2019-149587
US-2020-150147
CA-2020-138520'''

import pandas as pd

orders = pd.read_csv('orders.txt')
# Set the index of the DataFrame to 'order_id'
orders.set_index('order_id', inplace =True)
# List of orders to fetch details for
order_list = ['CA-2020-111682','CA-2020-111682','US-2020-150147','CA-2020-138520']
order_details = orders.loc[order_list]
print(order_details)


#7
'''
for the previous question display columns order id, order date , sales and category columns in the given order
'''

import pandas as pd

orders = pd.read_csv('orders.txt')

# Set the index of the DataFrame to 'order_id'
orders.set_index('order_id', inplace =True)
# List of orders to fetch details for
order_list = ['CA-2020-111682','CA-2020-111682','US-2020-150147','CA-2020-138520']
order_details = orders.loc[order_list,['order_date', 'sales', 'category']]
print(order_details)


#8
'''
for the previous(6th) question display all the columns from order_date to city (as per the order in dataset)
'''

import pandas as pd

orders = pd.read_csv('orders.txt')

# Set the index of the DataFrame to 'order_id'
orders.set_index('order_id', inplace =True)
# List of orders to fetch details for
order_list = ['CA-2020-111682','CA-2020-111682','US-2020-150147','CA-2020-138520']
order_details = orders.loc[order_list,'order_date': 'city']
print(order_details)


#9
'''
sort the index (order id) in descending order for the dataframe 
'''

import pandas as pd

orders = pd.read_csv('orders.txt')

# Set the index of the DataFrame to 'order_id'
orders.set_index('order_id',inplace = True)
# Sort the index in descending order
sorted_order = orders.sort_index(ascending = False)
print(sorted_order)


#10
'''
write the result of previous question into a csv file in your local machine
'''
sorted_order.to_csv('sort_order.csv')
