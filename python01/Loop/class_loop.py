#loop

# for i in range(1,20):
#     if i%2==0:
#         print(f"{i} is even!!")

# number=int(input("enter your number: ").split()[0])
# for i in range(1,number+1):
#     if i%2==1:
#         print(f"{i} is odd!!")

# num1=int(input("enter your first number: ").split()[0])
# num2=int(input("enter your second number: ").split()[0])
# for i in range(num1,num2+1):
#     if i%2==0:
#         print(f"{i}is even number!!")

# str=input("enter a string: ").strip().lower()
# str1=""
# length=len(str)
# for element in range(length-1,-1,-1):
#      str1=str1+str[element]
# print(str1)
# if str==str1:
#     print("palindrom")
# else:
#     print("not palindrom")

# name="python"
# for character in name:
#     print(character)
    
# word="python"
# count=0
# for chracter in word:
#     count=count+1
#     #count+=1 
# print("character:",count) 

# word="banana"
# count=0
# for chracter in word:
#      if chracter =="a":
#           count=count+1
# print("count:",count)


# for i in range(3):
#     for j in range(2):
#          print(i,j)

# for row in range(5):
#     for column in range(4):
#         print("*",end="")
#     print()

# for i in range(4):
#     for column in range(i+1):
#         print("*",end="")
#     print()

# for i in range(4):
#     for column in range(i-1):
#         print("*",end="")
#     print()

# n=int(input("enter your number of row: " ).split()[0])
# for i in range(1,n):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# for i in range(5,6):
#     for j in range(1,11):
#         print(f"{i}×{j} = {i*j}")
#     print()

# for i in range(1):
#     for j in range(5):
#         print("12345")

# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(j,end="")
#     print()
    

# for i in range(1,6):
#     for j in range(1,6):
#         print((i,j))

# for i in range(1,5):
#     for j in range(1,i):
#         print(j,end="")
#     print()
      
# for i in range(5):
#     for k in range(1,5-i):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end="")
#     print()

# n=int(input("enter you rom number: ").split()[0])
# for i in range(1,n+1):
#     for k in range(1,n+1-i):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# for i in range(1,5):
#     for k in range(5-i,5):
#         print(" ",end="")
#     for j in range(4,i-1,-1):
#         print("*",end="")
#     print()

# # peramide loop
# for i in range(5):
#     for k in range(1,5-i):
#         print(" ",end="")
#     for j in range(2*i+1):
#         print("*",end="")
#     print()

# for i in range(5):
#     for j in range(5):
#         if j==0 or j==4 or i==4:
#             print("*",end=" ")
#         else:
#             print("  ",end="")
#     print()

# n=int(input("enter your row: ").split()[0])
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or j==n or i==n:
#             print("*",end=" ")
#         else:
#             print("  ",end="")
#     print()

# n=int(input("enter your row: ").split()[0])
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or j==n or i==n or ((i==n/2 or i==n/n) and (j==n/2 or j==n/n)):
#             print("*",end=" ")
#         else:
#             print("  ",end="")
#     print()