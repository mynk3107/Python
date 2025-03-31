#!/usr/bin/env python
# coding: utf-8

#pandas basics operations

# Import necessary libraries
import pandas as pd

# Create a dictionary with employee data
emp = {"name": ["Ankit", "Rahul", "Priya"],
       "gender": ["Male", "Male", "Female"],
       "email": ["ankit@gmail.com", "rahul@gmail.com", "priya@gmail.com"]}

# Convert dictionary to DataFrame
df = pd.DataFrame(emp)
print(df)

# Filtering data using loc
fc = (df['name'] == 'Ankit')
print(df.loc[fc, ['gender']])

# Reset index
df.index = [0, 1, 2]
print(df)

# Modify column names
df.columns = ['emp', 'gender', 'emp_email']
print(df)

# Rename specific columns
df.rename(columns={'emp_name': 'name', 'emp_email': 'email'}, inplace=True)
print(df)

# Modify specific row values
df.loc[0] = ['Ankitt', 'Male', 'ankitt@gmail.com']
df.loc[0, ['name', 'email']] = ['Ankit', 'ankit@gmail.com']
print(df)

# Update values based on condition
fc = (df['gender'] == 'Male')
df.loc[fc, 'gender'] = 'Female'
print(df)

df.loc[fc, 'gender'] = 'Male'
print(df)

# Apply function to column
def update_email(inputval):
    return inputval.upper()

df['email'] = df['email'].apply(update_email)
print(df)

# Using string operations
df['name'] = df['name'].str.startswith('A')
print(df)

# Display dataframe info
df.info()
print(df)

# Add new columns
df['salary'] = 10000
df['name_gender'] = df['name'] + ' ' + df['gender']
df['salary'] = 20000
df.loc[(df['name'] == 'Ankit'), 'salary'] = 5000
print(df)

df['salary1'] = [5000, 6000, 7000]
print(df)

# Delete rows
df.drop(index=0, inplace=False)
fc = (df['salary'] >= 6000)
df.drop(index=df[fc].index, inplace=False)
print(df)

# Delete a column
df.drop(columns='salary1', inplace=False)
print(df)

# Sorting values
df.sort_values(by='name', inplace=True)
df.sort_values(by='salary', ascending=False, inplace=False)
df.sort_values(by=['gender', 'salary'], ascending=[False, True], inplace=True)
df.sort_index(ascending=False, inplace=False)
print(df)
