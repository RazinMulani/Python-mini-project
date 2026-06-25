# Student Login Form, Change Password, and Logout Section.

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")

db = client["student_db"]

users_collection = db["users"]

students_collection = db["students"]

#print(client.list_database_names())

#Get Username and Password
def create_new_acc():
    print("Create New Account")
    print("Enter The Username and Password")
    username =  input("Enter The Username")
    password = input("Enter The Password")

    if users_collection.find_one({"username":username}) is None:
        users_collection.insert_one({
            "username":username,
            "password":password
            })
        print("User Registered Successfully")
    else:
        print("Username Already Exists")


#create_new_acc()

is_logged_in = False

# Create Login Form

def login():
    global is_logged_in

    username = input("Enter Username")
    password = input("Enter Password")

    user = users_collection.find_one({
        "username":username,
        "password":password
        })

    if user:
        is_logged_in = True
        print("login successfully!")
    else:
        print("Invalid username and password")

#login()

# logout function
def logout():
    global is_logged_in
    is_logged_in = False

    print("Logged Out Successfully!")

#logout()

# Add user
def add_student():
    roll = int(input("Roll No: "))
    name = input("Name: ")
    age = int(input("Age: "))

    students_collection.insert_one({
        "roll": roll,
        "name": name,
        "age": age
    })

    print("Student Added Successfully!")

# View User
def view_students():
    data = students_collection.find()

    print("\nStudent Records")

    for s in data:
        print(
            s["roll"],
            s["name"],
            s["age"]
        )

# Search User

def search_student():
    roll = int(input("Enter Roll No: "))

    student = students_collection.find_one({
        "roll": roll
    })

    if student:
        print(student["roll"])
        print(student["name"])
        print(student["age"])
    else:
        print("Student Not Found")

#Update Student
def update_student():
    roll = int(input("Enter Roll No: "))

    name = input("New Name: ")
    age = int(input("New Age: "))

    result = students_collection.update_one(
        {"roll": roll},
        {
            "$set": {
                "name": name,
                "age": age
            }
        }
    )

    if result.modified_count:
        print("Student Updated")
    else:
        print("Student Not Found")


#Delete Student
def delete_student():
    roll = int(input("Enter Roll No: "))

    result = students_collection.delete_one({
        "roll": roll
    })

    if result.deleted_count:
        print("Student Deleted")
    else:
        print("Student Not Found")

# Password Change
def change_pass():
    username = input("Enter The Username: ")
    old_pass = input("Enter The Old Password: ")

    user = users_collection.find_one({
        "username":username,
        "password":old_pass
        })

    if user:
        new_pass = input("Enter The New Password: ")
        confirm_pass = input("Confirm New Password: ")

        if new_pass == confirm_pass:
            users_collection.update_one({"username": username},{"$set": {"password": new_pass}})
            print("Password Change Successfully!")
        else:
               print("Passwords Do Not Match!")
    else:
            print("Invalid Username or Old Password!")
# Drop table
def drop_user_table():
    db.users.drop()
    print("Deleted All Data Successflly!")

#Main Menu
while True:

    if not is_logged_in:
        print("\n1. Create Account")
        print("2. Login Account")
        print("3. Deleted all users data")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:
            create_new_acc()

        elif choice == 2:
            login()
        elif choice == 3:
            drop_user_table()
        elif choice == 4:
            break

    else:
        print("\n===== STUDENT MANAGEMENT SYSTEM=====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Change Password")
        print("7. Logout")

        choice = int(input("Choice: "))

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
           change_pass()

        elif choice == 7:
           logout()

