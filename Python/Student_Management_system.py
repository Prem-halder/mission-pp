import json
import os

def school():
    def initialize():
        if not os.path.exists("student.json"):
                with open("student.json","w") as f:
                    json.dump({},f)
    initialize()

    def load_data():
        with open("student.json","r") as f:
            return json.load(f)

    def save_data(save):
        with open("student.json","w") as f:
            json.dump(save,f,indent=4)
        
    def get_name():
        while True:
            name=input("ENTER STUDENT'S NAME :")
            if len(name)<2:
                print("ENTER A VALID NAME:")
            else:
                return name
            
    def get_roll():
        while True:
                try:
                    roll=int(input("ENTER STUDENT'S ROLL NUMBER :"))
                    return str(roll)
                except ValueError:
                    print("NUMBERS ONLY!!")

    def get_marks():
        while True:
            while True:
                try:
                    marks=int(input("ENTER STUDENT'S MARKS OUT OF 500 :"))
                    break
                except ValueError:
                    print("NUMBERS ONLY!!")
            if marks<0 or marks>500:
                print("MARKS CAN BE BETWEEN 0-500 ONLY!!")
            else:
                return marks

    def roll_check(roll):
        student=load_data()
        if roll in student.keys():
            return True
        else:
            print("STUDENT NOT FOUND!!")

    def add_student(roll,name,marks):
        load=load_data()
        load[roll]={"name":name,"marks":marks}
        save_data(load)
    
    def topper(load):
        while True:
            if not load:
                print("NO DATA IN FILE THAT CAN BE DELETED!!")
                break
            check=0
            roll=0
            for n in load.keys():
                if load[n]["marks"]>check:
                    check=load[n]["marks"]
                    roll=n
            print(f"STUDENT WITH ROLL NUMBER :{roll}") 
            print(f"NAME:{load[roll]['name']}")
            print(f"TOPPED WITH {check} MARKS")

    def average(load):
        while True:
            if not load:
                print("NO DATA IN FILE THAT CAN BE DELETED!!")
                break
            num=0
            student_count=0
            for n in load.keys():
                num+=load[n]["marks"]
                student_count+=1
            print(f"AVERAGE MARKS OF ALL STUDENTS ={num/student_count}")

    while True:
        print("=============================")
        print("  STUDENT MANAGEMENT SYSTEM  ") 
        print("=============================")  
        print("1.ADD STUDENT!!")
        print("2.VIEW ALL STUDENTS!!")
        print("3.SEARCH STUDENT!!") 
        print("4.UPDATE STUDENT!!")
        print("5.DELETE STUDENT!!")
        print("6.SHOW TOPPER!!")
        print("7.SHOW AVERAGE MARKS!!")
        print("8.EXIT")

        while True:
            try:
                ch=int(input("ENTER YOUR OPERATION :"))
                break
            except ValueError:
                print("NUMBERS ONLY(1-8)!!")

        if ch==1:
            roll=get_roll()
            name=get_name()
            marks=get_marks()
            if roll_check(roll):
                add_student(roll,name,marks)
                print("STUDENT'S DATA ENTERED SUCCESSFULLY!!")
            else:
                print("STUDENT WITH THIS ROLL NUMBER ALREADY EXISTS!!")

        elif ch==2:
            load=load_data()
            for n in load.keys():
                print("ROLL NUMBER :",n)
                print("NAME :",load[n]["name"])
                print("MARKS :",load[n]["marks"])
                print(" ")

        elif ch==3:
            roll=get_roll()
            load=load_data()
            if roll_check(roll):
                print(load[roll])

        elif ch==4:
            roll=get_roll()
            load=load_data()
            if roll_check(roll):
                print("IF YOU DON'T WANT TO CHANGE SOME DATA PUT IT AS IT IS BELOW!!")
                print(load[roll])
                name=get_name()
                marks=get_marks()
                temp={"name":name,"marks":marks}
                load[roll]=temp
                save_data(load)
                print("STUDENT'S DATA UPDATED SUCCESSFULLY!!")
                                  
        elif ch==5:
            print("DELETION OF DATA SELECTED!!")
            roll=get_roll()
            load=load_data()
            if roll_check(roll):
                load.pop(roll)
                save_data(load)
                print("STUDENT'S DATA DELETED SUCCESSFULLY!!")

        elif ch==6:
            while True:
                load=load_data()
                topper(load)

        elif ch==7:
            load=load_data()
            average(load)            

        elif ch==8:
            print("EXITING....")
            print("CLOSED!!")
            break

        else:
            print("INVALID CHOICE!!!")

school()