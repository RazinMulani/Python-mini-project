# Student Ragistration Form (Windows Based Application Using MongoDB)

# python library
from pymongo import MongoClient
import tkinter as tk
from tkinter import*
from tkinter import messagebox

#mongodb connectivity
client = MongoClient("mongodb://localhost:27017/")

db = client["Students"]
student = db["student"]
users = db["user"]

#=================================Functions=====================================
#=================================Login Function=====================================

def login():

    username = entry_username.get()
    password = entry_password.get()
    users.insert_one({
    "username":"admin",
    "password":"1234"
    })

    user = users.find_one({"username": username,"password": password})

    if user:
        login_frame.pack_forget()
        main_frame.pack()
        messagebox.showinfo("Success","Login Successful")
        
    else:
        messagebox.showerror("Error","Invalid Username or Password")

#=================================Add Student=====================================
def add_student():
    roll = roll_entry.get()
    name = name_entry.get()
    course = course_entry.get()

    if roll == "" or name == "" or course == "":
        messagebox.showerror("Error","All Field Required")
    else:
        student.insert_one(
            {
                "roll":roll,
                "name":name,
                "course":course
             }
            )
    messagebox.showinfo("Add Data","Add Student Data Successfully!")

#=================================View Student=====================================


def view_student():
    listbox.delete(0,END)
    roll = roll_entry.get()
    name = name_entry.get()
    course = course_entry.get()

    data = student.find()

    for s in data:
        listbox.insert(
            END,
            f"Roll: {s['roll']}    Name: {s['name']}    Course: {s['course']}"
        )

#=================================Search Student=====================================

def search_student():
    roll = search_entry.get()

    data = student.find_one({"roll":roll})

    if data:
        messagebox.showinfo("Student",f"Roll:{data["roll"]} Name:{data["name"]} Course:{data["course"]}")
        return
    else:
        messagebox.showerror("Not Found","Student Not Found")


#=================================Delete Student=====================================

def delete_student():
    roll =search_entry.get()
    data = student.find_one({"roll":roll})
    

    if data:
        student.delete_one({"roll":roll})
        messagebox.showinfo("Student",f"Roll:{data["roll"]} Name:{data["name"]} Course:{data["course"]}")
        return
    else:
        messagebox.showerror("Not Found","Student Not Found")
        
#=================================Main Window=====================================
        
root=tk.Tk()
root.title("Student Ragistration Form Using MongoDB")
root.geometry("700x500")
root.configure(bg="orchid")

#=================================Login Frame=====================================
login_frame = tk.Frame(root,bg="orchid")
login_frame.pack(pady=100)

tk.Label(login_frame,text="User Login",bg="orchid",font=("Arial",20,"bold")).pack(pady=10)

tk.Label(login_frame,text="Username",bg="orchid",font=("Arial",16)).pack(pady=10)
entry_username = tk.Entry(login_frame)
entry_username.pack(pady=10)

tk.Label(login_frame,text="Password",bg="orchid",font=("Arial",16)).pack(pady=10)
entry_password = tk.Entry(login_frame,show="*")
entry_password.pack(pady=10)

tk.Button(login_frame,text="Login",bg="red",fg="white",width=20,command=login).pack(pady=10)

#=================================Main Frame=====================================
main_frame = tk.Frame(root,bg="lightyellow")
# Label oF Student Ragistrartion Form
tk.Label(main_frame,text="Student Ragistration Form",bg="lightyellow",font=("Arial",20,"bold")).grid(row=0,column=0,columnspan=2,pady=10)

# Roll, Name, Course details
tk.Label(main_frame,text="Roll No:",font=("Arial",16),bg="lightyellow").grid(row=1,column=0)
roll_entry = tk.Entry(main_frame)
roll_entry.grid(row=1,column=1)

tk.Label(main_frame,text="Name:",font=("Arial",16),bg="lightyellow").grid(row=2,column=0)
name_entry = tk.Entry(main_frame)
name_entry.grid(row=2,column=1)

tk.Label(main_frame,text="Course:",font=("Arial",16),bg="lightyellow").grid(row=3,column=0)
course_entry = tk.Entry(main_frame)
course_entry.grid(row=3,column=1)

# Add Button
tk.Button(main_frame,command=add_student,text="Add Student",width = 20,bg="blue",fg="white").grid(row=4,column=0,pady=10)

#View Button
tk.Button(main_frame,command=view_student,text="View Student",width = 20,bg="blue",fg="white").grid(row=4,column=1,pady=10)

#Search Button
tk.Label(main_frame,text="Search/Delete",bg="lightyellow",font=("Arial",16)).grid(row=5,column=0,pady=10)
search_entry=tk.Entry(main_frame)
search_entry.grid(row=5,column=1,pady=10)
tk.Button(main_frame,text="Search Student",width = 20,bg="blue",fg="white",command=search_student).grid(row=6,column=0,pady=10)
# Delete Button
tk.Button(main_frame,text="Delete Student",width = 20,bg="blue",fg="white",command=delete_student).grid(row=6,column=1,pady=10)

# Listbox for showing Store Data
listbox = tk.Listbox(main_frame,width=70,height=10)
listbox.grid(row=7,column=0,columnspan=2,pady=10)

#Exit Button
tk.Button(main_frame,text="Exit",width = 20,bg="blue",fg="white",command=root.destroy).grid(row=8,column=0,columnspan=2,pady=10)
root.mainloop()

