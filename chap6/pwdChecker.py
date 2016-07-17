import sys,re
txt=sys.argv[1]

regex=re.compile(r'[a-z]+')
regex3=re.compile(r'[A-Z]+')
regex4=re.compile(r'[0-9]+')
regex2=re.compile(r'........*')
if regex2.search(txt)!=None:
	if regex.search(txt)!=None and regex3.search(txt)!=None and regex4.search(txt)!=None:
		print('Password is strong!')
	else:
		print('Include lowercase,uppercase letters and atleast one digit')
else:
	print('Password should be of atleast 8 characters.')
