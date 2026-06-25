#Mini Project
students = []
# Add Student Info
def add_student():
    roll =  int(input("Enter the Roll No."))
    name = input("Enter the name:")
    age = int(input("Enter The Age"))

    student = {
        "roll":roll,
        "name":name,
        "age":age
        }
    students.append(student)
    print("Student Added Successfully!")

# View Students
def view_students():
    if len(students) == 0:
        print("No Students Found!")
    else:
        print("\nStudent Records")
        print("-" * 30)
        for student in students:
            print("Roll No:", student["roll"])
            print("Name   :", student["name"])
            print("Age    :", student["age"])
            print("-" * 30)
      
# Search Student
def search_student():
    roll = int(input("Enter Roll No to Search:"))
    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found")
            print("Roll No:", student["roll"])
            print("Student Name:", student["name"])
            print("Student Age:", student["age"])
            return
        
    print("Student Not Found")

# Update Student
def update_student():
    roll = int(input("Enter Roll no To Update:"))

    for student in students:
        if student["roll"] == roll:
            student["name"] = input("Enter New Name")
            student["age"] = int(input("Enter New Age"))
            print("Student Update Successfully")
            return
    print("Student Not Found")

# Delete Student
def delete_student():
    roll = int(input("Enter Roll No To Delete:"))

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student Deleted Successfully")
            return
    print("Student Not Found")


# main menu
while True:
    print("\n=======STUDENT MANAGMENT SYSTEM=========")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice =  int(input("Enter Your Choice:"))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_student()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")








    
