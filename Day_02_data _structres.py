#1
''' write a program which takes single input from user contaning first name,last name and age as comma separated value
and display then in 3 lines in given format below.

example user input : Ankit,Bansal,35

output:
First name is Ankit
last name is Bansal
Ankit is 35 years old

note : do not hardcode name at any place'''

user_input = input("Enter first name, last name and age (comma-seprated) : ")

first_name, last_name, age = user_input.split(",")
print(f'First name is {first_name}')
print(f'Last name is {last_name}')
print(f'{first_name} is {age} years old.')

#2
'''given 2 list as list1= [1,3,4] and list2 = [2,4,6]
combined the 2 list and diplay the same without using extend method.'''
list1 = [1, 3, 4]
list2 = [2,4,6]
final_list = list1 + list2
print(final_list)

#3
''' given a list list1=[1,2,3,4,5,6,7,8]
diplay a new list which contains only odd position index values from above list.'''

#sol1 using slicing
list1=[1,2,3,4,5,6,7,8]

list1 = list1[1::2]
print(list1)

#sol2 using loop
list1=[1,2,3,4,5,6,7,8]

list= []
for i in range(len(list1)):
 if i % 2 != 0 :
  list.append(list1[i])
print(list)

#4
'''ipl= ['CSK','MI','KKR','LSG','PBKS']
take a ipl team name as input from user and display a list of all elements from that name.'''

ipl= ['CSK','MI','KKR','LSG','PBKS']
team_name = input("Enter team name from  CSk, MI, KKR, LSG, PBKS :")
x = ipl.index(team_name)
ipl= ipl[x:]
print(ipl)

#5
'''ipl= ['CSK','MI','KKR','LSG','PBKS']

take a ipl team name as input from user and display a list of all elements except input one

example : input : KKR
output : ['CSK','MI','LSG','PBKS']'''

#sol1 using remove method--
ipl= ['CSK','MI','KKR','LSG','PBKS']
team_name = input("Enter team name from  CSK, MI, KKR, LSG, PBKS :")
ipl.remove(team_name)
print(ipl)

#sol2 using pop method--
ipl= ['CSK','MI','KKR','LSG','PBKS']
team_name = input("Enter team name from  CSK, MI, KKR, LSG, PBKS :")
new_list = ipl.copy()
new_list.pop(ipl.index(team_name))
print(new_list)

#6
'''ipl= ['CSK','MI','KKR','LSG','PBKS']
take a user input contains 2 comma seprated values index,new_team . replace the index element of list with new value 
and display the same

example : input : 2,SRH
output : ['CSK','MI','SRH','LSG','PBKS']'''

ipl= ['CSK','MI','KKR','LSG','PBKS']
user_input = input("Enter the index and new team (comma-separated):")
index,team = user_input.split(",")
index =int(index)
ipl[index] = team
print(ipl)

#7
'''ipl= ['CSK','MI','KKR','LSG','PBKS']
take ipl team name as user input. display True if the team exists in ipl list else display False.'''

ipl= ['CSK','MI','KKR','LSG','PBKS']
user_input = input("Enter ipl team name:")
team_exists = user_input in ipl
print(team_exists)

#8
'''ipl= ['CSK','MI','KKR','LSG','PBKS']
take a user input contains 2 comma seprated values index,new_team . Add the new value at that index in the list. 
Display the old list , new list,length of original and new list

example : input : 2,SRH
output : 
old list : ['CSK','MI','KKR','LSG','PBKS'] and length 5
new list : ['CSK','MI','SRH','KKR',LSG','PBKS'] and length 6'''

ipl= ['CSK','MI','KKR','LSG','PBKS']
user_input = input("Enter the index and new team (comma-separated):")
index,team = user_input.split(",")
index = int(index)
old_len = len(ipl)

#old list
print(f'old list : {ipl} and length {old_len}')

#new list
ipl.insert(index,team)
new_len = len(ipl)
print(f'old list : {ipl} and length {new_len}')

