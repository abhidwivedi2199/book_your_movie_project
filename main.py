from movie import movie
from stats import stats
import input1

print("Enter the number of rows : ",end="")
n=input1.take_input()

print("Enter the number of columns : ",end="")
m=input1.take_input()

theatre=movie(n,m)

i=1
income=0
booked=0

while i!=0:
	
	print("**********************************")
	print("1. Show the seats")
	print("2. Buy a ticket")
	print("3. Statistics")
	print("4. Show booked Tickets user info")
	print("0. Exit")
	print("**********************************")

	i=input1.take_input()


	if i==1:
		theatre.show_seat()

	elif i==2:
		print("Enter the row number of seat you want to book : ",end="")
		row=input1.take_input()
		print("Enter the column number of seat you want to book : ",end="")
		col=input1.take_input()
		price=theatre.buy_ticket(row,col)
		if price==0:
			pass
		else:
			income=income+price
			booked=booked+1

	elif i==3:

		stats.statistics(n,m,income,booked)

	elif i==4:
		print("Enter the row number : ",end="")
		row=input1.take_input()
		print("Enter the column number : ",end="")
		col=input1.take_input()
		theatre.show_booked_user_info(row,col)

	elif i>4 or i<0 :
		print("Wrong choice , please provide input from the above choices")


