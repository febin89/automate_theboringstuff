import re,os
mo=[]

#regex=re.compile(r'\w*.txt',re.VERBOSE)i
for filename in os.listdir():
	if filename.endswith('.txt'):
		mo.append(filename)

print(mo)
