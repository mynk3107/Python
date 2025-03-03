#1
'''
a python function that accepts a string and prints the count of occurrence of each characters
sample string: aabccda
expected result:
a -> 3
b-> 1
c-> 2
d -> 1
'''

def occurrence_count(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char, count in char_count.items():
        print(f'{char} -> {count}')

string = input('Enter a string : ')
occurrence_count(string)


#2
'''
function called is_prime that takes an integer as an argument and returns True if it is a prime number, and 
False otherwise.
'''

def is_prime(number):
    if number <= 1:
        return False
    else:
        for i in range (2, int(number**0.5)+1):
            if number % i == 0:
                return False
        return True


num = int(input('Enter the number: '))
if is_prime(num):
    print("Prime")
else:
    print("not prime")


#3
'''
a function called generate_fibonacci that takes an integer n as input and returns a list of the first n 
Fibonacci numbers.
'''
def generate_fibonacci(n):
    fibonacci_sequence=[]
    if n >=1:
        fibonacci_sequence.append(0)
    if n>=2:
        fibonacci_sequence.append(1)
    for i in range(2,n):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
    return fibonacci_sequence

n = int(input('Enter the number : '))
print(generate_fibonacci(n))

#4
'''
A function called capitalize_odd_letters that takes a string as input and returns the same string with the odd-indexed 
letters capitalized.
'''

def capitalize_odd_letters(string):
    capital_string = ''
    for i in range (len(string)):
        if i % 2 == 0:
            capital_string += string[i]
        else:
            capital_string +=string[i].upper()
    return capital_string
string = input('Enter a string : ')
print(capitalize_odd_letters(string))


#5
'''
A function called find_common_elements that takes two lists as input and returns a new list containing the common 
elements between the two lists.
'''
def find_common_elements(list1,list2):
    common_element = []
    for item in list1:
        if item in list2:
            common_element.append(item)

    return common_element

input_list1 = [1, 2, 3, 4, 5]
input_list2 = [4, 5, 6, 7, 8]

print(find_common_elements(input_list1,input_list2))
