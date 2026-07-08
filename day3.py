# List are mutable 
# Tuples are immutable

# student=("ram","sam","bheem")
# print(student )

# marks=("10","20","30")
# print(marks [2])

# subjects=("c","maths","python","java")
# print(subjects[-3])

# data=(1,2,3)
# data[0]=20
# print(data)# immutable we cannot change the data in tuples.

# x=(1,2,3,2,4,4,1,1,1)
# print(x.count(2))
# print(x.count(4))
# print(x.count(1))
# print(x.count(3))
# x[2]=4 #immutable,cannot be changed
# print(x)

# subjects=("c","maths","python","java","c","java","maths","java","c") #strings
# print(subjects.count("c"))
# print(subjects.count("java"))
# print(subjects.count("maths"))
# print(subjects.count("python"))
# print(subjects [4])

# num=(10,20,30,40,50)#tuple slicing
# print(num[1:4])

#sets: remove duplicate values ,store unique vaules 
# x={1,2,3,4,1,1,1}
# print(x)

# sets are mutable
# x={1,2,3,4}
# x.add(5)
# print(x)

# x={10,20,30,60}
# x.remove(30)
# print(x)

# a={1,2,3,4}
# b={5,6}
# print(a|b)#union of sets

# a={1,2,3,4,5}
# b={5,6,1}
# print(a & b)#intersection of sets: combines the common value in set

#Functions: is a block of code which performs a specific task.
# def greeting():
#     print("hello students")
# greeting()   

# def add():#function return call
#     return 10+20
# result=add()
# print(result)

# def add():
#     return ("rasam"+"rice")
# result=add()
# print(result)
  
# def num():
#     num=int(input("enter number:"))
#     if num % 2 ==0:
#         return ("even")
#     else:
#         return("odd")
# result=num()
# print(result)

#function with arguments
# def add(a,b):
#     print(a+b)
# add(10,20)

# def add(*numbers):
#     print(numbers)
# add(10,20,30,40,50,60)

# def student(name,course):
#     return student("name","course")
# name=input("enter a name:")
# course=input("enter a course:")
# print(student)

# def student(**details):
#     print(details)

# student(
#         name="penga",
#         age=21,
#         job="sales"
#     )

# def square(x):
#     return x*x
# print(square(9))

# square=lambda x:x*x
# print(square(25))

# add=lambda a,b:a+b
# print(add(10,20))

# x=int(input("enter a number:"))
# num=lambda x:"even" if x % 2==0 else "odd"
# print(num(x))

# name=lambda x:x.upper()
# print(name("Nisha"))

# name=lambda x:x.lower()
# print(name("Nisha"))

# name=lambda text:len(text)
# print(name("nisha"))

# File handling: which reads,creates,opening,modify writing a file within a program
# #  example:
# file=open("student.txt","w")
# file.write("hello world")
# file.close()

# print("data written successfully")

# file=open("student.txt","r")
# data=file.read()
# print(data)
# file.close()

# file=open("student.txt","a")
# data=file.write("\nhello universe")
# file.close()
# print("Data is appended sucesfully")

# file=open("student.txt","r")
# data=file.read()
# file.close()
# try:
#     a=10
#     b=0
#     print(a/b) 
# except:
#     print("something went wrong")

# try:
#     num=int(input("enter a number"))
#     print(num)
# except ValueError:
#     print("only number allowed")
# try:
#     a=int(input("enter a number:"))
#     b=int(input("enter a number:"))
#     print(a/b)
# except ZeroDivisionError:
#     print("cannnot divide zero")
# except ValueError:
#     print("enter only numbers")
# try:
#     file=open("data.txt")
#     print("file.read()")
# except:
#     print("file error")
# finally:
#     print("file not found")
# else block
try:
    print(10/2)
except:
    print("error")
else:
    print("success")
