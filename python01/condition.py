#assignment
#number=15

#if number>10:
 #   print("the number is greater")


#age=20

#if age>18:
 #   print("you're adult")

#number=int(input("enter a number: "))

#if number>0:
 #   print("number is positive")


#marks=40

#if marks>=40:
 #   print("you're pass")


number=int(input("enter your number: ").split()[0])

if number%2==0:
    print("positive")

else:
    print("not positive")

age=int(input("enter your age: ").split()[0])

if age>=18:
    print("Adult")

else:
    print("Minor")

Number=int(input("enter your number: ").split()[0])

if Number%2==0:
    print("The number is even")

else:
    print("The number is odd")


percentage=int(input('enter your percentage: ').split()[0])

if percentage>=40:
    print("you are pass")

else:
    print("you are fail")

greater=int(input("enter your first number: ").split()[0])
smaller=int(input("enter your second number: ").split()[0])

if greater>smaller:
    print("number is greater")

else:
    print("number is smaller")