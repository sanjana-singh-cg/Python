#loop

for i in range(1,20):
    if i%2==0:
        print(f"{i} is even!!")

number=int(input("enter your number: ").split()[0])
for i in range(1,number+1):
    if i%2==1:
        print(f"{i} is odd!!")

num1=int(input("enter your first number: ").split()[0])
num2=int(input("enter your second number: ").split()[0])
for i in range(num1,num2+1):
    if i%2==0:
        print(f"{i}is even number!!")
        