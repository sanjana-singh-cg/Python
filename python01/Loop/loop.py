#assignment
# for i in range(1,6):
#     print("Hello")

# for i in range(0,10):
#     print(i ,end=" ")

# for i in range(1,11):
#     print(i)

# for i in range(10,1):
#     print(i)

# for i in range(2,20):
#     if i%2==0:
#         print(f"{i} is even number")

# for i in range(1,19):
#     if i%2==1:
#         print(f"{i} is odd number")

# for row in range(3):
#     for column in range(4):
#         print("*",end="")
#     print()

# for i in range(5):
#     for column in range(i+1):
#         print("*",end="")
#     print()
    
# for i in range(5):
#     for j in range(i+1):
#         print("1",end="")
#     print()

# n=int(input("enter your number of row: " ).split()[0])
# for i in range(1,n):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

    
# n=int(input("enter your number: ").split()[0])
# for i in range(1,n+1):
#     if i%2==0:
#         print(f"{i}is even number")

# for i in range(5,50,5):
#     print(i)

# for i in range(3,19,3):
#     print(i)

# for i in range(20,1,-2):
#     print(i)

# n=int(input("enter your number: ").split()[0])
# for i in range(1,n+1):
#     if i%2==1:
#         print(f"{i} is odd")

# n=int(input("enter your number: ").split()[0])
# for i in range(1,n+1):
#     if i%3==0:
#         print(f"{i} is divisibal by 3")

# n=int(input("enter your number: ").split()[0])
# for i in range(1,n+1):
#     if i%3==0 and i%2==0:
#         print(f"{i} is divisibal by both 3 and 2")

# n=int(input("enter your number: ").split()[0])
# count=0
# for character in range(1,n+1):
#     if character%2==0:
#         count=count+1    
# print("character:",count)

# n=int(input("enter your number: ").split()[0])
# total_sum=0
# for add in range(1,n+1):
#     total_sum+=add
    
# print(f"addition:",total_sum)

# n=int(input("enter your number: ").split()[0])
# even_sum=0
# for i in range(1,n+1):
#     if i%2==0:
#          even_sum+=i
# print(f"Addition of even number: ",even_sum)

# n=int(input("enter your number: ").split()[0])
# odd_sum=0
# for i in range(1,n+1):
#     if i%2==1:
#          odd_sum+=i
# print(f"Addition of odd number: ",odd_sum)

# n=int(input("enter your number: ").split()[0])
# multi=1
# for i in range(1,n+1):
#         multi*=i
# print(f"multiplication is: ",multi)

# str=(input("enter your number: ").split()[0])
# for i in str:
#     print(i)

# str=(input("enter your number: ").split()[0])
# for i in str:
#     print(i,end="")

# str=(input("enter your string: ").split()[0].lower())
# lenght=len(str)
# count=0
# for character in range(0,lenght):
#     count=count+1
# print("character: ",count)

# str=(input("enter your word: ").split()[0])
# count="a"
# for i in str:
#     count=count+1
#     print(str.count())


# total = 0
# passed = True
# grade="F"

# for i in  range(5):
#     marks = int(input("enter your marks: "))
#     total+= marks
#     if marks < 35:
#         passed = False

# percentage = total / 5

# if passed==True:
#     if percentage >= 90:
#         grade = "A+"
#     elif percentage >= 80:
#         grade = "A"
#     elif percentage >= 70:
#         grade = "B"
#     elif percentage >= 60:
#         grade = "C"
#     elif percentage >= 50:
#         grade = "D"
#     elif percentage<50:
#         grade = "F"

#     print(f"marks-{total}\nPercentage-{percentage}%\nGrade-{grade}")

# if passed:
#    print(" you're passed")
# else:
#    print("you're failed")

# for i in range(3):
#     for j in range(3):
#      print("*",end="")
#     print()

# for i in range(1,4):
#     for j in range(1,4):
#         print(j,end=" ")
#     print()

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end=" ")
#     print()

# for i in range(5):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# for i in range(5):
#     for j in range(5-i):
#         print("*",end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# tbl=int(input("enter your table: ").split()[0])
# for i in range(1,6):
#     for j in range(1,11):
#         print(f"{i}×{j}={i*j}")
#     print()

# for i in range(1,4):
#     for j in range(1,6):
#         print(i*j,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         print(j**2,end=" ")
#     print()

 
# for i in range(1,6):
#     for j in range(i):
#         print(chr(65+j), end=" ")
#     print()

# for i in range(1,6):
#     for j in range(i):
#         print(chr(64+i),end=" ")
#     print()
    

# for i in range(1,10,2):
#     for j in range(1,i+1):
#         if j%2==1:
#            print(j,end=" ")
#     print()

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j*2-1,end=" ")
#     print()


# for i in range(2,11,2):
#     for j in range(1,i+1):
#         if j%2==0:
#             print(j, end=" ")
#     print()

# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()

# for i in range(1,2):
#     for j in range(1,10):
#         if j==4 or j==7 :
#             print()
#         print(j,end=" ")
#     print()

# n=int(input("enter your number: ").split()[0])
# count=1
# for i in range(n):
#     for j in range(n):
#         print(count,end=" ")
#         count+=1
#     print()

# for i in range(1,2):
#     for j in range(1,21):
#         if j==6 or j==11 or j==16:
#             print()
#         print(j,end=" ")
#     print()

# for i in range(1,4):
#     for j in range(1,4):
#         print((i,j), end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,7-i):
#         print(j,end="")
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end="")
#     print()

# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(j,end="")
#     print()

# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i}×{j}={i*j}",sep=" ")
#     print( )

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)

