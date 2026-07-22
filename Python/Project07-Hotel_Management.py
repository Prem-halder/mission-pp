import json
import os
from datetime import datetime

def hotel():
    room_file="rooms.json"
    admin_file="admin.json"
    bill_file="bills.json"
    user_file="user.json"
    book_file="room_booked.json"

    def initialize(file,item):
        if not os.path.exists(file):
            with open(file,"w") as f:
                json.dump(item,f,indent=2)
    
    def data_initialize():
        rooms = {
        "101": {
            "type": "Single",
            "price": 1200,
            "status": "Available"
        },
        "102": {
            "type": "Single",
            "price": 1200,
            "status": "Available"
        },
        "103": {
            "type": "Single",
            "price": 1200,
            "status": "Available"
        },
        "104": {
            "type": "Double",
            "price": 1800,
            "status": "Available"
        },
        "105": {
            "type": "Double",
            "price": 1800,
            "status": "Available"
        },
        "106": {
            "type": "Double",
            "price": 1800,
            "status": "Available"
        },
        "107": {
            "type": "Deluxe",
            "price": 2500,
            "status": "Available"
        },
        "108": {
            "type": "Deluxe",
            "price": 2500,
            "status": "Available"
        },
        "109": {
            "type": "Deluxe",
            "price": 2500,
            "status": "Available"
        },
        "110": {
            "type": "Suite",
            "price": 4000,
            "status": "Available"
        },
        "111": {
            "type": "Suite",
            "price": 4000,
            "status": "Available"
        },
        "112": {
            "type": "Family",
            "price": 5000,
            "status": "Available"
        },
        "113": {
            "type": "Family",
            "price": 5000,
            "status": "Available"
        },
        "114": {
            "type": "Luxury Suite",
            "price": 8000,
            "status": "Available"
        },
        "115": {
            "type": "Luxury Suite",
            "price": 8000,
            "status": "Available"
        }
        }
    
        admins = {
        "1001": {
            "name": "Main Admin",
            "Password": "12345678",
            "last_room": 116,
            "last_customer": 101,
            "total_earnings": 0
        }
        }
    
        initialize(room_file,rooms)
        initialize(admin_file,admins)
        initialize(bill_file,{})
        initialize(user_file,{})
        initialize(book_file,{})
    
    def load(file):
        with open(file,"r") as f:
            return json.load(f)
    
    def save(file,item):
        with open(file,"w") as f:
            json.dump(item,f,indent=2)

    def register(user,admin):
        while True:
            while True:
                name=input("Enter Your Name:")
                if len(name)>2:
                    break
                else:
                    print("Name Must Be Atleast 3 Alphabets Long!!")
        
            while True:
                try:
                    phone=int(input("Enter Your Mobile Number:"))
                    if len(str(phone)) == 10:
                        break
                    else:
                        print("Invalid Number!!")
                except ValueError:
                    print("Numbers Only!!")

            dupe=False

            if user:
                for n in user:
                    if user[n]["Phone"] == phone:
                        print("Same Number Is Registered With A Different Account!!")
                        print("Login To That Account Or Enter A Different Number!!")
                        dupe=True
                        break
                
            if dupe == False:
                while True:
                    Pass=input("Enter Your Password:")
                    if len(Pass)>7:
                        break
                    else:
                        print("Password Must Be Atleast 8 Characters Long!!")
            
                user[admin["1001"]["last_customer"]]={"Name":name,"Phone":phone,"Password":Pass,"Current_bookings":0,"Total_bookings":0}
                save(user_file,user)
                admin["1001"]["last_customer"]+=1
                save(admin_file,admin)
                print("\nACCOUNT REGISTERED SUCCESSFULLY!!\n")
                break

    def login(file,id):
        Pass=input("Enter Password:")
        for n in file:
            if n == id and file[n]["Password"] == Pass:
                print("\nLOGIN SUCCESSFULLY...\n")
                return True
        print("\nLOGIN FAILED DUE TO INCORRECT PASSWORD...\n")
        return False

    def view(room):
        for n in room:
            print(" ")
            print("Room Number:",n)
            print("Room Type:",room[n]["type"])
            print("Room Price:",room[n]["price"])
            print("Room Status:",room[n]["status"])

    def booking(user, room, bill, book, id):
        if user[id]["Current_bookings"] == 3:
            print("You Can't Book More Than 3 Rooms At A Time!!")
            return
        room_id = input("Enter Room Id: ")
        if room_id not in room:
            print("Invalid Room Id!!")
            return
        if room[room_id]["status"] != "Available":
            print("Room is", room[room_id]["status"])
            return
        while True:
            date = input("Enter Check-in Date (DD-MM-YYYY): ")
            try:
                check_in = datetime.strptime(date, "%d-%m-%Y")
                break
            except ValueError:
                print("Invalid Date Format!!")
        while True:
            try:
                days = int(input("Enter Number Of Days To Stay: "))
                if days > 0:
                    break
                else:
                    print("Days must be greater than 0!!")
            except ValueError:
                print("Numbers Only!!")
    
        if id not in book:
            book[id] = {}
        if id not in bill:
            bill[id] = {}

        book[id][user[id]["Current_bookings"] + 1] = {
        "Room": room_id,
        "Type": room[room_id]["type"],
        "Price": room[room_id]["price"],
        "Check_In": str(check_in.date()),
        "Days": days,
        "Status": "Booked"
        }
        bill[id][user[id]["Total_bookings"] + 1] = {
        "Room": room_id,
        "Type": room[room_id]["type"],
        "Price": room[room_id]["price"],
        "Days": days,
        "Total": room[room_id]["price"] * days,
        "Status": "Booked"
        }
        room[room_id]["status"] = "Booked"
        user[id]["Current_bookings"] += 1
        user[id]["Total_bookings"] += 1

        save(user_file, user)
        save(room_file, room)
        save(book_file, book)
        save(bill_file, bill)

        print("\nROOM BOOKED SUCCESSFULLY!")
        print("Room :", room_id)
        print("Type :", room[room_id]["type"])
        print("Check-In :", check_in.date())
        print("Days :", days)
        print("Total Bill : ₹", room[room_id]["price"] * days)

    def cancel(user, room, bill, book, id):
        if id not in book:
            print("No Data About Your Booking Avaialble!!")
            return
        room_id = input("Enter Room Id: ")
        if room_id not in room:
            print("Invalid Room Id!!")
            return
        temp=book[id]
        for k in range(1,user[id]["Current_bookings"]+1):
            if temp[str(k)]["Room"] == room_id and user[id]["Current_bookings"] == 1 and temp[str(k)]["Status"] == "Booked":
                book.pop(id)
                room[room_id]["status"] = "Available"
                user[id]["Current_bookings"] -= 1
                save(user_file, user)
                save(room_file, room)
                save(book_file, book)
                for k in range(1,user[id]["Total_bookings"]+1):
                    if bill[id][str(k)]["Room"] == room_id and bill[id][str(k)]["Status"] == "Booked":
                        bill[id][str(k)]["Status"] = "Cancelled"
                save(bill_file, bill)
                print("\nBOOKING CANCELLED SUCCESSFULLY!!\n")
                return
            elif temp[str(k)]["Room"] == room_id and temp[str(k)]["Status"] == "Booked":
                temp.pop(str(k))
                for n in range(1,len(temp)+1):
                    if n > len(temp)+1:
                        return
                    if str(n) not in temp:
                        temp[str(n)]={}
                        temp[str(n)] = temp[str(n+1)]
                        temp.pop(str(n+1))
                book[id]=temp
                room[room_id]["status"] = "Available"
                user[id]["Current_bookings"] -= 1
                save(user_file, user)
                save(room_file, room)
                save(book_file, book)
                for k in range(1,user[id]["Total_bookings"]+1):
                    if bill[id][str(k)]["Room"] == room_id and bill[id][str(k)]["Status"] == "Booked":
                        bill[id][str(k)]["Status"] = "Cancelled"
                save(bill_file, bill)
                print("\nBOOKING CANCELLED SUCCESSFULLY!!\n")
                return
            elif temp[str(k)]["Room"] == room_id and temp[str(k)]["Status"] == "Occupied":
                print("Room is Occupied and can't be cancelled!!")
        print("THIS ROOM NEVER BOOKED!!")

    def check_in(book,bill,room,user,id):
        if id not in book:
            print("\nNo Booking by This User!!\n")
            return False
        room_id=input("Enter Room Id For Check-In:")
        if room_id in room:
            for k in range(1,user[id]["Current_bookings"]+1):
                if book[id][str(k)]["Room"] == room_id:
                    if book[id][str(k)]["Status"] == "Occupied":
                        print("\nThis Room Is Already Checked-In!!\n")
                        return False
                    book[id][str(k)]["Status"] = "Occupied"
                    break
            else:
                print("\nThis Room Is Not Booked By You Right Now!!\n")
                return False
            for k in range(1,user[id]["Total_bookings"]+1):
                if bill[id][str(k)]["Room"] == room_id and bill[id][str(k)]["Status"] == "Booked":
                    bill[id][str(k)]["Status"] = "Occupied"
                    break
            save(book_file,book)
            save(bill_file,bill)
            print("\nCHECK-IN SUCCESSFULLY COMPLETED!!\n")
            return True            
        else:
            print("\nInvalid Room Id!!\n")
            return False
        
    def check_out(book,bill,room,user,admin,id):
        if id not in book:
            print("\nNo Booking by This User!!\n")
            return False
        room_id=input("Enter Room Id For Check-Out:")
        if room_id in room:
            temp=book[id]
            for k in book[id]:
                if book[id][k]["Room"] == room_id:
                    if book[id][k]["Status"] != "Occupied":
                        print("\nThis Room Is Not Checked-In Yet!!\n")
                        return False
                    temp.pop(k)
                    for n in range(1,len(book[id])+1):
                        if str(n) not in book[id]:
                            book[id][str(n)]={}
                            book[id][str(n)] = book[id][str(n+1)]
                            book[id].pop(str(n+1))
                    for k in bill[id]:
                        if bill[id][k]["Room"] == room_id and bill[id][k]["Status"] == "Occupied":
                            bill[id][k]["Status"] = "Completed"
                            Earn=bill[id][k]["Total"]
                            break

                    room[room_id]["status"] = "Available"
                    user[id]["Current_bookings"] -=1
                    admin["1001"]["total_earnings"] += Earn
                    save(user_file,user)
                    save(room_file,room)
                    save(book_file,book)
                    save(bill_file,bill)
                    save(admin_file,admin)
                    print("\nCHECK-OUT SUCCESSFULLY COMPLETED!!\n")
                    return True
            print("\nThis Room Is Not Booked By You Right Now!!\n")
            return False
        else:
            print("\nInvalid Room Id!!\n")
            return False

    def view_book(book,id):
        if id not in book:
            print("No booking By this user!!")
            return
        print("Customer Id:",id)
        for k in book[id]:
            print("Booking Number:",k)
            print("Room Id:",book[id][k]["Room"])
            print("Type:",book[id][k]["Type"])
            print("Price Per Night:",book[id][k]["Price"])
            print("Total Stay Days:",book[id][k]["Days"])
            print("Check-In Date:",book[id][k]["Check_In"])

    def view_bill(bill,id):
        if id not in bill:
            print("No booking By this user till now!!")
            return
        print("Customer Id:",id)
        for k in bill[id]:
            print("Booking Number:",k)
            print("Room Id:",bill[id][k]["Room"])
            print("Type:",bill[id][k]["Type"])
            print("Price Per Night:",bill[id][k]["Price"])
            print("Total Stay Days:",bill[id][k]["Days"])
            print("Total Bill:",bill[id][k]["Total"])
            print("Status:",bill[id][k]["Status"])

    def change_pass(file,user,id):
        while True:
            Pass=input("Enter New Password:")
            if len(Pass)>7:
                break
            else:
                print("Password Must Be Atleast 8 Characters Long!!")
        
        user[id]["Password"]=Pass
        save(file,user)
        print("\nPASSWORD CHANGED SUCCESSFULLY!!\n")

    def add_room(admin,room):
        l=["Single","Double","Deluxe","Suite","Family","Luxury Suite"]
        for i in range(len(l)):
            print(f"{i}.{l[i]}")
        Type=input("Enter Room Type From List Above:")
        if Type.capitalize().strip() not in l:
            print("Invalid Type!!")
            return
        while True:
            try:
                price=int(input("Enter Room Price:"))
                if price > 1000:
                    break
                else:
                    print("Price Must be More Than 1000!!")
            except ValueError:
                print("Number Only!!")
        room[admin["1001"]["last_room"]]={"type":Type,"price":price,"status":"Available"}
        save(room_file,room)
        admin["1001"]["last_room"]+=1
        save(admin_file,admin)

    def update(room):
        room_id=input("Enter Room Id:")
        if room_id in room:
            l=["Single","Double","Deluxe","Suite","Family","Luxury Suite"]
            for i in range(len(l)):
                print(f"{i}.{l[i]}")
            Type=input("Enter Room's New Type(Or Same For Not Changing):")
            if Type.capitalize().strip() not in l:
                print("Invalid Type!!")
                return
            while True:
                try:
                    price=int(input("Enter Room's New Price(Or Same For Not Changing):"))
                    if price > 1000:
                        break
                    else:
                        print("Price Must be More Than 1000!!")
                except ValueError:
                    print("Number Only!!")
            room[room_id]["type"]=Type
            room[room_id]["price"]=price
            save(room_file, room)

    def delete(room,book,admin):
        room_id=input("Enter Room Id:")
        if room_id in room:
            for k in book:
                for j in book[k]:
                    if book[k][j]["Room"] == room_id:
                        print("Room is Booked By A User!!")
                        print("Hence Room Can't Be Deleted!!")
                        return
            room.pop(room_id)
            temp=room
            for k in range(101,len(room)+101):
                if str(k) not in temp:
                    temp[str(k)]={}
                    temp[str(k)] = temp[str(k+1)]
                    temp.pop(str(k+1))
            room=temp
            admin["1001"]["last_room"]-=1
            save(admin_file,admin)
            save(room_file,room)

    def view_customer(user):
        for k in user:
            print("\nCustomer Id:",k)
            print("Name:",user[k]["Name"])
            print("Phone:",user[k]["Phone"])
            print("Current Bookings:",user[k]["Current_bookings"])

    def delete_customer(user,book):
        id= input("Enter Customer Id:")
        if id in user:
            if id in book:
                print("This Customer Has A Booking!!")
                print("Therefore Can't Be Deleted!!")
                return
            user.pop(id)
            save(user_file,user)
        else:
            print("Unknown User!!")

    def view_all_book(book):
        if not book:
            print("No bookings At The Time!!")
            return
        for i in book:
            print("Customer Id:",i)
            for k in book[i]:
                print("Booking Number:",k)
                print("Room Id:",book[i][k]["Room"])
                print("Type:",book[i][k]["Type"])
                print("Price Per Night:",book[i][k]["Price"])
                print("Total Stay Days:",book[i][k]["Days"])
                print("Check-In Date:",book[i][k]["Check_In"])

    def view_check_in_out(bill,check):
        if check == "Occupied":
            print("Check-In Rooms In Bill-\n")
        else:
            print("Check-Out Rooms In Bill-\n")
        for k in bill:
            temp=False
            print("Customer Id:",k)
            for j in bill[k]:
                if bill[k][j]["Status"] == check:
                    print("Room:",bill[k][j]["Room"])
                    print("Type:",bill[k][j]["Type"])
                    print("Price:",bill[k][j]["Price"])

    def view_stats(book,bill,room,user,admin):
        total_rooms=len(room)
        available_rooms=0
        booked_rooms=0
        occupied_rooms=0
        for k in room:
            if room[k]["status"] == "Available":
                available_rooms+=1
        for k in book:
            for j in book[k]:
                if book[k][j]["Status"] == "Booked":
                    booked_rooms+=1
                else:
                    occupied_rooms+=1

        total_customers=len(user)
        active_customers=0
        for k in user:
            if user[k]["Current_bookings"] > 0:
                active_customers+=1
        
        current_bookings=0
        total_bookings=0
        for k in user:
            current_bookings += user[k]["Current_bookings"]
            total_bookings += user[k]["Total_bookings"]

        booked=0
        occupied=0
        completed=0
        cancelled=0
        for k in bill:
            for j in bill[k]:
                if bill[k][j]["Status"] == "Completed":
                    completed += 1
                elif bill[k][j]["Status"] == "Cancelled":
                    cancelled += 1
                elif bill[k][j]["Status"] == "Booked":
                    booked += 1
                else:
                    occupied +=1
        
        single=0
        double=0
        deluxe=0
        suite=0
        family=0
        luxury_suite=0
        for k in room:
            if room[k]["type"] == "Single":
                single += 1
            elif room[k]["type"] == "Double":
                double += 1
            elif room[k]["type"] == "Deluxe":
                deluxe += 1
            elif room[k]["type"] == "Suite":
                suite += 1
            elif room[k]["type"] == "Family":
                family += 1
            else:
                luxury_suite += 1

        earnings=admin["1001"]["total_earnings"]

        print(f"""
        ========== HOTEL STATISTICS ==========
        ROOM DETAILS
        --------------------------------------
        Total Rooms          : {total_rooms}
        Available Rooms      : {available_rooms}
        Booked Rooms         : {booked_rooms}
        Occupied Rooms       : {occupied_rooms}
        
        CUSTOMER DETAILS
        --------------------------------------
        Total Customers      : {total_customers}
        Active Customers     : {active_customers}
        
        BOOKING DETAILS
        --------------------------------------
        Current Bookings     : {current_bookings}
        Total Bookings       : {total_bookings}
        Booked               : {booked}
        Occupied             : {occupied}
        Completed            : {completed}
        Cancelled            : {cancelled}
        
        ROOM TYPES
        --------------------------------------
        Single               : {single}
        Double               : {double}
        Deluxe               : {deluxe}
        Suite                : {suite}
        Family               : {family}
        Luxury Suite         : {luxury_suite}
        
        HOTEL EARNINGS
        --------------------------------------
        Total Earnings       : ₹{earnings}       
        ======================================
        """)

    data_initialize()

    while True:
        print("======================================")
        print("|        REGISTER/LOGIN PAGE         |")
        print("======================================")
        print("| 1. Register Account                |")
        print("| 2. Customer Login                  |")
        print("| 3. Admin Login                     |")
        print("| 4. Exit                            |")
        print("======================================")

        while True:
            try:
                ch=int(input("Enter Your Operation:"))
                break
            except ValueError:
                print("NUMBERS ONLY!!")

        if ch == 1:
            user=load(user_file)
            admin=load(admin_file)
            register(user,admin)
        
        elif ch == 2:
            user=load(user_file)
            id=input("Enter Customer Id:")
            if id in user:
                if login(user,id):
                    while True:
                        print("======================================")
                        print("|      HOTEL MANAGEMENT SYSTEM       |")
                        print("======================================")
                        print("| 1. View Available Rooms            |")
                        print("| 2. Book Room                       |")
                        print("| 3. Cancel Booking                  |")
                        print("| 4. Check-In                        |")
                        print("| 5. Check-Out                       |")
                        print("| 6. View My Booking                 |")
                        print("| 7. View All Bills                  |")
                        print("| 8. Change Password                 |")
                        print("| 9. Logout                          |")
                        print("======================================")

                        while True:
                            try:
                                ch=int(input("Enter Your Operation:"))
                                break
                            except ValueError:
                                print("NUMBERS ONLY!!")

                        if ch == 1:
                            room=load(room_file)
                            view(room)  
    
                        elif ch == 2:
                            user=load(user_file)
                            room=load(room_file)
                            bill=load(bill_file)
                            book=load(book_file)
                            booking(user,room,bill,book,id)

                        elif ch == 3:
                            user=load(user_file)
                            room=load(room_file)
                            bill=load(bill_file)
                            book=load(book_file)
                            cancel(user, room, bill, book, id)

                        elif ch == 4:
                            book=load(book_file)
                            bill=load(bill_file)
                            room=load(room_file)
                            user=load(user_file)
                            check_in(book,bill,room,user,id)

                        elif ch == 5:
                            book=load(book_file)
                            bill=load(bill_file)
                            room=load(room_file)
                            user=load(user_file)
                            admin=load(admin_file)
                            check_out(book,bill,room,user,admin,id)
                        
                        elif ch == 6:
                            book=load(book_file)
                            view_book(book,id)

                        elif ch == 7:
                            bill=load(bill_file)
                            view_bill(bill,id)
                        
                        elif ch == 8:
                            user=load(user_file)
                            change_pass(user_file,user,id)

                        elif ch == 9:
                            print("\nExiting...")
                            print("Closed...\n")
                            break

                        else:
                            print("Invalid Choice!!")

            else:
                print("No Such Data Found!!")
        
        elif ch == 3:
            admin=load(admin_file)
            id=input("Enter Admin Id:")
            if id in admin:
                if login(admin,id):
                    while True:
                        print("======================================")
                        print("|      WELCOME TO ADMIN PANEL!!      |")
                        print("======================================")
                        print("| 1. VIEW ALL ROOMS.                 |")
                        print("| 2. ADD NEW ROOM.                   |")
                        print("| 3. UPDATE ROOM DETAILS.            |")
                        print("| 4. DELETE ROOM.                    |")
                        print("| 5. VIEW ALL CUSTOMERS.             |")
                        print("| 6. DELETE CUSTOMER.                |")
                        print("| 7. VIEW ALL BOOKINGS.              |")
                        print("| 8. CHECK-IN CUSTOMER.              |")
                        print("| 9. CHECK-OUT CUSTOMER.             |")
                        print("|10. CANCEL CUSTOMER BOOKING.        |")
                        print("|11. VIEW HOTEL STATISTICS.          |")
                        print("|12. VIEW TOTAL EARNINGS.            |")
                        print("|13. CHANGE ADMIN PASSWORD.          |")
                        print("|14. LOGOUT.                         |")
                        print("======================================")

                        while True:
                            try:
                                ch=int(input("Enter Your Operation:"))
                                break
                            except ValueError:
                                print("NUMBERS ONLY!!")

                        if ch == 1:
                            room=load(room_file)
                            view(room)

                        elif ch == 2:
                            admin=load(admin_file)
                            room=load(room_file)
                            add_room(admin,room)

                        elif ch == 3:
                            room=load(room_file)
                            update(room)

                        elif ch == 4:
                            room=load(room_file)
                            admin=load(admin_file)
                            book=load(book_file)
                            delete(room,book,admin)

                        elif ch == 5:
                            user=load(user_file)
                            view_customer(user)

                        elif ch == 6:
                            user=load(user_file)
                            book=load(book_file)
                            delete_customer(user,book)

                        elif ch == 7:
                            book=load(book_file)
                            view_all_book(book)

                        elif ch == 8:
                            bill=load(bill_file)
                            check="Occupied"
                            view_check_in_out(bill,check)

                        elif ch == 9:
                            bill=load(bill_file)
                            check="Completed"
                            view_check_in_out(bill,check)

                        elif ch == 10:
                            user=load(user_file)
                            customer_id=input("Enter Customer Id:")
                            if customer_id in user:               
                                room=load(room_file)
                                bill=load(bill_file)
                                book=load(book_file)
                                cancel(user, room, bill, book, customer_id)
                            else:
                                print("Invalid Customer Id!!")

                        elif ch == 11:
                            book=load(book_file)
                            bill=load(bill_file)
                            room=load(room_file)
                            user=load(user_file)
                            admin=load(admin_file)
                            view_stats(book,bill,room,user,admin)

                        elif ch == 12:
                            admin=load(admin_file)
                            print("\nTOTAL EARNING:",admin[id]["total_earnings"],"\n")

                        elif ch == 13:
                            admin=load(admin_file)
                            change_pass(admin_file,admin,id)

                        elif ch == 14:
                            print("\nExiting...")
                            print("Closed...\n")
                            break

                        else:
                            print("Invalid Choice!!")
            
            else:
                print("No Such Data Found!!")

        elif ch == 4:
            print("\nExiting...")
            print("Closed...\n")
            break

        else:
            print("Invalid Choice!!")

hotel()