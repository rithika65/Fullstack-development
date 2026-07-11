# product_price = 5000
# delivery_charges = 100
# total=product_price+delivery_charges
# print(total)

# product_price = 5000
# delivery_charges = 100
# total=product_price-delivery_charges
# print(total)

# product_price = 5000
# delivery_charges = 100
# total=product_price*delivery_charges
# print(total)

# product_price = 5000
# delivery_charges = 100
# total=product_price/delivery_charges
# print(total)

product_price = 5000
delivery_charges = 100
total=product_price//delivery_charges
print(total)

product_price = 5000
delivery_charges = 100
total=product_price**delivery_charges
print(total)

product_price = 5000
delivery_charges = 100
total=product_price%delivery_charges
print(total)

#arthimetic operators
a=15
b=5
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a/b)
print(a//b)# floating division
print(a%b)
# floating division
a=15
b=10
print(a//b)

####### assignment operators ##########

followers=100
followers -= 1
print(followers)

 #######comparison operator########
saved_password="abc"
entered_password="abc"
print(saved_password==entered_password)

#######logical operators##########
balance = 500
pin_correct=True
if balance >= 100 and pin_correct:
    print("withdraw allowed")
else:
    print("failed")

# billing details
username=input("enter username:")
product=input("enter product:")
product_price=int(input("enter the price:"))
delivery_price=int(input("enter the delivery price:"))
gst_rate=int(input("enter the gst rate:"))
quantity=int(input("enter the number of quantity:"))
print("username:",username)
print("product:",product)
print("product_price:",product_price)
print("delivery_price:",delivery_price)
print("gst_rate:",gst_rate)
print("quantity:",quantity)
total=product_price+delivery_price+gst_rate
print("the total is: ",total)
if total >=100:
    print("Discount")
else:
    print("Invalid")
print("----------Happy Coding-----------")


product_price=500
delivery_price=50
gst_rate=10
platform_fee=0
total=product_price+delivery_price+gst_rate+platform_fee
print( "the total is:",total)
if total >=100:
    print(True)
else:
    print(False)

# conditional statements
password=input("enter the password:")
if password=="admin@123":
    print("welcome")
else:
    print("invalid password")



age=35
if age >= 60:
    print("senior")
else:
    print("adult")

marks=int(input("enter the marks:"))
if marks >=90:
    print("A Grade")
elif marks >=75:
    print("B Grade")
elif marks >=50:
    print("c Grade")
else:
    print("fail")

subject=input("enter the subject:")
marks=int(input("enter the marks:"))
if  marks >=90:
    print("A Grade")
elif marks >=75:
    print("B Grade")
elif marks >=50:
    print("c Grade")
else:
    print("fail")

age=25
salary=70000
if age>=25 and salary>=50000:
    print("loan approved")
else:
    print("loan not approved")

age=25
salary=70000
if age>=25|salary>=50000:
    print("loan approved")
else:
    print("loan not approved")


login=True
if not login:
    print("print login")

pin="admin@123"
pin=input("enter the pin:")
if pin=="admin@123":
    print("correct")
else:
    print("invalid pin")
ask_amount=50000
print("the amount is:",ask_amount)
withdraw=ask_amount-500
print("check balance : ",withdraw)

def withdraw_money():
    pin=input("enter pin")
    if pin == '1234':
        amount=int(input("enter amount:"))
        balance=10000
        if amount <= balance:
            balance=balance-amount
            if amount <=balance:
                print("withdraw succesful")
                print("remaining balance:",balance)
            else:
                 print("insufficient successful")
        else:
            print("wrong pin")
withdraw_money()

Loops 
for i in range(5):
    print("hello world!")

users=["abc","cde","efg"]
for users in users:
    print("mesage sent to",users)
for i in range(2,6):
    print("hello world!")
name="dhoni"
for ch in name:
    print(ch)
### whole loop
count=1
while count <=5:
    print(count)
    count +=1
for i in range(10):
    if i==5:
        continue
    print(i)
password=""
while password!="1234":
    password=input("enter password")
    print("login success")
students=["ram","sam","spruthi"]
students.append("alex")
print(students)
students=["ram","sam","spruthi","alex"]
students.remove("sam")
print("students")