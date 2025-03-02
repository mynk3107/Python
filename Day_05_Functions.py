#1
'''
function which takes a positive number as input and return the factorial of the number.
from Day_03_dictionaries_loops_controlflow import reverse_string
'''
def factorial(n):
    # Check if the input is negative
    if n < 0:
        return "Error: input must be a positive number."  # Return error message for negative input
    # If the number is 0 or 1, the factorial is 1
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1  # Initialize result to 1
        # Loop from 2 to the number n, multiplying to calculate the factorial
        for i in range(2, n + 1):
            result *= i  # Multiply the result by the current value of i
        return result  # Return the final factorial result


number = int(input("Enter a positive number: "))
factorial_result = factorial(number)
print('The factorial of {} is {}'.format(number, factorial_result))


#2
'''
Python function that accepts a string and counts the number of upper and lower case letters. 
'''
def count_upper_lower(string):
    count_upper = 0
    count_lower = 0

    for char in string :
        if char.isupper():
            count_upper +=1
        elif char.islower():
            count_lower +=1
    return count_upper,count_lower

string = input('Enter the statement: ')
upper,lower = count_upper_lower(string)
print("No. of Upper case characters:", upper)
print("No. of Lower case characters:", lower)


#3
'''
Python function that takes a list and returns a new list with distinct elements from the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
'''
def get_unique_list(list):

    unique_list =[]
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


list = [1,2,3,3,3,3,4,5]
final_list = get_unique_list(list)
print(final_list)
 

#4
'''
Python function that checks whether a passed string is a palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam.
'''
def is_palindrome(string):
    reverse_string = string[::-1]

    return reverse_string == string

string = input('Enter the string: ')
if is_palindrome(string):
    print('Entered string is palindrome')
else:
    print('Entered string is not palindrome')

#5
'''
Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated 
sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow
'''
#soln1
def sorting_alphabetically(sequence):
    words = sequence.split('-')  #Split the sequence into individual words
    words.sort() #Split the sequence into individual words
    result = ''
    for word in words:
        result += word + '-'
    return result.rstrip('-') #Remove the trailing hyphen

sequence = 'green-red-yellow-black-white'
result = sorting_alphabetically(sequence)
print(result)

#soln 2
def sorting_alphabetically(sequence):
    words = sequence.split('-')
    words.sort()
    words = '-'.join(words)
    return words

result = sorting_alphabetically(sequence)
print(result)
