# string
text="python"
print(text[0])
print(text[3])
print(text[-1])
print(text[-2])

text="programming"
print(text[0:4])
print(text[3:8])
print(text[:5])
print(text[5:])

text="python"
print(text[::2])
print(text[1::2])
print(text[::-1])

text="Hello World"
print(len(text))
print(text[5])
print(text[-1])

name="sanjana singh"
city='Patna'
favorite_programming_language="python"
message='hi everyone'
print(name,city,favorite_programming_language,message)

text=""
print(text,(type)(text),len(text))

text="python programming"
print(len(text))
print(text)
print(text[0])
print(text[5])
print(text[2])
print(text[17])

text="programming"
print(text[0])
print(text[1])
print(text[4])
print(text[10])

print(text[-1])
print(text[-2])
print(text[-3])
print(text[-11])

name="sanjana singh"
print(name[0])
print(name[7])
print(name[9])

text="python programming"
print(text[0:6])
print(text[7:11])
print(text[0:11])
print(text[0:5])
print(text[::2])
print(len(text))
text="python"
print(text[0:0:-1])
print(text[1:5])
print(len(text))
a="sanjana"
b=" singh"
print(a+b)
name="sanjana"
age=20
city="patna"
programming_language="python"
print(f"my name is {name}, my age is {age}, i live in {city}, my favorite programming language is {programming_language}")
a="python"
b=5
print(a+str(b))
a="s"
print(a*5)
print(a*3)
a="*"
print(a*5)
text="python programming"
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.swapcase())
a="Python"
b="python"
c=a.lower()==b
print(c)
a="python is a programming language"
print("python" in a)
print("programming" in a)
print("java" in a)
print("language" in a)
print(a.find("python"))
print(a.find("programming"))
print(a.find("java"))
print(a.find("language"))
a="banana"
print(a.count("a"))
print(a.count("b"))
print(a.count("n"))
filename="student_notes.pdf"
print(filename.startswith("student"))
print(filename.endswith(".pdf"))
print(filename.endswith(".txt"))
a="I am learning Java"
print(a.replace("Java","python"))
a="apple apple apple"
print(a.replace("apple","banana"))
print(a.replace("apple","banana",1))
text="python"
a=text.upper()
print(text)
print(a)
text=" python programming "
print(text.strip())
print(text.lstrip())
print(text.rstrip())


