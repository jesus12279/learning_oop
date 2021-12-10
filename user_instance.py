"""Importing from our previously built file users.py"""
from users import User

print("Enter 'q' at any time to quit. ")
"""Asking for user input and giving them a way to end the program when needed"""
while True:
	first = input("\n Please give me a first name ")
	if first == 'q':
		break
	last = input("Please give me a last name ")
	if last == 'q':
		break
	"""Calling upon the User function and passing the user input"""
	formatted_name = User(first, last)
    print("\nNeatly formatted name: " + formatted_name.greet_user() + "!")