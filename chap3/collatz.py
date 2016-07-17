def collatz(number):
	if (number %2)==0:
		print(number//2)
		return number//2

	else:
		res=3*number+1
		print(res)
		return res
try:
	print('Enter an integer')
	num=input()
except ValueError:
	print('Please type an integer')
while (num !=1):
	num=collatz(int(num))

	

