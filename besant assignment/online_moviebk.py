import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Middleclass21*",
    database="online_moviebk"

)
mycursor=mydb.cursor()

print("-----------Online Movies Ticket Booking------------\n")
print("----------------Sandy Cineplex-----------------\n")
print("1.Registration the ticket")
print("2.View the register tickets")
print("3.Update the ticket ")
print("4.Delete the ticket\n")
print("choose the choice 1 to 4\n")

def register_ticket(SIno,name,date,movie,timing,seat_no,tickets,total_cost):
    
    sql="insert into cineplex_bk(SIno,name,date,movie,timing,seat_no,tickets,total_cost) value (%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(SIno,name,date,movie,timing,seat_no,tickets,total_cost)

    mycursor.execute(sql,val)
    mydb.commit()
    print(f"\n {movie} \n {timing} successfully register")


def view_registration():
    mycursor.execute("select * from cineplex_bk")
    result=mycursor.fetchall()
    for i in result:
        print(i)

def update(SIno,name,date,movie,timing,seat_no,tickets,total_cost):
    if choose==1:
        mycursor=mydb.cursor()
        sql="UPDATE cineplex_bk set name=%s where SIno=%s"
        val=(name,SIno)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Update successfully")

    elif choose==2:
        mycursor=mydb.cursor()
        sql="UPDATE cineplex_noset date=%s where SIno=%s"
        val=(date,SIno)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Update successfully")

    elif choose==3:
        mycursor=mydb.cursor()
        sql="UPDATE cineplex_bk set movie=%s where SIno=%s"
        val=(movie,SIno)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Update successfully")

    elif choose==4:
        mycursor=mydb.cursor()
        sql="UPDATE cineplex_bk set timing=%s where SIno=%s"
        val=(timing,SIno)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Update successfully")

    elif choose==5:
        mycursor=mydb.cursor()
        sql="UPDATE cineplex_bk set seat_no=%s where SIno=%s"
        val=(seat_no,SIno)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Update successfully")

    elif choose==6:
        mycursor=mydb.cursor()
        sql="UPDATE cineplex_bk set tickets=%s where SIno=%s"
        val=(tickets,SIno)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Update successfully")
    
    elif choose==7:
        mycursor=mydb.cursor()
        sql="UPDATE cineplex_bk total_cost=%s where SIno=%s"
        val=(tickets,SIno)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Update successfully")

    else:
        print("Invalid data....!!!")

def delete_data(SIno):
    mycursor=mydb.cursor()
    sql="delete from cineplex_bk  where SIno=%s"
    val=(SIno)
    mycursor.execute(sql,val)
    mydb.commit()
    print("successfully Deleted")

option = int(input("Enter Your Number : "))

if option==1:

    sino=input("\nEnter the register number: ")
    name=input("Enter the name:").lower().strip()
    date=input("Date:")
    movie=input("Movie:")
    timing=input("Timing:")
    seat_no=input("Seat_no:")
    tickets=int(input("Tickets:"))

    per_ticket=200

    if tickets>=0:

        total_cost=per_ticket*tickets
        print(f"Total_cost:{total_cost}")

        register_ticket(sino,name,date,movie,timing,seat_no,tickets,total_cost)



elif option==2:
    view_registration()

elif option==3:
    print("1.Update name")
    print("2.Update date")
    print("3.Update movie")
    print("4.Update timing")
    print("5.Update seat_no")
    print("6.Update tickets")
    print("7.Update total_cost")

    choose=int(input("\n which data you have to update:"))

    SIno=int(input("Enter the SI:"))

    if choose==1:
        name=input("Enter the name:")
        update(name,SIno)
        print(f"{name} successfully updated")

    elif choose==2:
        date=input("Enter the date:")
        update(date,SIno)
        print("Moblie number updated successfully")

    elif choose==3:
        movie=input("Enter the movie:")
        update=(movie,SIno)
        print("Movie updated successfully")

    elif choose==4:
        timing=input("Enter the timing:")
        update=(timing,SIno)
        print("timing updated successfully")

    elif choose==5:
        seat_no=input("Enter the seat:")
        update=(seat_no,SIno)
        print("Seat_number updated successfully")

    elif choose==6:
        tickets=input("Enter the tickets:")
        update=(tickets,SIno)
        print("Tickets_count updated successfully")

    
    else:
        print("Invalid choice....!!!")

elif option==4:
    SIno=input("Enter your deleted SIno:")
    delete_data(SIno)

else:
    print("Invalid option.....!!!!")




    










    