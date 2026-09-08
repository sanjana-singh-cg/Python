#assignment
user_name=input("enter your first name and last name :")
print(user_name)
user_city=input("your city :")
print(user_city)
user_age=int(input("enter your age"))
print(user_age, type(user_age))
first_name=input("enter your first name :")
last_name=input("enter your last name :")
print(f"enter your first name{first_name} and enter your last name{last_name}")
name=input("student name :")
city=input("student city :")
college=input("student college name :")
print(f"student name is {name},student city is{city},student college is {college} ")
firstname,lastname=input("enter your first name and last name :").split()
print(f"first name{firstname},last name{lastname}")
a,b=input("first latter and last latter :").split()
a,b,c=input("1 ,2 and 3 word :").split()
print(a,b,c)
a="25"
b=int(a)
c="25.5"
d=float(c)
e=100
f=str(e)
print(b,c,f,type(c))
g=int(input("take a number :"))
print(g,type(g))
h=int(input(("enter first number :")))
i=int(input("enter second number :"))
print(h+i)
Name="Rahul"
age=20
print(f"my name is {Name} and I am {age} years old")
A=10
B=20
print(f"sum of :{A+B}")
product_price=999.35678
print(f"{product_price:.2f}")
print("A","B","C")
print("2026","08","19",sep="-")
print("Hello",end=" ")
print("World")
price=int(input("product price :"))
quantity=int(input("product quantity"))
print(f"price of product is {price} and quantityt of product is {quantity} ,total{price*quantity}")
name=input("enter student name")
age=int(input("enter student age"))
marks=float(input("enter student marks"))
print(f"student name is {name},student age is {age} and student marks are {marks}")

