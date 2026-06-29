# Mini Project
# Create one student ragistration form

import tkinter as tk
from tkinter import messagebox

def show_info():

    student_name = std_entry.get()
    father_name = father_entry.get()
    address = add_entry.get()
    contact_no = contact_entry.get()
    
    messagebox.showinfo(
        "Student Addmision Form",
        f"Student Name: {student_name}\n Father Name: {father_name}\n Address: {address}\n Contact No.:{contact_no}"
        )

root = tk.Tk()
root.title("Student Ragistration Form")
root.geometry("700x500")
root.configure(bg="lightblue")

# Frame section
frame = tk.Frame(root,bd=2,relief="solid",width=500,height=380,bg="lightblue")
frame.pack(padx=10,pady=10)
frame.pack_propagate(False)
# Student Name Section
tk.Label(frame,text="Student Ragistration Form",justify="center",font=("Arial",20,'bold')).pack(pady=5)
tk.Label(frame,text="Student Name: ",font=("Arial",20,'bold'),bg="lightblue").place(x=10,y=60)

std_entry = tk.Entry(frame,font=("Arial",18),bg="lightyellow")
std_entry.place(x=220,y=60)
#std_entry.pack()

# Father Name Section
tk.Label(frame,text="Father Name: ",font=("Arial",20,'bold'),bg="lightblue").place(x=10,y=120)
father_entry = tk.Entry(frame,font=("Arial",18),bg="lightyellow")
father_entry.place(x=220,y=120)
#father_entry.pack()

# Address Section
tk.Label(frame,text="Address: ",font=("Arial",20,'bold'),bg="lightblue").place(x=10,y=180)
add_entry = tk.Entry(frame,font=("Arial",18),bg="lightyellow")
add_entry.place(x=220,y=180)
#add_entry.pack()

# Contact Number
tk.Label(frame,text="Contact No.: ",font=("Arial",20,'bold'),bg="lightblue").place(x=10,y=240)
contact_entry=tk.Entry(frame,font=("Arial",18),bg="lightyellow")
contact_entry.place(x=220,y=240)
#contact_entry.pack()

# Submit Button
btn = tk.Button(
    frame,
    text="Submit",
    font=("Arial",16,"bold"),
    bg="green",
    fg="white",
    command=show_info
    )
btn.place(x=150,y=300)
#btn.pack()
root.mainloop()
