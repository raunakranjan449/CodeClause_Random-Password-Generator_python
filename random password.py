## Project On Random Password Generator in Python 

import string
import random

# Typing the password length you want
length = int(input("Enter the length of your password : "))
print('''Choose the character set for password from these :
		1. Letters
		2. Digits
		3. Special characters	
		4. Exit''')
print("")

print('''You can choose these options to include letter, digits, 
special character in your password''')
print("")
character_List = ""
while(True):
	choice = int(input("Choose no. from given choice : "))
	if(choice == 1):
		
		# Adding the letters to possible characters
		character_List = character_List + string.ascii_letters
	elif(choice == 2):
		
		# Adding the digits to possible characters
		character_List = character_List + string.digits
	elif(choice == 3):
		
		# Adding the special characters to possible
		# characters
		character_List = character_List + string.punctuation
	elif(choice == 4):
		break
	else:
		print("Please pick a valid option!")

password = []

for i in range(length):

	# Picking a random character from our
	randomchar = random.choice(character_List)
	password.append(randomchar)

# printing password as a string
print("The random password is " + "".join(password))

### Thank You CodeClause ####