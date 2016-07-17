
inventory={'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}

def displayInventory():
	item_total=0
	print('Inventory:')
	for k,v in inventory.items():
		#print (k.get(key,0)+' ' +v.get(value,0))
		print(str(k)+' '+str(v))
		item_total=item_total+v
	return item_total
total=displayInventory()
print('Total no of items:'+str(total))
dragonLoot=['gold coin','dagger','gold coin','gold coin','ruby']
def addtoInventory(inventory,addedItems):
	for k in addedItems:	
		if k in inventory:
			inventory[k]=inventory[k]+1
		else:
			inventory[k]=0

inv=addtoInventory(inventory,dragonLoot)
displayInventory()
