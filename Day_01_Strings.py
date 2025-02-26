#1
''' program which takes 2 inputs from the user : weight(kg) and height(meter) and prints the BMI in the
output.'''

weight = int(input("Enter Weight (Kg) : "))
height = int(input("Enter height (m) : "))
BMI =  weight/(height ** 2)
print(f"Hey your BMI is {BMI}")

#2
'''program which takes the name of the user as input and replace all the occurence of character 'a' in the name to 'b'
 and print it.'''

name = input("Enter your name : ")
name= name.replace("a","b")
print(name)

#3
'''program which takes 2 inputs from user as principle amount (int) and rate of annual interest (float) and print the
 expected total amount  after  2 years.'''

principle_amount = int(input("Enter the principal amount : "))
annual_interest = float(input("Enter rate of the annual interest"))
total_amount = principle_amount * (1 + (annual_interest / 100)) ** 2
print("Expected total amount  after  2 years is :",total_amount)

#4
'''program which takes city name from user input. irrespective of in which case user enters the city name, 
print the city name in camel case meaning first letter should be capital and rest in small.'''

#sol 1---
city_name = input("Enter the city name: ")
city_name = city_name[0].upper() + city_name[1:].lower()
print(city_name)

#sol 2---
city_name = input("Enter the city name: ")
city_name = city_name.capitalize()
print(city_name)

#5
''' program which takes the name of the user as input and print the index of character 'a' in the string. if 'a' is not
there then return -1.'''

name = input("Enter your name :")
index = name.find('a')
print(index)

#6
'''Display the number of letters in the below string'''

my_word = "antidisestablishmentarianism"
print(len(my_word))

#7
''' 3 inputs from user : first name , last name and age . Display the information in below format
exmaple
first name : Mohit
last name : sharma
age 32 

Display : my name is Mohit Sharma and I am 32 years old.

note that first letter of first name and last name both should be in capital letters and rest in small. 
'''

first_name = input("Enter your first name :")
last_name = input("Enter your last name :")
age = int(input("Enter your Age :"))

full_name = first_name.capitalize() + " " + last_name.capitalize()

print(f"My Name is {full_name} and I am {age} years old")


# 8
'''
take 3 inputs from user : first name , last name and company name. create the email alias for the user and display it.  
Email alias is first 2 letters of first name , last 3 letters of last name and @company.com
example 
first name : Mohit
last name : sharma 
company : infosys

Display : morma@infosys.com 

note full email id should -be in lower case
'''
first_name = input("Enter your first name :")
last_name = input("Enter your last name :")
company = input("Enter your company name :")

email  = first_name[0:2].lower() + last_name[-3:].lower() + "@" + company.lower() + ".com"
print(email)
