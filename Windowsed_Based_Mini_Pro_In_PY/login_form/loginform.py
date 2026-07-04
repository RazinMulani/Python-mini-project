# Login Form
import tkinter as tk
from tkinter import messagebox

def login_form():
    username = user_entry.get()
    password = pass_entry.get()

    messagebox.showinfo(
        "Login",
        f"Username: {username}\nPassword: {password}"
        )

root = tk.Tk()
root.title("Mini Login Form")
root.geometry("600x400")
root.configure(bg="lightblue")

frame = tk.Frame(root,bd=2,relief="solid",width=600,height=300)
frame.pack()

label_user=tk.Label(frame,text="Username:",font=("Arial",20,"bold"),bg="lightblue",justify="center")
label_user.place(x=10,y=10)

#label_user.pack()

user_entry = tk.Entry(frame,width=25,font=("Arial",20),bg="lightyellow",justify="center")
user_entry.place(x=200,y=10)
#user_entry.pack()

label_pass = tk.Label(frame,text="Password:",font=("Arial",20,"bold"),bg="lightblue",justify="center")
label_pass.place(x=10,y=100)
#label_pass.pack()

pass_entry = tk.Entry(frame,width=25,font=("Arial",20),bg="lightyellow",show="*",justify="center")
pass_entry.place(x=200,y=100)
#pass_entry.pack()

btn = tk.Button(
    frame,
    text="login",
    font=("Arial",
    10,"bold"),
    relief="solid",
    bg="black",
    fg="white",
    command=login_form,
    width = 25,
    justify = "center")
btn.place(x=150,y=180)
#btn.pack(pady=10)
root.mainloop()
