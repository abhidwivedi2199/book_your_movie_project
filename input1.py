def take_input():
	while True:
		try:
			a=int(input())
			break
		except ValueError:
			print("Invalid Input , Please provide valid input")

	return a