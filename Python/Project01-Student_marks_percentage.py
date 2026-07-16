name=input("Enter Name:")
#No. of Subject input with exception 
while True:
    sub_num=int(input("Number of subjects?:"))
    if sub_num>0:
        break
    else:
        print("Number of subject must be more than 0!!")
num={}
high,low,marksobt,fail=0,100,0,0

for i in range(sub_num):
    #Subject name input without duplicate name
    while True:
        sub=input(f"Subject {i+1} Name:")
        if sub not in num.keys():
            break
        else:
            print("Same name detected Bruh dumbo!!Re-Enter-")
    #Marks input with range
    while True:
        marks=int(input("Marks obtained:"))
        if marks>=0 and marks<=100:
            break
        else:
            print("Marks should be between 0-100 only try again!!")

    num[sub]=marks
    marksobt+=num[sub]
    if high<num[sub]:
        high=num[sub]
    if low>num[sub]:
        low=num[sub]

perc=marksobt/sub_num
#Data Printing
print("Name:",name)
print("Total Marks:",marksobt,"/",sub_num*100)
print("Percentage:",perc,"%")
print("Maximum Marks in a Subject:",high)
print("Minimum Marks in a Subject:",low)

for sub_name,mark in num.items():
    if mark<33:
        if fail==0:
            print(f"Still Failed due to subject back in {sub_name}!!")
            fail+=1
        else:
            print(f",also in {sub_name}!!")

if fail>0:
    print("Net Grade:Fail(F)")
elif perc>=90:
    print("Net Grade:A+")
elif perc>=80:
    print("Net Grade:A")
elif perc>=70:
    print("Net Grade:B")
elif perc>=60:
    print("Net Grade:C")
elif perc>=50:
    print("Net Grade:D")
else:
    print("Net Grade:F")