import json
import os

print("This is a Simple Bank Account Management Program For basic needs like-")

def bank():
    def initialize():
        if not os.path.exists("last_anum.json"):
            with open("last_anum.json", "w") as f:
                json.dump({"last_anum": 1000}, f)
        if not os.path.exists("bank_register.json"):
            with open("bank_register.json", "w") as f:
                json.dump({}, f)
        if not os.path.exists("transactions.json"):
            with open("transactions.json", "w") as f:
                json.dump({}, f)

    def login(anum):
        with open("bank_register.json","r") as f:
            temp=json.load(f)
            if anum in temp.keys():
                dis=temp[anum]
                check=dis["Password:"]
                while True:
                    code=input("Enter Password:")
                    if check==code:
                        break
                    else:
                        print("Wrong Password!! Try Again!!")
                return True
            else:
                return False

    def account():
        trans,bank_book={},{}
        with open("bank_register.json","r") as f:
            bank_book=json.load(f)
        with open("transactions.json","r") as f:
            trans=json.load(f)
        with open("last_anum.json","r") as f:
            temp=json.load(f)
            anum=temp["last_anum"]+1
            temp["last_anum"]=anum
            anum=str(anum)
            name=input("Enter Name:")
            while True:
                password=input("Enter Password:")
                if len(password)>=8:
                    break
                else:
                    print("Password Must be 8 characters long!!")
            while True:
                try:
                    bal=int(input("Enter starting Balance:"))
                    break
                except ValueError:
                    print("Integers only!!")  
            trans[anum]=[f"Starting Balance:{bal}"]
            bank_book[anum]={"Name:":name,"Password:":password,"Balance:":bal}
            with open("bank_register.json","w") as f:
                json.dump(bank_book,f,indent=2)
            with open("transactions.json","w") as f:
                json.dump(trans,f,indent=2)
            with open("last_anum.json","w") as f:
                json.dump(temp,f)
            print("Your Account Number:",anum)
                

    def display(anum):
        with open("bank_register.json","r") as f:
            temp=json.load(f)
            dis=temp[anum]
            print("Your Details:")
            print("Account Number:",anum)
            print("Name:",dis["Name:"])
            print("Balance:",dis["Balance:"])   

    def deposit(anum,amount):
        with open("bank_register.json","r") as f:
            bank_book=json.load(f)
            bank_book[anum]["Balance:"]=bank_book[anum]["Balance:"]+amount
            with open("bank_register.json","w") as f:
                json.dump(bank_book,f,indent=2)
        with open("transactions.json","r") as f:
            trans=json.load(f)
            temp=f"Deposit:{amount}"
            trans[anum].append(temp)
            with open("transactions.json","w") as f:
                json.dump(trans,f,indent=2)

    def withdraw(anum,amount):
        with open("bank_register.json","r") as f:
            bank_book=json.load(f)
            bank_book[anum]["Balance:"]=bank_book[anum]["Balance:"]-amount
            with open("bank_register.json","w") as f:
                json.dump(bank_book,f,indent=2)
        with open("transactions.json","r") as f:
            trans=json.load(f)
            temp=f"Withdrawal:{amount}"
            trans[anum].append(temp)
            with open("transactions.json","w") as f:
                json.dump(trans,f,indent=2)

    def transaction(anum):
        with open("transactions.json","r") as f:
            trans=json.load(f)
            temp=trans[anum]
            print(temp)

    def transfer(anum,num,amount):
        withdraw(anum,amount)
        deposit(num,amount)

    print("---Choose from the Below---")
    print("1.Create Account!")
    print("2.Account info!")
    print("3.Deposit!")
    print("4.Withdraw!")
    print("5.Transaction History!")
    print("6.Transfer Money!")
    print("7.Exit")

    while True:
        try:
            ch=int(input("Enter Your Operation:"))
        except ValueError:
            print("Number only")
            continue
        initialize()
        if ch==1:
            account()
        elif ch==2:
            print("Login first!!")
            anum=input("Enter Account Number:")   
            if login(anum) is True:
                display(anum)
        elif ch==3:
            print("Login first!!")
            anum=input("Enter Account Number:")
            if login(anum) is True:
                while True:
                    try:
                        amount=int(input("Enter Ammount to be Deposited:"))
                        break
                    except ValueError:
                        print("Number only")
                deposit(anum,amount)
                print("Amount Deposits!!")
        elif ch==4:
            print("Login first!!")
            anum=input("Enter Account Number:")
            if login(anum)==True:
                with open("bank_book","r") as f:
                    temp=json.load(f)
                    temp2=temp[anum]["Balance:"]
                while True:
                    try:
                        amount=int(input("Enter Ammount to be Withdraw:"))
                        break
                    except ValueError:
                        print("Number only")
                if temp2>amount:
                    withdraw(anum,amount)
                    print("Amount Withdrawal!!")
                else:
                    print("Insufficient Balance!!")
        elif ch==5:
            print("Login first!!")
            anum=input("Enter Account Number:")
            if login(anum) is True:
                transaction(anum)
        elif ch==6:
            print("Login first!!")
            anum=input("Enter Account Number:")
            if login(anum) is True:
                num=input("Enter Account Number to Which money to be transfered:")
                if login(num)==True:
                    while True:
                        try:
                            amount=int(input("Enter Ammount to be Withdraw:"))
                            break
                        except ValueError:
                            print("Number only")
                    transfer(anum,num,amount)
        else:
            print("Thanks For Coming!!")
            break

bank()