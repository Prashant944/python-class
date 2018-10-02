year = int(input("Please Enter the Year Number you wish:"))
if (year%4 == 0 and year%100!=0 or year%400 ==0):
     print("The year is Leap Year!")
else:
    print("The year is Not Leap Year")
