#Q1
year = int(input("Please Enter the Year Number you wish:"))
if (year%4 == 0 and year%100!=0 or year%400 ==0):
     print("The year is Leap Year!")
else:
    print("The year is Not Leap Year")
#Q2
length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))
if length==breadth:
    print("It is a square")
else:
    print("It is a rectangle")
    
#Q3
    print ("Enter first age")
first = input()
print ("Enter second age")
second = input()
print ("third age")
third = input()

if first >= second and first >= third:
  print ("Oldest age",first)
elif second <= first and second <= third:
  print ("Oldest age",first)
elif third <= first and third <= second:
  print ("Oldest age",first)
else:
  print ("All are equal")

#Q4
  age = int(input("Enter your age: "))
sex = input("Enter your sex(M or F): ").upper()
marital_status = input("Enter marital status(Y or N): ").upper()
if sex=="F":
    print("Urban Areas")
else:
    if age>=20 and age<40:
        print("Work anywhere")
    elif age>=40 and age<60:
        print("Urban Areas")
    else:
        print("Error")

#Q5
       quantity = int (input("Enter the quantity:"))
Cost = 100

if quantity > 1000:
  print ("Cost is")(quantity*100)- (.1*quantity*100)
else:
  print ("Cost is",quantity*100)
  
#6
    
1=[]
for a in range(10):
    intiger=int(input("enter nos.:"))
    l.append(integer)
    print(l)
    for b in l:
        print(b)

#Q7
        while True:
    print("It's an infinite loop")

#Q8
    l = list(map(int,input().split()))
l_square = []
for i in l:
    l_square.append(i**2)
print(l_square)

#9
for num in range(1,101):
    for i in range(2,num):
        if (num%i==0):
            break
        else:
            print(num)
            break
#Q10
        def pypart(n): 
      for i in range(0, n): 
        for j in range(0, i+1): 
          print("* ",end="") 
        print("\r") 
n = 5
pypart(n) 

#11
l = list(map(int,input("Enter list elements: ").split()))
element = int(input("Enter the element to search: "))
if element in l:
    print("Element found")
    del l[l.index(element)]
print(l)
    
