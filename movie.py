from stats import stats
class movie:
    global user_details_list
    user_details_list=[]

    def __init__(self,ro,co):
        global rows
        rows=ro
        global cols
        cols=co
        global arr
        arr = [["S"]*co for _ in range(ro)]
        
    def show_seat(self):
        print(" ",end="")
        for i in range(cols):
                print(" ",i+1,end="")
        print("")
        for i in range(rows):
            print(i+1,"",end="")
            for j in range(cols):
                print(" ",arr[i][j],end="")
            print("")
        

    
    def user_details(self,row,col):
        l=[]
        l.append(row)
        l.append(col)
        l.append(input("Enter your name : "))
        l.append(input("Enter your Gender : "))
        l.append(input("Enter your Age: "))
        l.append(input("Enter your Phone Number : "))
        user_details_list.append(l)
        return None


    def buy_ticket(self,row,col):

        if row<=rows and col<=cols:
        	if arr[row-1][col-1]=="B":
        		print("The seat is already booked!")
        		return 0
        	else:
        		price=stats.price_of_seat(rows,cols,row,col)
        		print("The price of the seat is : $",price," to confirm, Press Y otherwise, Press N : ")
        		con=input()
        		if con=="Y":
        			self.user_details(row,col)
        			arr[row-1][col-1]="B"
        			print('\033[1m' +"Booked Successfully!!")
        			return price
        		else:
        			return 0
        else:
            print("Invalid seat number")
            return 0
        
    def show_booked_user_info(self,row,col):
        if arr[row-1][col-1]=="B":
            self.print_details_of_user(row,col)
        else:
            print("This seat is not booked yet.")

    def print_details_of_user(self,row,col):
        for i in range(0,len(user_details_list)):
                if user_details_list[i][0]==row and user_details_list[i][1]==col:
                    print("Name : ",user_details_list[i][2])
                    print("Gender : ",user_details_list[i][3])
                    print("Age : ",user_details_list[i][4])
                    print("Phone No. : ",user_details_list[i][5])
    
