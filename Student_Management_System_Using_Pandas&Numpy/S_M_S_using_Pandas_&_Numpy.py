# Student Managment System(Using Pandas And Numpy Laibrary)

import pandas as pd
import numpy as np
import os

FILL_NAME = "students.csv"

if os.path.exists(FILL_NAME):
    df = pd.read_csv(FILL_NAME)
else:
    df = pd.DataFrame(column=["Roll No", "Name", "Age", "Course", "Marks"])
    df.to_csv(FILL_NAME,index = False)


# Save Files
def save_files():
    df.to_csv(FILL_NAME, index =False)

# Add Students
def add_std():
    global df

    roll = int(input("Enter The Roll No"))

    if roll in df["Roll No"].values:
        print("Roll Number Already Exits!")
        return

    name = input("Enter Name:")
    age = int(input("Enter Age"))
    course = input("Enter Course Name")
    marks = float(input("Enter Marks Of Student:"))

    new_student = pd.DataFrame({
        "Roll No":[roll],
        "Name":[name],
        "Age":[age],
        "Course":[course],
        "Marks":[marks]
        })

    df = pd.concat([df,new_student],ignore_index = True)
    save_files()

    print("Student Added Successfully!")

# View Students
def view_std():

    if df.empty:
        print('No Records Found!')
    else:
        print(df)

# Search Students
def search_std():
    roll = int(input("Enter The Roll No: "))

    student =  df[df["Roll No"]== roll]

    if student.empty:
        print("Student not found!")
    else:
        print(student)

# Update Students
def update_std():
    global df

    roll = int(input("Enter The Roll No: "))

    if roll not in df["Roll No"].values:
        print("Roll Number Already Exits!")
        return

    marks = float(input("Enter New Marks:"))
    df.loc[df["Roll No"]==roll,"Marks"]=marks

    save_files()

    print("Marks Update Successfully!")

# Delete Student
def delete_std():
    global df

    roll = int(input("Enter The Roll No:"))

    if roll not in df["Roll No"].values:
        print("Roll Number Already Exits!")
        return

    df = df[df["Roll No"]!= roll]

    save_files()

    print('Student Deleted Successfully!')

# Find Topper
def find_topper_std():

    if df.empty:
        print("No Records!")
        return

    top = df[df["Marks"] == df["Marks"].max()]

    print(top)


# Average Marks
def aveg_marks_std():

    if df.empty:
        print("No Records1")
        return
    aveg = df["Marks"].mean()
    print("Average Marks Of Students:",aveg)

    
# main menu

while True:
    print("====================STUDENT MANAGEMENT SYSTEM======================\n")

    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Deleted Student")
    print("6. Find Topper")
    print("7. Average Marks")
    print("8. Exit")


    choice = input("Enter Choice:")

    if choice == "1":
        add_std()

    if choice == "2":
        view_std()

    if choice == "3":
        search_std()

    if choice == "4":
        update_std()

    if choice == "5":
        delete_std()

    if choice == "6":
        find_topper_std()

    if choice == "7":
        aveg_marks_std()

    if choice == "8":
        print("Thank You")
        break
    else:
        ("Invalid Choice!")
