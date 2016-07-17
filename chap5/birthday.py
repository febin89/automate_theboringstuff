birthdays={'Fred':'Apr1','George':'May2','Alex':'May2','Titus':'June3'}
while True:
	print('Enter a name:')
	name=input()
	if name in birthdays:
		print(birthdays[name]+ ' is the birthday of '+name)
	
	else:
		print('I donot have the information for '+name)
		print('When is their birthday?')
		bday=input()
		birthdays[name]=bday
		print('Birthday database updated')
