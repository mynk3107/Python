#1
'''
creating a txt file and putting 4-5 lines and creating another file from the previous file and at the end of each line
putting the count of words.
'''
#Creating the first file and write lines into it
with open('file1.txt','w') as file1:
    lines=['The drug lord kept four hippos.',
            'Reasoning and science lay bare legends.','I think at some point something happened to it, maybe?',
            'The floor is covered in sawdust.','Could I get a referral to another endocrinologist?'
    ]
    for line in lines:
        file1.write(line + '\n')

# Creating the second file with word count at the end of each line
with open('file1.txt', 'r') as file1, open('file2.txt','w') as file2:
    for line in file1:
        line = line.strip()
        word_count = len(line.split())
        file2.write(line + str(word_count) + '\n')
print("File creation and word count operation completed!")

#2
'''
given below dictionaries of states and their capital:

capitals_dict = {
'Alabama': 'Montgomery',
'Alaska': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock',
'California': 'Sacramento',
'Colorado': 'Denver',
'Connecticut': 'Hartford',
'Delaware': 'Dover',
'Florida': 'Tallahassee',
'Georgia': 'Atlanta',
}

picking a state from above dictionary and asking user to enter the capital of the state.If the user answers incorrectly, then repeatedly asking them
for the capital until they either enter the correct answer or type "exit".
If the user answers correctly, then display "Correct" and end the program. However, if the user exits without guessing correctly, display
the correct answer and the word "Goodbye".

Note: Make sure the user isn’t punished for case sensitivity. In other words, a guess of "Denver" is the same as 
"denver". Do the same for exiting—"EXIT" and "Exit" should work the same as "exit".
'''

capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta'
}

state = input("Pick a state from the dictionary: ")
state = state.capitalize()  # Convert the input to capitalize for case insensitivity

while True:
    if state in capitals_dict:
        capital = capitals_dict[state]
        guess = input("Enter the capital of {}: ".format(state))
        guess = guess.capitalize()  # Convert the guess to capitalize for case insensitivity

        if guess == capital:
            print("Correct!")
            break
        elif guess.lower() == 'exit':
            print("The correct answer was: {}".format(capital))
            print("Goodbye!")
            break
        else:
            print("Incorrect. Try again or type 'exit' to quit.")
    else:
        print("Invalid state. Please pick a state from the dictionary.")

    state = input("Pick a state from the dictionary: ")
    state = state.capitalize()

#3
'''program to take state as input from user and print the capital of the state using above dictionary. 
If the state is not there in dictionary then print "sorry , information not available"
'''

capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta'
}

state = input("Enter a state: ")
capital = capitals_dict.get(state.capitalize())

#note here using capitals_dict.get function instead of capitals_dict['state']. the advantage of using this method
# it won't throw error if key is not present in the dictionary. it will only return None.

if capital:
    print("The capital of {} is {}.".format(state, capital))
else:
    print("Sorry, information not available.")

