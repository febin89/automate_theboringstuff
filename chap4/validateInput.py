while True:
	print('Enter your age:')
	age=input()
	if age.isdecimal():
		break
	print('Please enter a number for your age')
while True:
	print('Select a new password(letters and digits)')
	password=input()
	if password.isalnum():
		break
	print('Passwords can have only letters and digits')
