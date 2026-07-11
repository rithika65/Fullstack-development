#######encapsulation######## wrapping of the data in single unit and controlling  access of th data
# class bank:
#     def __init__(self):
#         self.balance=10000
# account=bank()
# account.balance=10000000
# print(account.balance)

# class bank:
#     def __init__(self):
#         self.__balance=10000
#     def deposit(self,amount):
#         self.__balance += amount
#     def show_balance(self):
#         print(self.__balance)
# account=bank()
# account.deposit(5000)
# account.show_balance()

#####getter#########
# class employee:
#     def __init__(self,salary):
#         self.__salary=salary
#     def get_salary(self):
#         return self.__salary
# emp=employee(356767)
# print(emp.get_salary())

# class employee:
#     def __init__(self,salary):
#         self.__salary=salary
#     def set_salary(self):
#         return self.__salary
# emp=employee(356767)
# print(emp.set_salary())

# class employee:
#     def __init__(self):
#         self.__salary=0
#     def set_salary(self,amount):
#         if amount > 0:
#             self.__salary=amount
#         else:
#             print("invalid salary")
#     def get_salary(self):
#         return self.__salary
# emp=employee()
# emp.set_salary(1234434)
# print(emp.get_salary())
########## polymorphism###########
# class dog:
#     def sound(self):
#         print("boew boew")
# class cat:
#     def sound(self):
#         print("meow meew")
# class cow:
#     def sound(self):
#         print("MOOO moo")
# class donkey:
#     def sound(self):
#         print("rakshitha")
# Dog=dog()
# Cat=cat()
# Cow=cow()
# Donkey=donkey()
# Dog.sound()
# Cat.sound()
# Cow.sound()
# Donkey.sound()

# class bus:
#     def transport(self):
#         print("bmtc")
# class flight:
#     def transport(self):
#         print("indigo")
# class metro:
#     def transport(self):
#         print("namma metro")
# class cruise:
#     def transport(self):
#         print("titanic")
# class car:
#     def transport(self):
#         print("BMW")
# class bike:
#     def transport(self):
#         print("gt")
# Bus=bus()
# Flight=flight()
# Metro=metro()
# Cruise=cruise()
# Car=car()
# Bike=bike()
# Bus.transport()
# Flight.transport()
# Metro.transport()
# Cruise.transport()
# Car.transport()
# Bike.transport()

######Abstraction method######## hiding  internal  implementation and showing only necessary feature to the user 
# from abc import ABC, abstractmethod
# class vehicle(ABC):
#     def start(self):
#         pass 
# class car(vehicle):
#     def start(self):
#         print("car started")
# car=car()
# car.start()

# from abc import ABC, abstractmethod
# class animal(ABC):
#     def sound(self):
#         pass
# class cow(animal):
#     def sound(self):
#         print("Mooo")
# class cat(animal):
#     def sound(self):
#         print("meow meow")
# class dog(animal):
#     def sound(self):
#         print("boew boew")
# class duck(animal):
#     def sound(self):
#         print("quack quack")
# cow=cow()
# cat=cat()
# dog=dog()
# duck=duck()

# cow.sound()
# cat.sound()
# dog.sound()
# duck.sound()