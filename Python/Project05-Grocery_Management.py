import json
import os

def grocery_store():

    def initialize():
        if not os.path.exists("grocery.json"):
            with open("grocery.json","w") as f:
                pro={"RICE :":60,"FLOUR :":50,"WATER :":20,"OIL :":150,"MILK :":30,"BREAD :":30}
                json.dump(pro,f,indent=4)
        if not os.path.exists("bill.json"):
            with open("bill.json","w") as f:
                json.dump({},f)
        if not os.path.exists("cart.json"):
            with open("cart.json","w") as f:
                json.dump({},f)
        if not os.path.exists("last_bill_num.json"):
            with open("last_bill_num.json","w") as f:
                json.dump({"last_num:":100},f,indent=4)
        if not os.path.exists("grocery_admin.json"):
            with open("grocery_admin.json","w") as f:
                admin={"name":"Main Admin","pass":"12345678","Total":0}
                json.dump(admin,f,indent=4)
    initialize()

    def load(file):
        with open(file,"r") as f:
            return json.load(f)
        
    def save(file,item):
        with open(file,"w") as f:
            json.dump(item,f,indent=4)

    def product(load):
        num=1
        print("=======PRODUCTS=======")
        for n in load.keys():
            print(f"{num}.{n}{load[n]}")
            num+=1
        print("======================")
    
    def quantity():
        while True:
            try:
                quantity=int(input("ENTER QUANTITY :"))
                return quantity
            except ValueError:
                print("NUMBERS ONLY!!")

    def remove(cart):
        if not cart:
            print("CART IS EMPTY!!")
        else:
            while True:
                choice=input("ENTER PRODUCT YOU WANT TO REMOVE FROM CART(LEAVE BLANK TO EXIT) :")
                temp=f"{choice.upper().rstrip()} :"
                if choice.strip()=="":
                    save("cart.json",cart)
                    break
                elif temp in cart.keys():
                    cart.pop(temp)
                    print("ITEM REMOVED!!")
                else:
                    print("INVALID ITEM!!")
                
    def view(cart,grocery):
        if not cart:
            print("CART IS EMPTY!!")
        else:
            total=0
            for temp in grocery:
                if temp in cart:
                    print(f" {temp} x",cart[temp])
                    print(" PRICE :",grocery[temp])
                    total+=cart[temp]*grocery[temp]
            
            print("================================")
            print(" GRAND TOTAL =",total)
            print("================================")

    def bill(cart,grocery,bills,last,admin):
        while True:
            if not cart:
                print("CART IS EMPTY!!")
                break
            else:
                name=input("ENTER YOUR NAME :")
                print("================================")
                print(" THANKS FOR PURCHASING FROM US! ")
                print("================================")
                print(" NAME :",name)
                print(" BILL NUMBER :",last["last_num:"]+1)
                view(cart,grocery)
                print(" AMOUNT PAID!!!")
                print("================================")

                bill_str=""
                total=0

                for n in cart:
                    bill_str+=f" {n} x {cart[n]},"
                    total+=cart[n]*grocery[n]
                
                num=last["last_num:"]+1
                bills[num]={"NAME :":name,"TOTAL AMOUNT OF CROCERY:":total,"GROCERY:":bill_str}
                save("bill.json",bills)
                last["last_num:"]=num
                save("last_bill_num.json",last)
                save("cart.json",{})
                admin["Total"]+=total
                save("grocery_admin.json",admin)
                break
        
    def login():
        name=input("ENTER ADMIN NAME :")
        Pass=input("ENTER PASSWORD :")
        load=load("grocery_admin.json")
        if load["name"]==name and load["pass"]==Pass:
            print("WELCOME TO ADMIN PANEL!!")
            return True
        else:
            print("INVALID NAME OR PASSWORD!!")

    def add_product(load):
        while True:
            check=input("DO YOU WANT TO ADD A PRODUCT(Y/N) :")
            if check=="Y" or check=="y":
                pro=input("ENTER PRODUCT NAME :")
                while True:
                    try:
                        price=int(input("ENTER PRODUCT'S PRICE :"))
                        break
                    except ValueError:
                        print("NUMBERS ONLY!!")
                load[f"{pro} :"]=price
            elif check=="N" or check=="n":
                save("grocery.json",load)
                break
            else:
                print("INVALID CHOICE!!")

    def update(load):
        while True:
            print("WHICH PRODUCT'S PRICE YOU WANT TO CHANGE FROM THE LIST ABOVE!!")
            ch=input("ENTER NAME OF THE ITEM(OR BLANK TO EXIT) :")
            temp=f"{ch.upper().rstrip()} :"

            if ch.strip()=="":
                save("grocery.json",load)
                break

            elif temp in load.keys():
                while True:
                    try:
                        price=int(input("ENTER UPDATED PRICE :"))
                        if price>0:
                            load[temp]=price
                            break
                        else:
                            print("PRICE CAN'T BE NEGATIVE OR ZERO!!")
                    except ValueError:
                        print("NUMBERS ONLY!!")
            else:
                print("ENTER ITEM IS NOT IN THE LIST!!")
                        
    def remove_product(load):
        while True:
            print("WHICH PRODUCT'S YOU WANT TO REMOVE FROM THE LIST ABOVE!!")
            ch=input("ENTER NAME OF THE ITEM(OR BLANK TO EXIT) :")
            temp=f"{ch.upper().rstrip()} :"

            if ch.strip()=="":
                save("grocery.json",load)
                break

            elif temp in load.keys():
                load.pop(temp)

            else:
                print("ENTER ITEM IS NOT IN THE LIST!!")
    
    def view_bill(load):
        for n in load.keys():
            print("BILL NUMBER :",n)
            print("NAME :",load[n]["NAME :"])
            print("TOTAL AMOUNT OF CROCERY:",load[n]["TOTAL AMOUNT OF CROCERY:"])
            print("GROCERYS:",load[n]["GROCERY:"])

    while True:
        print("=======GROCERY STORE=======")
        print("1.SHOW PRODUCTS.")
        print("2.ADD TO CART.")
        print("3.REMOVE PRODUCT FROM CART.")
        print("4.VIEW CART.")
        print("5.GENERATE BILL.")
        print("6.ADMIN PANEL.")
        print("7.EXIT.")
        print("===========================")
        print(" ")
        
        while True:
            try:
                ch=int(input("ENTER YOUR OPERATION :"))
                break
            except ValueError:
                print("INVALID CHOICE!!")
        
        if ch==1:
            load=load("grocery.json")
            product(load)

        elif ch==2:
            print("IF YOU RE-ENTER A ALREADY EXISTING ITEM IN THE CART ENTER THE NEW TOTAL QUANTITY!!")
            cart=load("cart.json")
            grocery=load("grocery.json")
            while True:
                choice=input("ENTER PRODUCT YOU WANT TO ADD TO CART(LEAVE BLANK TO EXIT) :")
                temp=f"{choice.upper().rstrip()} :"

                if choice.strip()=="":
                    save("cart.json",cart)
                    break
                elif temp in grocery:
                    quan=quantity()
                    cart[temp]=quan
                else:
                    print("ITEM NOT AVAILABLE IN PRODUCT LIST!!")                  

        elif ch==3:
            cart=load("cart.json")
            remove(cart)
        
        elif ch==4:
            cart=load("cart.json")
            grocery=load("grocery.json")
            view(cart,grocery)
        
        elif ch==5:
            cart=load("cart.json")
            grocery=load("grocery.json")
            bills=load("bill.json")
            last=load("last_bill_num.json")
            admin=load("grocery_admin.json")
            bill(cart,grocery,bills,last,admin)
        
        elif ch==6:
            print("ENTERED ADMIN PANEL!!")
            print("LOGIN FIRST!!")

            if login():
                while True:
                    print("======= ADMIN PANEL =======")
                    print("1.SHOW PRODUCTS.")
                    print("2.ADD NEW PRODUCTS.")
                    print("3.UPDATE PRODUCTS PRICE.")
                    print("4.DELETE PRODUCTS.")
                    print("5.VIEW ALL BILLS.")
                    print("6.TOTAL REVENUE.")
                    print("7.EXIT ADMIN PANEL.")
                    print("===========================")

                    while True:
                        try:
                            ch=int(input("ENTER YOUR OPERATION :"))
                            break
                        except ValueError:
                            print("INVALID CHOICE!!")

                    if ch==1:
                        load=load("grocery.json")
                        product(load)
                    
                    elif ch==2:
                        load=load("grocery.json")
                        add_product(load)

                    elif ch==3:
                        load=load("grocery.json")
                        product(load)
                        update(load)

                    elif ch==4:
                        load=load("grocery.json")
                        product(load)
                        remove_product(load)

                    elif ch==5:
                        load=load("bill.json")
                        view_bill(load)

                    elif ch==6:
                        load=load("grocery_admin.json")
                        print(" ")
                        print("TOTAL REVENUE:",load["Total"])
                        print(" ")
                    
                    else:
                        print("EXITING....")
                        print("CLOSED!!")
                        break           
        
        else:
            print("EXITING....")
            print("CLOSED!!")
            break

grocery_store()