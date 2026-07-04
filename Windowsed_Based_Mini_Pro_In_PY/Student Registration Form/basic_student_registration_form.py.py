# Mini Project
# Create one student ragistration form

import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

root = tk.Tk()
root.iconbitmap("user_graduate_solid.ico")
root.title("Student Ragistration Form")
#root.geometry("1200x800")
root.configure(bg="lightgoldenrod")
#root.attributes("-fullscreen",True)
root.maxsize(1200,800)

img = tk.PhotoImage(file="user-graduate-solid.png")
img = img.subsample(16, 18)

output_frame = tk.Frame(root, bd=2,relief="solid",width=500,height=380,bg="ghostwhite")
output_frame.pack(padx=10,pady=10)
output_frame.pack_propagate(False)
output_frame.place(x=350,y=400)

def show_info():

    student_name = std_entry.get()
    father_name = father_entry.get()
    address = add_entry.get()
    contact_no = contact_entry.get()

    for widget in output_frame.winfo_children():
        widget.destroy()

    img_label = tk.Label(output_frame, image=img, bg="gainsboro")
    img_label.image = img          # Keep reference
    img_label.place(x=8, y=10)    

    tk.Label(output_frame,
             text="Student Ragistered Successfully!",
             font=("Arial",18,"bold"),
             justify="center",
             bg="gainsboro").pack(padx=10,pady=10)

    #tk.Label(output_frame,
     #        text=f"Student Name: {student_name}\nFather Name: {father_name}\nAddress: {address}\nContact Number: {contact_no}",
      #       justify="left",
       #      font=("Arial",20,"bold")
        #     ).place(x=10,y=100)


    
    tk.Label(output_frame,
             text=f"Student Name: {student_name}",
             font=("Arial",20,"bold"),
             bg="ghostwhite",
             justify="left"
             ).place(x=10,y=80)
    tk.Label(output_frame,
             text=f"Father Name: {father_name}",
             font=("Arial",20,"bold"),
             bg="ghostwhite"
             ).place(x=10,y=160)
    tk.Label(output_frame,
             text=f"Address: {address}",
             font=("Arial",20,"bold"),
             bg="ghostwhite"
             ).place(x=10,y=240)
    tk.Label(output_frame,
             text=f"Contact Number: {contact_no}",
             font=("Arial",20,"bold"),
             bg="ghostwhite"
             ).place(x=10,y=320)
    
    '''messagebox.showinfo(
        "Student Addmision Form",
        f"Student Name: {student_name}\n Father Name: {father_name}\n Address: {address}\n Contact No.:{contact_no}"
        )'''




    # Frame section
frame = tk.Frame(root,bd=2,relief="solid",width=500,height=380,bg="ghostwhite")
frame.pack(padx=10,pady=10)
frame.pack_propagate(False)
    # Student Name Section
img=tk.PhotoImage(file="user-graduate-solid.png")
img = img.subsample(16,18)
tk.Label(frame,image=img,bg="gainsboro").place(x=20,y=5)
tk.Label(frame,text="Student Ragistration Form",justify="center",font=("Arial",20,'bold'),bg="gainsboro").pack(pady=5)
tk.Label(frame,text="Student Name: ",font=("Arial",20,'bold'),bg="ghostwhite").place(x=10,y=60)

std_entry = tk.Entry(frame,font=("Arial",18),bg="lightyellow")
std_entry.place(x=220,y=60)
#std_entry.pack()



# Father Name Section
tk.Label(frame,text="Father Name: ",font=("Arial",20,'bold'),bg="ghostwhite").place(x=10,y=120)
father_entry = tk.Entry(frame,font=("Arial",18),bg="lightyellow")
father_entry.place(x=220,y=120)
#father_entry.pack()

# Address Section
tk.Label(frame,text="Address: ",font=("Arial",20,'bold'),bg="ghostwhite").place(x=10,y=180)
add_entry = tk.Entry(frame,font=("Arial",18),bg="lightyellow")
add_entry.place(x=220,y=180)
#add_entry.pack()

# Contact Number
tk.Label(frame,text="Contact No.: ",font=("Arial",20,'bold'),bg="ghostwhite").place(x=10,y=240)
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
# main menu
root.mainloop()
#tk.Label(root,text="Student Raagistration Form").pack()



















