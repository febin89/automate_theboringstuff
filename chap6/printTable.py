tableData=[['apples','oranges','cherries','banana'],
		['Alice','Bob','Carol','David'],
		['dogs','cats','moose','goose']]
def printTable():
	x=0
	colWidths=[0]*len(tableData)
	for i, k in enumerate(tableData):
		for w in tableData[i]:
			if len(w)>x:
				x=len(w)
		colWidths[i]=x
	for j in range(len(tableData)-2):
		for b in range(len(tableData[0])):
		#for j in range(len(tableData)):
			print(tableData[j][b].rjust(colWidths[j])+tableData[j+1][b].rjust(colWidths[j])+tableData[j+2][b].rjust(colWidths[j]))
printTable()	
	
