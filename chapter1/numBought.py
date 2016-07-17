all={'Alice':{'apples':5,'nuts':13},
	'Bob':{'ham':3,'apples':2},
	'Carol':{'cups':3,'pies':1}}
def bought(guests,item):
	numBought=0
	for k,v in guests.items():
		numBought=numBought+ v.get(item,0)
	return numBought

print('Number of things bought:')
print(' -Apples    '+str(bought(all,'apples')))
print(' -Cups      '+str(bought(all,'cups')))
print(' -Nuts      '+str(bought(all,'nuts')))
print(' -Pies      '+str(bought(all,'pies')))
