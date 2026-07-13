import random

print("This is a Number guessing game with different difficulty modes!!!")

def num_game(high,low,play):
    print("""
    Easy(0-10)=1
    Normal(0-100)=2 
    Hard(0-1000)=3
    Impossible(0-10000)=4
    Exit=5
      """)
    while True:
        try:
            ch=int(input("Enter Your Choice:"))
            break
        except ValueError:
            print("Number only")
    guesses=0

    if ch==1:
        print("You chose Easy difficulty!!")
        num=random.randrange(0,11)
    elif ch==2:
        print("You chose Normal difficulty!!")
        num=random.randrange(0,101)
    elif ch==3:
        print("You chose Hard difficulty!!")
        num=random.randrange(0,1001)
    elif ch==4:
        print("You chose Impossible difficulty!!")
        num=random.randrange(0,10001)
    elif ch==5:
        print("Thanks for Playing!!")
    else:
        print("Not a valid choice!! Choose again!!")
        num_game(high,low,play)
    
    while True:
        if ch!=5 and play==0:
            while True:
                try:
                    guess=int(input("Guess the Number:"))
                    break
                except ValueError:
                    print("Number Only!!")
            if guess==num:
                guesses+=1
                print("You Won Hurray!!")
                print("Number Of Guesses:",guesses)
                print("You can Play Again or Exit:")
                if play==0:
                    high=guesses
                    low=guesses
                    play+=1
                else:
                    if guesses>high:
                        high=guesses
                    elif guesses<low:
                        low=guesses
                print("Highest Number of Guesses:",high)
                print("Lowest Number of Guesses:",low)
                ch2=input("Do you want to continue(Y/N):")
                if ch2=="Y" or ch2=="y":
                    num_game(high,low,play)
                else:
                    print("Thanks for Playing!!")
                    break      
            elif guess>num:
                guesses+=1
                print("Guess Lower!!")
            else:
                guesses+=1
                print("Guess Higher!!")
        else:
            break
    
high,low,play=0,0,0
print("Choose Difficulty:")
num_game(high,low,play)