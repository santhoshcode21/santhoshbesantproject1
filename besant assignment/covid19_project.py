import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Middleclass21*",
    database="covid19_project"
)

print("-----------Covid19 Data Management System------------\n")
print("1.Insert data")
print("2.View data")
print("3.Updata data")
print("4.Delete data\n")
print("choose the choice 1 to 4\n")

mycursor=mydb.cursor()

def insert_data(SI,State,Total_cases,Active_cases,Recovery_cases,Death_cases,Vaccinatted_people):
    
    sql="insert into corona_casesdet(SI,State,Total_cases,Active_cases,Recovery_cases,Death_cases,Vaccinatted_people) value (%s,%s,%s,%s,%s,%s,%s)"
    val=(SI,State,Total_cases,Active_cases,Recovery_cases,Death_cases,Vaccinatted_people)

    mycursor.execute(sql,val)
    mydb.commit()
    print(f"\n{State} cases successfully inserted")

def view_data():
    mycursor.execute("select * from corona_casesdet")
    result=mycursor.fetchall()
    for i in result:
        print(i)

def update(state,SI):
    if choose==1:
        mycursor=mydb.cursor()
        sql="UPDATE corona_casesdet set state=%s where SI=%s"
        val=(state,SI)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Update successfully")

    elif choose==2:
        mycursor=mydb.cursor()
        sql="UPDATE corona_casesdet set Total_cases=%s where SI=%s"
        val=(Total_cases,SI)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Update successfully")

    elif choose==3:
        mycursor=mydb.cursor()
        sql="UPDATE corona_casesdet set Active_cases=%s where SI=%s"
        val=(Active_cases,SI)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Update successfully")

    elif choose==4:
        mycursor=mydb.cursor()
        sql="UPDATE corona_casesdet set Recovery_cases=%s where SI=%s"
        val=(Recovery_cases,SI)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Update successfully")

    elif choose==5:
        mycursor=mydb.cursor()
        sql="UPDATE corona_casesdet set Death_cases=%s where SI=%s"
        val=(Death_cases,SI)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Update successfully")

    elif choose==6:
        mycursor=mydb.cursor()
        sql="UPDATE corona_casesdet set Vaccinatted_people=%s where SI=%s"
        val=(Vaccinatted_people,SI)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Update successfully")

    else:
        print("Invalid data....!!!")

def delete_data(SI):
    mycursor=mydb.cursor()
    sql="delete from corona_casesdet where SI=%s"
    val=(SI)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Data successfully Deleted")

option=int(input("Enter the Number:"))

if option==1:
    SI=input("\nEnter the SI.no:")
    State=input("Enter the state:").lower().strip()
    Total_cases=input(f"{State} total cases:")
    Active_cases=input(f"{State} active cases:")
    Recovery_cases=input(f"{State} recovery cases:")
    Death_cases=input(f"{State} death cases:")
    Vaccinatted_people=input(f"{State} vaccinated people:")
    insert_data(SI,State,Total_cases,Active_cases,Recovery_cases,Death_cases,Vaccinatted_people)

elif option==2:
    view_data()

elif option==3:
    print("1.Update State name")
    print("2.Update Total cases")
    print("3.Update Active cases")
    print("4.Update recovery cases")
    print("5.Update Death cases")
    print("6.Update Vaccinnated people")
    choose=int(input("\n which data you have to update:"))
    SI=int(input("Enter the SI:"))

    if choose==1:
        State=input("Enter the State:")
        update(State,SI)
        print(f"{State} successfully updated")

    elif choose==2:
        Total_cases=input("Enter the Total_cases:")
        update(Total_cases,SI)
        print("Total_cases updated successfully")

    elif choose==3:
        Active_cases=input("Enter the Active_cases:")
        update=(Active_cases,SI)
        print("Active_cases updated successfully")

    elif choose==4:
        Recovery_cases=input("Enter the Recovery_cases:")
        update=(Recovery_cases,SI)
        print("Recovery_cases updated successfully")

    elif choose==5:
        Death_cases=input("Enter the Death_cases:")
        update=(Death_cases,SI)
        print("Death_cases updated successfully")

    elif choose==6:
        Vaccinatted_people=input("Enter the Vaccinatted_people:")
        update=(Vaccinatted_people,SI)
        print("Vaccinatted_people updated successfully")
    
    else:
        print("Invalid choice....!!!")

elif option==4:
    SI=input("Enter your deleted SI no:")
    delete_data(SI)

else:
    print("Invalid option.....!!!!")




    







