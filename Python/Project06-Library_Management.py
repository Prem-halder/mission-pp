import json
import os
from datetime import datetime

def library():
    book_file="books.json"
    admin_file="library_admin.json"
    member_file="member.json"
    issue_file="issue.json"

    books = {
    "101": {"title": "Python Basics", "author": "John Smith", "copies": 5},
    "102": {"title": "Advanced Python", "author": "David Brown", "copies": 3},
    "103": {"title": "C++ Fundamentals", "author": "Bjarne Stroustrup", "copies": 4},
    "104": {"title": "Data Structures", "author": "Mark Allen", "copies": 6},
    "105": {"title": "Algorithms Made Easy", "author": "Narasimha Karumanchi", "copies": 4},
    "106": {"title": "Operating Systems", "author": "Abraham Silberschatz", "copies": 3},
    "107": {"title": "Computer Networks", "author": "Andrew S. Tanenbaum", "copies": 5},
    "108": {"title": "Database Management Systems", "author": "Raghu Ramakrishnan", "copies": 4},
    "109": {"title": "Artificial Intelligence", "author": "Stuart Russell", "copies": 2},
    "110": {"title": "Machine Learning Basics", "author": "Tom Mitchell", "copies": 3},
    "111": {"title": "Java Programming", "author": "Herbert Schildt", "copies": 5},
    "112": {"title": "JavaScript Essentials", "author": "Ethan Clark", "copies": 4},
    "113": {"title": "HTML & CSS Guide", "author": "Jennifer Robbins", "copies": 6},
    "114": {"title": "Linux Command Line", "author": "William Shotts", "copies": 3},
    "115": {"title": "Git & GitHub", "author": "Scott Chacon", "copies": 5},
    "116": {"title": "Cyber Security Basics", "author": "Charles Brooks", "copies": 4},
    "117": {"title": "Cloud Computing", "author": "Rajkumar Buyya", "copies": 3},
    "118": {"title": "Software Engineering", "author": "Ian Sommerville", "copies": 5},
    "119": {"title": "Clean Code", "author": "Robert C. Martin", "copies": 2},
    "120": {"title": "Introduction to SQL", "author": "Alan Beaulieu", "copies": 4}
    }

    admins={"1001":{"name":"Main Admin","pass":"12345678","last_book":120,"last_member":101}}

    def initialize(file,item):
        if not os.path.exists(file):
            with open(file,"w") as f:
                json.dump(item,f,indent=2)
    
    initialize(book_file,books)
    initialize(admin_file,admins)
    initialize(member_file,{})
    initialize(issue_file,{})

    def load(file):
        with open(file,"r") as f:
            return json.load(f)
    
    def save(file,item):
        with open(file,"w") as f:
            json.dump(item,f,indent=2)

    def login(file,id):
        if not file:
            print("NO DATA TO LOGIN!!")
            return False
        
        else:
            if id in file:
                Pass=input("ENTER PASSWORD:")
                for n in file:
                    if n == id and file[n]["pass"] == Pass:
                        print("LOGIN SUCCESSFULLY...")
                        return True
                print("LOGIN FAILED DUE TO INCORRECT PASSWORD...")
                return False
            else:
                print("NO SUCH ID IN MEMBER LIST!!")
                print("LOGIN FAILED...")
                return False      
       
    def add_member(member,admin):
        name=input("ENTER YOUR NAME:")
        Pass=input("CREATE PASSWORD:")
        print("======================================")
        print("|        AVAILABLE MEMBERSHIP        |")
        print("======================================")
        print("| 1.BASIC MEMBERSHIP(2 BORROW).      |")
        print("| 2.GOLD MEMBERSHIP(3 BORROW).       |")
        print("| 3.DIAMOND MEMBERSHIP(5 BORROW).    |")
        print("======================================")
        while True:
            try:
                ch=int(input("CHOOSE MEMBERSHIP(1-3):"))
                if ch == 1:
                    membership="Basic Membership."
                    num=2
                    break
                elif ch ==2:
                    membership="Gold Membership."
                    num=3
                    break
                elif ch==3:
                    membership="Diamond Membership."
                    num=5
                    break
                else:
                    print("INVALID CHOICE!!")
            except ValueError:
                print("NUMBERS ONLY!!")

        member[admin["1001"]["last_member"]]={"name":name,"pass":Pass,"membership":membership,"max_borrow":num,"current_borrow":0}
        print("YOUR MEMBER ID:",admin["1001"]["last_member"])
        admin["1001"]["last_member"]+=1
        save(admin_file,admin)
        save(member_file,member)

    def view(book):
        for n in book:
            print(n,"- Title:",book[n]["title"])
            print("    Author:",book[n]["author"])
            print("    Available Copies:",book[n]["copies"])

    def available(id,book):
        if book[id]["copies"]>0:
            return True
        else:
            print("BOOK CURRENTLY UN-AVAIAVLBE!!")

    def borrow(member,mem_id,issue,book):
        id=input("ENTER BOOK ID THAT YOU WANT TO BORROW:")
        if id in book:
            if available(id,book):
                if mem_id in issue:
                    if member[mem_id]["max_borrow"]>member[mem_id]["current_borrow"]:
                        dt=datetime.now()
                        issue[mem_id][f"{member[mem_id]["current_borrow"]+1}"]={"book_id":id,"title":book[id]["title"],"author":book[id]["author"],"borrowed_on":str(dt.date())}
                        book[id]["copies"]-=1
                        member[mem_id]["current_borrow"]+=1                          
                    else:
                        print("BORROW LIMIT IS ALREADY REACHED RETURN A BOOK TO BORROW AGAIN!!")
                else:
                    dt=datetime.now()
                    issue[mem_id]={member[mem_id]["current_borrow"]+1:{}}
                    issue[mem_id][member[mem_id]["current_borrow"]+1]={"book_id":id,"title":book[id]["title"],"author":book[id]["author"],"borrowed_on":str(dt.date())}
                    book[id]["copies"]-=1
                    member[mem_id]["current_borrow"]+=1
                save(member_file,member)
                save(book_file,book)
                save(issue_file,issue)
        else:
            print("ENTERED BOOK ID IS NOT AVAIABLE IN THIS LIBRARY!!")

    def returns(member,mem_id,issue,book):
        id=input("ENTER BOOK ID THAT YOU WANT TO RETURN:")
        if id in book:
            for key in list(issue[mem_id]):
                if issue[mem_id][key]["book_id"] == id and member[mem_id]["current_borrow"] == 1 :
                    issue.pop(mem_id)
                    book[id]["copies"]+=1
                    member[mem_id]["current_borrow"]-=1
                    save(issue_file,issue)
                    save(member_file,member)
                    save(book_file,book)
                    break
                elif issue[mem_id][key]["book_id"] == id and member[mem_id]["current_borrow"] > 1:
                    issue[mem_id].pop(key)
                    book[id]["copies"]+=1
                    member[mem_id]["current_borrow"]-=1
                    break
        else:
            print("ENTERED BOOK ID IS NOT AVAILABLE IN THIS LIBRARY!!")

    def borrow_check(mem_id):
        issue=load(issue_file)
        if mem_id in issue:
            for n in issue[mem_id]:
                print("MEMBER ID:",mem_id)
                print(issue[mem_id][n]["title"])
                print("AUTHOR:",issue[mem_id][n]["author"])
                print("BORROW DATE:",issue[mem_id][n]["borrowed_on"])

    def add_book(file,book):
        while True:
            try:
                id=int(input("ENTER BOOK ID:"))
                break
            except ValueError:
                print("NUMBERS ONLY!!")

        if str(id) in book:
            print("SAME BOOK ID ALREADY EXISTS!!")
        else:
            name=input("ENTER BOOK NAME:")
            author=input("ENTER AUTHOR NAME:")
            while True:
                try:
                    copy=int(input("ENTER NUMBER OF COPIES AVAILABLE:"))
                    break
                except ValueError:
                    print("NUMBERS ONLY!!")
            check=True
            for n in book:
                if book[n]["title"] == name and book[n]["author"] == author:
                    print("SAME BOOK EXISTS WITH DIFFERENT BOOK ID!!")
                    check=False
                    break
            if check:
                book[str(id)]={"title":name,"author":author,"copies":copy}
                print("NEW BOOK ADDED!!\n")
                save(file,book)

    def delete(file,data,issue,id):
        check=1
        if str(id) in data:
            for n in issue:
                for k in issue[n]:
                    if str(id) in issue[n][k]["book_id"]:
                        check=0
                        break
                if check == 0:
                    break
            if check == 1:
                data.pop(str(id))
                save(file,data)
                return True
            else:
                return False
        else:
            print("THIS ID DOESN'T EXISTS!!")        

    def update(book):
        while True:
            try:
                id=int(input("ENTER BOOK ID:"))
                break
            except ValueError:
                print("NUMBERS ONLY!!")
        if str(id) in book:
            while True:
                try:
                    print("100+ FOR UPDATING OR -1 FOR NOT CHANGING!")
                    id2=int(input("ENTER UPDATED BOOK ID:"))
                    if id2 in book:
                        print("SAME BOOK ID EXISTS ENTER A DIFFERENT ONE!!")
                    elif id2 > 100 or id2 == -1:
                        break
                    else:
                        print("INVALID ID!!")
                except ValueError:
                    print("NUMBERS ONLY!!")
            title2=input("ENTER UPDATED BOOK NAME:")
            author2=input("ENTER UPDATED AUTHOR NAME:")
            while True:
                try:
                    copy2=int(input("ENTER UPDATED NUMBER OF COPIES OF BOOK:"))
                    if copy2 == -1 or copy2 >=0:
                        break
                    else:
                        print("INVALID AMOUNT!!")
                except ValueError:
                    print("NUMBERS ONLY!!")
            if id2 != -1:
                temp=book[str(id)]
                book.pop(str(id))
                book[str(id2)]=temp
                if title2.strip()!="":
                    book[str(id2)]["title"]=title2
                if author2.strip()!="":
                    book[str(id2)]["author"]=author2
                if str(copy2).strip()!="":
                    book[str(id2)]["copies"]=copy2
                save(book_file,book)
            else:
                if title2.strip()!="":
                    book[str(id)]["title"]=title2
                if author2.strip()!="":
                    book[str(id)]["author"]=author2
                if str(copy2).strip()!="":
                    book[str(id)]["copies"]=copy2
                save(book_file,book)
        else:
            print("THIS BOOK IS NOT IN LIBRARY!!") 

    while True:
        print("======================================")
        print("| Welcome To Online Library Portal!! |")
        print("======================================")
        print("| 1.BECOME MEMBER.                   |")
        print("| 2.VIEW BOOKS.                      |")
        print("| 3.BORROW BOOKS.                    |")
        print("| 4.RETURN BOOKS.                    |")
        print("| 5.CHECK BORROWED BOOKS.            |")
        print("| 6.ADMIN PANEL.                     |")
        print("| 7.EXIT.                            |")
        print("======================================") 

        while True:
            try:
                ch=int(input("ENTER YOUR OPERATION:"))
                break
            except ValueError:
                print("NUMBERS ONLY")

        if ch==1:
            member=load(member_file)
            admin=load(admin_file)
            add_member(member,admin)

        elif ch==2:
            book=load(book_file)
            view(book)

        elif ch==3:
            print("LOGIN FIRST TO BORROW!!")
            member=load(member_file)
            mem_id=input("ENTER YOUR MEMBER ID:")
            if login(member,mem_id):
                issue=load(issue_file)
                book=load(book_file)
                if member[mem_id]["current_borrow"]==member[mem_id]["max_borrow"]:
                    print("MAX BORROW LIMIT IS REACHED!!")
                else:
                    borrow(member,mem_id,issue,book)
                if member[mem_id]["max_borrow"]>member[mem_id]["current_borrow"]:
                    while member[mem_id]["max_borrow"]>member[mem_id]["current_borrow"]:
                        ch=input("DO YOU WANT TO BORROW ANOTHER BOOK(Y/N)? :")
                        if ch.upper()=="Y":
                            borrow(member,mem_id,issue,book)
                        elif ch.upper()=="N":
                            break
                        else:
                            print("INVALID CHOICE!!")
                else:
                    print("MAX BORROW LIMIT REACHED TO BORROW MORE RETURN OLD BOOKS!!")

        elif ch==4:
            print("LOGIN FIRST TO RETURN!!")
            member=load(member_file)
            mem_id=input("ENTER YOUR MEMBER ID:")
            if login(member,mem_id):
                issue=load(issue_file)
                book=load(book_file)
                while member[mem_id]["current_borrow"]>0:
                    if member[mem_id]["current_borrow"]==0:
                        print("NOTHING IS BORROWED TO RETURN!!")
                        break
                    else:
                        returns(member,mem_id,issue,book)
                    while True:
                        if member[mem_id]["current_borrow"]==0:
                            print("NOTHING IS BORROWED TO RETURN!!")
                            break
                        ch=input("DO YOU WANT TO RETURN ANOTHER BOOK TOO(Y/N)? :")
                        if ch.upper()=="Y":
                            returns(member,mem_id,issue,book)
                        elif ch.upper()=="N":
                            save(issue_file,issue)
                            save(member_file,member)
                            save(book_file,book)
                            break
                        else:
                            print("INVALID CHOICE!!")
                     
        elif ch==5:
            print("LOGIN FIRST TO CHECK YOUR BORROWED BOOKS!!")
            member=load(member_file)
            mem_id=input("ENTER YOUR MEMBER ID:")
            if login(member,mem_id):
                borrow_check(mem_id)

        elif ch==6:
            print("ENTERING ADMIN PANEL!!")
            print("LOGIN FIRST TO ENTER ADMIN PANEL!!")
            admin=load(admin_file)
            mem_id=input("ENTER YOUR MEMBER ID:")
            if login(admin,mem_id):
                while True:
                    print("======================================")
                    print("|      Welcome To ADMIN PANEL!!      |")
                    print("======================================")
                    print("| 1.VIEW BOOKS.                      |")
                    print("| 2.ADD BOOKS.                       |")
                    print("| 3.UPDATE BOOKS.                    |")
                    print("| 4.DELETE BOOKS.                    |")
                    print("| 5.VIEW ALL MEMBERS.                |")
                    print("| 6.DELETE MEMBER.                   |")
                    print("| 7.VIEW ALL BORROWED BOOKS.         |")
                    print("| 8.EXIT.                            |")
                    print("======================================")

                    while True:
                        try:
                            ch=int(input("ENTER YOUR OPERATION :"))
                            break
                        except ValueError:
                            print("INVALID CHOICE!!")

                    if ch==1:
                        book=load(book_file)
                        view(book)
                    
                    elif ch==2:
                        book=load(book_file)
                        add_book(book_file,book)
                                            
                    elif ch==3:
                        book=load(book_file)
                        update(book)

                    elif ch==4:
                        book=load(book_file)
                        issue=load(issue_file)
                        while True:
                            try:
                                id=int(input("ENTER BOOK ID:"))
                                break
                            except ValueError:
                                print("NUMBERS ONLY!!")
                        result=delete(book_file,book,issue,id)
                        if not result:
                            print("THIS BOOK IS ISSUED TO A MEMBER!!") 
                            print("CAN'T DELETE BOOK DATA UNTIL THE MEMBER RETURNS THE BOOK!!")
                                               
                    elif ch==5:
                        member=load(member_file)
                        if not member:
                            print("NO MEMBERS AT THE LIBRARY!!")
                        else:
                            for n in member:
                                print("MEMBER ID:",n)
                                print("NAME:",member[n]["name"])
                                print("MEMBERSHIP:",member[n]["membership"])
                                print(" ")

                    elif ch==6:
                        member=load(member_file)
                        issue=load(issue_file)
                        while True:
                            try:
                                id=int(input("ENTER MEMBER ID:"))
                                break
                            except ValueError:
                                print("NUMBERS ONLY!!")
                        result=delete(member_file,member,issue,id)
                        if not result:
                            print("THIS MEMBER IS ISSUED A BOOK!") 
                            print("CAN'T DELETE MEMBER DATA UNTIL THEY RETURNS THE BOOK!!")

                    elif ch==7:
                        issue=load(issue_file)
                        if not issue:
                            print("NO BOOK BORROWED AT THE MOMENT!!")
                        else:
                            for n in issue:
                                print("MEMBER ID:",n)
                                for k in issue[n]:
                                    print(" ")
                                    print("BORROW NUMBER:",k,"BY",n)
                                    print("BOOK ID:",issue[n][k]["book_id"])
                                    print("BOOK:",issue[n][k]["title"])
                                    print("AUTHOR:",issue[n][k]["author"])
                                    print("BORROWED ON:",issue[n][k]["borrowed_on"])

                    elif ch==8:
                        print("EXITING....")
                        print("CLOSED!!")
                        break

                    else:
                        print("INVALID CHOICE!!")
                                 
        elif ch==7: 
            print("EXITING...")
            print("CLOSED...")
            break

        else:
            print("INVALID CHOICE!!")

library()