class stats:
	def price_of_seat(rows,cols,row,col):
		if rows*cols <=60:
			price=10
		else:
			if rows%2==0 and row <= rows/2:
				price=10
			elif rows%2==0 and row >= rows/2:
				price=8
			elif row%2!=0:
				r=rows-1
				if row <= r/2:
					price=10
				else:
					price=8
		return price

	def statistics(rows,cols,income,booked):
		print("Number of purchased tickets are : ",booked)
		per=(booked/(rows*cols)*100)
		print("Percentage : %.2f"%per,"%")
		total_income=0
		if rows*cols <=60:
			total_income=rows*cols*10
		else:
			if rows%2==0:
				total_income=rows*cols*9
			else:
				total_income=((rows-1/2))*cols*10
				total_income=total_income+((rows+1/2))*cols*8
		print("Current Income : $",income)
		print("Total Income : $",total_income)

