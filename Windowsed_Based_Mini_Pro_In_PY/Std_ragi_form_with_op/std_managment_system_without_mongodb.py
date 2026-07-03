#Student Managment System With Login Form
'''
Features:
Login
Add Students
View Students
Search Students
Delete Students
Exit
'''

#=======================================Import Library===================================================
import tkinter as tk
from tkinter import*
from tkinter import messagebox
'''
root = tk.Tk()
root.title("Student Managment System Without MongoDB")
root.geometry("700x500")
root.configure(bg="orchid")
root.mainloop()
'''

students=[]


#==========================================Login========================================================
def login():
    if username.get()=="admin" and password.get()=="1234":
        login_frame.pack_forget()
        main_frame.pack()
    else:
        messagebox.showerror("Error","Invalid Username Or Password!")
#==========================================Add Student========================================================
def add_student():
    name = name_entry.get()
    roll = roll_entry.get()
    course =course_entry.get()

    if name =="" or roll =="" or course =="":
        messagebox.showwarning("Warning","Fill All Fields")
        return

    students.append([roll,name,course])

    messagebox.showinfo("Success","Student Added Successfully!")

    name_entry.delete(0,END)
    roll_entry.delete(0,END)
    course_entry.delete(0,END)
#==========================================View Student========================================================
def view_student():
    listbox.delete(0,END)

    for s in students:
        listbox.insert(END,f"Roll:{s[0]} Name: {s[1]} Course: {s[2]}")

#==========================================Search Student========================================================

def search_student():
    roll = search_entry.get()

    for s in students:
        if s[0]==roll:
            messagebox.showinfo("Student",
                                f"Roll:{s[0]} Name:{s[1]} Course:{s[2]}")
            return

    messagebox.showerror("Not Found","Student Not Found")

#=========================================Delete Student========================================================

def delete_student():
    roll = search_entry.get()

    for s in students:
        if s[0]==roll:
            students.remove(s)
            messagebox.showinfo("Delete","Deleted Successfully!")
            return
    messagebox.showerror("Not Found","Student Not Found")

#=========================================Main Window====================================================
root = tk.Tk()
root.title("Student Managment System Without MongoDB")
root.geometry("700x500")
root.configure(bg="orchid")


#=========================================Login Frame=====================================================

login_frame = tk.Frame(root,bg="orchid")
login_frame.pack(pady=60)

tk.Label(login_frame,text="Login",font=("Arial",20,"bold"),bg="orchid").pack(pady=10)

tk.Label(login_frame,text="Username",bg="orchid",font=("Arial",16)).pack()
username = tk.Entry(login_frame,bg="lightyellow")
username.pack(padx=10,pady=10)

tk.Label(login_frame,text="Password",font=("Arial",16),bg="orchid").pack()
password = tk.Entry(login_frame,bg="lightyellow",show="*")
password.pack(padx=10,pady=10)

tk.Button(login_frame,text="Login",command = login,width=20,bg="red",fg="white").pack(pady=10)


#==========================================Main Frame===================================================

main_frame = tk.Frame(root,bg="lightyellow")
main_frame.pack()

tk.Label(main_frame,text="Student Ragistration Form",font=("Arial",20,"bold"),bg="lightyellow").grid(row=0,column=0,columnspan=2,pady=10)

tk.Label(main_frame,text="Roll",font=("Arial",16),bg="lightyellow").grid(row=1,column=0)
roll_entry = tk.Entry(main_frame)
roll_entry.grid(row=1,column=1)

tk.Label(main_frame,text="Name",font=("Arial",16),bg="lightyellow").grid(row=2,column=0)
name_entry = tk.Entry(main_frame)
name_entry.grid(row=2,column=1)

tk.Label(main_frame,text="Course",font=("Arial",16),bg="lightyellow").grid(row=3,column=0)
course_entry = tk.Entry(main_frame)
course_entry.grid(row=3,column=1)

# Add Student Button
tk.Button(main_frame,text="Add Student",command=add_student,width=20,bg="green",fg="white").grid(row = 4, column=0,pady=10)

# View Student Button
tk.Button(main_frame,text="View Student",command=view_student,width=20,bg="green",fg="white").grid(row = 4, column=1,pady=10)

# Search or Delete
tk.Label(main_frame,text="Seach/Delete Roll",font=("Arial",16),bg="lightyellow").grid(row=5,column=0)
search_entry = tk.Entry(main_frame)
search_entry.grid(row=5,column=1)

# Search Button
tk.Button(main_frame,text="Search Button",command=search_student,width=20,bg="green",fg="white").grid(row=6,column=0,pady=10)

# Delete Button
tk.Button(main_frame,text="Delete Button",command=delete_student,width=20,bg="green",fg="white").grid(row=6,column=1,pady=10)


#Exit Button
tk.Button(main_frame,text="Exit",command=root.destroy,width=20,bg="green",fg="white").grid(row=8,column=0,columnspan=2,pady=10)
# ListBox
listbox = tk.Listbox(main_frame,width=70,height=10)
listbox.grid(row=7,column=0,columnspan=2,pady=20)

root.mainloop()















