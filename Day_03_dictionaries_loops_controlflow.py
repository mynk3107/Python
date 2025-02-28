#1
'''program to find the mean of the numbers in list'''

list1 =[1,2,3,4]
sum_num = sum(list1)
mean = sum_num/len(list1)
print(mean)

#2
'''program to find the mean of the numbers in list'''

numbers = [5, 1, 3, 2, 6,7,8]
# Sort the list in ascending order
numbers.sort()
# calculating median if list has even number of elements
if len(numbers) % 2 == 0:
    median = (numbers[len(numbers)//2] + numbers[len(numbers)//2-1]) / 2
# calculating median if list has even odd of elements
else:
    median = numbers[((len(numbers)-1)//2)]

print(median)

#3
#from a list of numbers creating 2 list , one containing only the even numbers and other only the odd numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#empty lists for even and odd numbers
even_number = []
odd_number =[]
#Iterate through the numbers and classify them as even or odd
for i in numbers:
    if i % 2 == 0:
        even_number.append(i)
    else:
        odd_number.append(i)
# Display the even numbers list
print('Even Numbers :',even_number)
# Display the odd numbers list
print('Odd Numbers :',odd_number)

#4
'''creating a dictionary to store following attributes of CSK 
key "CSK" ; attributes : team full name , captain , playing 11 for each match(name of players), opponent name
 (assume there are 3 matches only against MI, RCB , GT ) and result won/loss'''

csk = {
    'team_name' : 'Chennai Super Kings',
    'captain' : 'MS Dhoni',
    'playing_11' : [
        ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11"],  # Match 1
        ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11"],  # Match 2
        ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11"],  # Match 3
    ],
    'opponents' : ['MI','RCB','GT'],
    'results' : ['Won','Loss','Won']
    }
#5
'''program to take a positive number as input from user. if the user enters negative number then keep promoting him 
to enter positive number until he enters the positive number and then print the same'''

num = int(input('Enter a positive number :'))
#prompting until a positive number is entered
while num <= 0 :
    print(f'{num} is not valid')
    num = int(input('Enter a positive number :'))
print(f'Your num is {num}.')

#6
'''write a program to print following information :
1- a list of all the universities  : ['California Institute of Technology','Harvard',..so on]
2- total number of student enrolled in all the universities together 
3- mean of tuition fees'''

universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

universities_list = []
for university in universities:
    universities_list.append(university[0])

total_students =0
for university in universities:
    total_students += university[1]

fee_sum=0
tuition_fee =[]
for university in universities:
    tuition_fee.append(university[2])
    fee_sum += university[2]

mean_tuition_fee = (fee_sum/len(tuition_fee))

print(f'list of all the universities : {universities_list}')
print(f'total number of student enrolled in all the universities together {total_students}')
print(f'mean of tuition fees is {mean_tuition_fee}')

#7
'''program to convert list to a dictionary. the keys should be the name of the university'''
universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]
# Initialize an empty dictionary to store university data
universities_dict={}
# Iterate through the list and store university data
for university in universities:
    name = university[0] # University name
    attributes ={
        'total_students' : university[1], # Total number of students
        'tuition_fees' : university[2]  # Tuition fees
    }
    # Store the university data in the dictionary
    universities_dict[name] = attributes
print(universities_dict)

#8
'''program that reverses a given string. For example, if the input is "Hello" from user, the output should be 
"olleH" '''

# Prompt the user to enter a string
string = input('Enter a string')
# Initialize an empty string to store the reversed string
reverse_string = ''
# Iterate through each character in the input string
for words in string :
    # Prepend each character to reverse_string to build the reversed string
    reverse_string = words + reverse_string
print(reverse_string)

#9
'''program that finds the largest number in a list(unsorted) of integers without using sort/sorted method'''
# List of numbers
numbers = [9, 4, 7, 2, 1, 5, 8, 3, 6]

# Assume the first number is the largest
largest_num = numbers[0]

# Iterate through the list to find the largest number
for number in numbers:
    if number > largest_num:  # If a larger number is found, update largest_num
        largest_num = number

# Print the largest number in the list
print(f'Largest number in list is {largest_num}')

