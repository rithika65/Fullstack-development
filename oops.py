# class student:#class name
#     name="rishika"#attribute
#     def study(self):#represent current object
#         print("rishika is studying")
# s1=student()
# print(s1.name)
# s1.study()# study is a method

# class student:
#     name="rishika"
#     def details(self):
#         print("had breakfast")
# s1=student()
# print(s1.name)
# s1.details()
# student.details(s1)

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s1=student("rishika",22)
# s2=student("rithika",21)
# s3=student("harshitha",18)
# print(s1.name,s1.age)
# print(s2.name,s2.age)
# print(s3.name,s3.age)
#methods
# class bank:
#     def __init__(self,balance):
#         self.balance=balance
#     def check_balance(self):
#         print(self.balance)
# account=bank(5000)
# account.check_balance()

# class user:
#     def __init__(self,name,password):
#         self.name=name
#         self.password=password
#     def login(self):
#         print(self.name,self.password ,"logged in")
# user1=user("rithika","admin@123")
# user1.login()


# class user:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         name=input("enter a name:")
#         age=int(input("enter a age:"))
#     def details(self):
#         print(self.name,self.age)   
# user1=user(self,name,age)
# print(self.name)
# print(self.age) 
# user1.details()



# class a:
#     def __init__(self,num):
#         self.num=num
# b=a(6+6)
# print(b.num)

# class father:
#     def house(self):
#         print("father as a house")
# class son(father):
#     def bike(self):
#         print("son has abike")
# s=son()
# s.house()
# s.bike()
# class frog:
#     def grasshopper(self):
#         print("grasshopper is eaten by frog")
# class snake:
#     def frog(self):
#         print("frog is eaten by snake")
# class eagle:
#     def snake(self):
#         print("snake is eaten by eagle")
# class lion(frog,snake,eagle):
#     def deer(self):
#         print("deer is eaten by lion")
# foodchain=lion()
# foodchain.grasshopper()
# foodchain.frog()
# foodchain.snake()
# foodchain.deer()                                                                                                                                                                                                                                                



# class dad:
#     def house(self):
#         print("has a house")
# class daugther(dad):
#     def company(self):
#         print("she has a company")
# class son(dad):
#     def car(self):
#         print("he has a car")
# inheritance=son()

# inheritance.house()
# inheritance=daugther()

# inheritance.house()

# class appa:
#     def house(self):
#         print("appa has a house")
# class amma:
#     def land(self):
#         print("amma has a land")
# class son(appa,amma):
#     def bike(self):
#         print("has abike")
# assests=son()
# assests.house()
# assests.land()
# assests.bike()


######################used for readable object output####################
# class student:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return self.name
# s=student("king")
# print(s)
# def login(func):
#     def wrapper():
#         func()
#     return wrapper
# @login
# def dashboard():
#     print("welcome")
# dashboard()
# def name():
#     print("rithika b")
# name()
# def password():
#     print("admin@123")
# password()
# print("logged in succesfully")

# def message(func):
#     def wrapper():
#         print("function started")
#         func()
#         print("function ended")
#     return wrapper
# @message
# def hello():
#     print("hello world")

# import json
# student={
#     "name":"nisha",
#     "age":22
# }
# data=json.dumps(student)
# print(data)

# import json
# data='{"name":"rishi","age":22}'
# result=json.loads(data)
# print(result["name"])
# print(result["age"])

# import requests
# response=requests.get(
#     "https://github.com/users/python"
# )
# data=response.json()
# print(data)


















