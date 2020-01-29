import random

def pickCasinoNumbers(table):
	
	Casinos_Numbers = []
	for i in range(1,21):

		number = random.choice(table)
		Casinos_Numbers.append(number)
		table.remove(number)
		
	return(Casinos_Numbers)

def createNonUniformTable():
	Table = [i for i in range(1,81)]
	Table.insert(5,50)
	Table.insert(60,50)
	return(Table)

def main():
	Count50s = 0

	delta = 0.5
	i = 0
	x = float(3)/float(82)

	while delta > 0.000001:
		#print(delta)
		i = i + 1
		List = pickCasinoNumbers(createNonUniformTable())
		#print(List)
		for item in List:
			if item == 50:
				Count50s = Count50s + 1

		preportionOf50s = float(Count50s)/float(20*i)
		#print(preportionOf50s)
		delta = abs(preportionOf50s - x)

	#i is the number of times we had to run the keno machine for the liklihood of picking the number 50 to be within 0.000001 of 3/8
	print(i)
	print(Count50s)
	print(preportionOf50s)

main()
