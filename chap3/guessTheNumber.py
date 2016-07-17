import random
Num=random.randint(1,20)
print('I am thinking of  a numbetween 1 and 20')

#Ask the player to guess 6 times.
for guesses in range(1,7):
	print('Take a guess')
	guess=int(input())
	if guess<Num:
		print('Your guess is too low')
	elif guess>Num:
		print('Your guess is too high')
	else:
		break
if guess==Num:
	print('Good job!You guessed my number in '+str(guesses)+' guesses')
else:
	print('Nope.The number I was thinking of was '+str(Num))
