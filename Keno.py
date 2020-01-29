import random

def pickCasinoNumbers(table):
	
	Casinos_Numbers = []
	for i in range(1,21):

		number = random.choice(table)
		Casinos_Numbers.append(number)
		
		table.remove(number)
		
	return(Casinos_Numbers)

def userPicksNumbers(table):
	numbers = []
	count = 0

	while count<10:

		x = int(input("Pick a number "))
		if x not in numbers and x in table:
			numbers.append(x)
			count = count + 1
		else:
			print("Invalid number")

	return(numbers)

def autoPickNumbers(table):
	numbers = []
	for i in range(10):
		number = random.choice(table)
		table.remove(number)
		numbers.append(number)
	return(numbers)

def main():
	
	
	table = [i for i in range(1,81)]

	y = input("Would you like to Quick Play? Y/N ")

	MyList = None
	if y == "Y":
		MyList = set(autoPickNumbers(table))
	else:
		MyList = set(userPicksNumbers(table))

	table = [i for i in range(1,81)]
	CasinoList = set(pickCasinoNumbers(table))
		
	print(MyList)
	print(CasinoList)
	
	NumberOfMatches = len(CasinoList.intersection(MyList))
	print("The number of matches is " , NumberOfMatches)

main()



