student=[]
while True:
    print("""\ 1.add students
    2. view students
    3. search students
    4. exit""")
    choice=input("enter option:")
    if choice=="1":
         name=input("name:")
         age=input("age:")
         course=input("course:")
         student={
            "name":name,
            "age":age,
            "course":course
          }
         student.append(student)
         print("student added successfully")
    elif choice=="2":
            for student in student:
                print(student)
    elif choice=="3":
            search=input("enter a name:")
            for student in student:
                if student["name"]==search:
                    print(student)
    elif choice=="4":
            break
    else:
            print("wrong option")