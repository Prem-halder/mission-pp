name=input("Enter Name:")
sub_num=int(input("Number of subjects?:"))
num={}
high,low,marksobt,fail=0,100,0,0

for i in range(sub_num):
    sub=input(f"Subject {i+1} Name:")
    while True:
        marks=int(input("Marks obtained:"))
        if marks>=0 and marks<=100:
            break
        else:
            print("Marks should be betwwen 0-100 only try again!!")

    num[sub]=marks
    marksobt+=num[sub]
    if high<num[sub]:
        high=num[sub]
    if low>num[sub]:
        low=num[sub]
perc=marksobt/sub_num
print("Name:",name)
print("Total Marks:",marksobt,"/",sub_num*100)
print("Percentage:",perc,"%")
print("Maximum Marks in a Subject:",high)
print("Minimum Marks in a Subject:",low)

for name,mark in num.items():
    if mark<33:
        if fail==0:
            print(f"Failed due to subject back in {name}!!")
            fail+=1
        else:
            print(f",also in {name}!!")

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