# Student Ragistration Form with login Form

import tkinter as tk
from tkinter import messagebox

# ========================================Login Form============================================

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "1234":
        login_frame.pack_forget()
        ragistration_frame.pack(fill="both",expand=True)
    else:
        messagebox.showerror("Login","Invalid Username and Password")


#=========================================Show Information=======================================
def show_info():
    form = form_entry.get()
    date = date_entry.get()
    student_name = std_entry.get()
    collage_name = clg_entry.get()
    #male = gender_male.get() #--> not support .get method
    #female = gender_female.get()#--> not support .get method
    address = add_entry.get()
    contact_number = contact_entry.get()
    alternate_number = alternate_entry.get()
    email = email_entry.get()
    father_name = father_entry.get()
    occupation = father_ocuupation_entry.get()
    parets_contact_no = father_Contactno_entry.get()
    
    messagebox.showinfo("Student Ragisteration form","Student Ragistered Successfully!")
    
    

# ===========================================Main Window=========================================

root=tk.Tk()
root.title("Student Managment System")
root.minsize(1200,800)
root.maxsize(1200,800)
# readio button of gender
#male_var = tk.IntVar()
#female_var = tk.IntVar()

gender_var = tk.IntVar()
def gender_sec():
    if gender_var ==  "male":
        gender_female.config(state="disabled")
    elif gender_var == "female":
        gender_male.config(state="disabled")

# Redio Button Of Class
#FY_var = tk.IntVar()
#SY_var = tk.IntVar()
#TY_var = tk.IntVar()

class_var = tk.IntVar()
def class_sec():
    if class_var == "fy":
        class_SY.config(state="disabled")
        class_TY.config(state="disabled")
    elif class_var == "sy":
        class_FY.config(state="disabled")
        class_TY.config(state="disabled")
    elif class_var == "ty":
        class_FY.config(state="disabled")
        class_SY.config(state="disabled")


#Checkbox button Of Courses
#1st line
c_var = tk.IntVar()
core_java_var = tk.IntVar()
android_var = tk.IntVar()
wt_var = tk.IntVar()
ang_js_var = tk.IntVar()
dbms_var = tk.IntVar()
bm_var = tk.IntVar()
account_var = tk.IntVar()
ppa_var = tk.IntVar()
# 2nd line
ds_var = tk.IntVar()
adv_java_var = tk.IntVar()
core_py_var = tk.IntVar()
php_var = tk.IntVar()
node_js_var = tk.IntVar()
pdbms_var = tk.IntVar()
tcs_var = tk.IntVar()
block_chain_var = tk.IntVar()
advanced_c_var = tk.IntVar()
# 3rd Line
cpp_var = tk.IntVar()
dotnet_var = tk.IntVar()
adv_py_var = tk.IntVar()
adv_php_var = tk.IntVar()
Hadoop_var = tk.IntVar()
stats_var = tk.IntVar()
QS_var = tk.IntVar()
se_var = tk.IntVar()

# Condition Checkbox
condition_box_var = tk.IntVar()
# ==========================Login Frame===========================================================

login_frame = tk.Frame(root,bd=2,relief="solid")
login_frame.pack(pady=50)

tk.Label(login_frame,text="Login Form",font=("Arial",20,"bold")).pack(pady=20)

# Username
tk.Label(login_frame,text="Username",font=("Arial",16,"bold")).pack()
username_entry = tk.Entry(login_frame,font=("Arial",16,"bold"))
username_entry.pack(padx=20,pady=10)

# Password
tk.Label(login_frame,text="Password",font=("Arial",16,"bold")).pack()
password_entry=tk.Entry(login_frame,font=("Arial",16,"bold"),show="*")
password_entry.pack(padx=20,pady=10)

# Login Button
login_btn = tk.Button(login_frame,text="Login Button",fg="white",bg="red",command=login)
login_btn.pack(pady=20)

#=======================================Ragistration Frame==========================================

ragistration_frame = tk.Frame(root,bd=2,relief="solid",bg="ghostwhite")
ragistration_frame.pack(padx=10,pady=10)
ragistration_frame.pack_propagate(False)
# Headiing
img=tk.PhotoImage(file="user-graduate-solid.png")
img = img.subsample(16,18)
tk.Label(ragistration_frame,image=img,bg="gainsboro").place(x=20,y=5)
tk.Label(ragistration_frame,text="Student Ragistration Form",justify="center",font=("Arial",20,'bold'),bg="gainsboro").pack(pady=5)
# Form Number
tk.Label(ragistration_frame,text="Form Number: ",font=("Arial",20,'bold'),bg="ghostwhite").place(x=10,y=60)
form_entry = tk.Entry(ragistration_frame,font=("Arial",18),bg="lightyellow")
form_entry.place(x=220,y=60)

# Date
tk.Label(ragistration_frame,text="Date: ",font=("Arial",20,'bold'),bg="ghostwhite").place(x=10,y=120)
date_entry = tk.Entry(ragistration_frame,font=("Arial",18),bg="lightyellow")
date_entry.place(x=220,y=120)

# Student Name Section

tk.Label(ragistration_frame,text="Student Name: ",font=("Arial",20,'bold'),bg="ghostwhite").place(x=10,y=180)

std_entry = tk.Entry(ragistration_frame,font=("Arial",18),bg="lightyellow")
std_entry.place(x=220,y=180)
#std_entry.pack()

# College Name:

tk.Label(ragistration_frame,text="College Name: ",font=("Arial",20,'bold'),bg="ghostwhite").place(x=10,y=240)

clg_entry = tk.Entry(ragistration_frame,font=("Arial",18),bg="lightyellow")
clg_entry.place(x=220,y=240)

# Gender:
tk.Label(ragistration_frame,text="Gender: ",font=("Arial",20,'bold'),bg="ghostwhite").place(x=10,y=300)

gender_male = tk.Radiobutton(ragistration_frame,command=gender_sec,value="male",text="Male",variable = gender_var,font=("Arial",16),bg="ghostwhite")
gender_male.place(x=220,y=300)

gender_female = tk.Radiobutton(ragistration_frame,value="female",command=gender_sec,text="Female",variable = gender_var,font=("Arial",16),bg="ghostwhite")
gender_female.place(x=320,y=300)



# Address Section
tk.Label(ragistration_frame,text="Address: ",font=("Arial",20,'bold'),bg="ghostwhite").place(x=10,y=420)
add_entry = tk.Entry(ragistration_frame,font=("Arial",18),bg="lightyellow")
add_entry.place(x=220,y=420)
#add_entry.pack()

# Contact Number
tk.Label(ragistration_frame,text="Contact No.: ",font=("Arial",20,'bold'),bg="ghostwhite").place(x=10,y=480)
contact_entry=tk.Entry(ragistration_frame,font=("Arial",18),bg="lightyellow")
contact_entry.place(x=220,y=480)
#contact_entry.pack()

# Alternate Number
tk.Label(ragistration_frame,text="Alternate No.: ",font=("Arial",20,'bold'),bg="ghostwhite").place(x=10,y=540)
alternate_entry=tk.Entry(ragistration_frame,font=("Arial",18),bg="lightyellow")
alternate_entry.place(x=220,y=540)

# Email Section
tk.Label(ragistration_frame,text="Student Email: ",font=("Arial",20,'bold'),bg="ghostwhite").place(x=10,y=600)
email_entry=tk.Entry(ragistration_frame,font=("Arial",18),bg="lightyellow")
email_entry.place(x=220,y=600)

# Class:
tk.Label(ragistration_frame,text="Classes: ",font=("Arial",20,'bold'),bg="ghostwhite").place(x=10,y=660)

class_FY = tk.Radiobutton(ragistration_frame,value = "fy",text="FY",variable = class_var,font=("Arial",16),bg="ghostwhite")
class_FY.place(x=220,y=660)

class_SY = tk.Radiobutton(ragistration_frame,value = "sy",text="SY",variable = class_var,font=("Arial",16),bg="ghostwhite")
class_SY.place(x=320,y=660)

class_TY = tk.Radiobutton(ragistration_frame,value = "ty",text="TY",variable = class_var,font=("Arial",16),bg="ghostwhite")
class_TY.place(x=420,y=660)

# Father Name Section
tk.Label(ragistration_frame,text="Father Name: ",font=("Arial",20,'bold'),bg="ghostwhite").place(x=550,y=60)
father_entry = tk.Entry(ragistration_frame,font=("Arial",18),bg="lightyellow")
father_entry.place(x=900,y=60)
#father_entry.pack()


# Father Occupation
tk.Label(ragistration_frame,text="Father Occupation: ",font=("Arial",20,'bold'),bg="ghostwhite").place(x=550,y=120)
father_ocuupation_entry = tk.Entry(ragistration_frame,font=("Arial",18),bg="lightyellow")
father_ocuupation_entry.place(x=900,y=120)


# Father Name Section
tk.Label(ragistration_frame,text="Father Contact Number: ",font=("Arial",20,'bold'),bg="ghostwhite").place(x=550,y=180)
father_Contactno_entry = tk.Entry(ragistration_frame,font=("Arial",18),bg="lightyellow")
father_Contactno_entry.place(x=900,y=180)

#Chooce Course
tk.Label(ragistration_frame,text="Choise Courses ",font=("Arial",20,'bold'),bg="ghostwhite").place(x=700,y=240)
#Course Checkbutton
# C
c_entry = tk.Checkbutton(ragistration_frame,text="C",variable = c_var,font=("Arial",16),bg="ghostwhite")
c_entry.place(x=550,y=300)
# Core Java
core_java_entry = tk.Checkbutton(ragistration_frame,text="Core Java",variable = core_java_var,font=("Arial",16),bg="ghostwhite")
core_java_entry.place(x=550,y=330)
# Android
android_entry = tk.Checkbutton(ragistration_frame,text="Android",variable = android_var,font=("Arial",16),bg="ghostwhite")
android_entry.place(x=550,y=360)
# WT
wt_entry = tk.Checkbutton(ragistration_frame,text="WT",variable = wt_var,font=("Arial",16),bg="ghostwhite")
wt_entry.place(x=550,y=390)
# Angular JS
ang_js_entry = tk.Checkbutton(ragistration_frame,text="Angular JS",variable = ang_js_var,font=("Arial",16),bg="ghostwhite")
ang_js_entry.place(x=550,y=420)
# DBMS
dbms_entry = tk.Checkbutton(ragistration_frame,text="DBMS",variable = dbms_var,font=("Arial",16),bg="ghostwhite")
dbms_entry.place(x=550,y=450)
# BM
bm_entry = tk.Checkbutton(ragistration_frame,text="BM",variable = bm_var,font=("Arial",16),bg="ghostwhite")
bm_entry.place(x=550,y=480)
# Account
account_entry = tk.Checkbutton(ragistration_frame,text="Account",variable = account_var,font=("Arial",16),bg="ghostwhite")
account_entry.place(x=550,y=510)
# PPA
ppa_entry = tk.Checkbutton(ragistration_frame,text="PPA",variable = ppa_var,font=("Arial",16),bg="ghostwhite")
ppa_entry.place(x=550,y=540)
#---------------------------
# DS
ds_entry = tk.Checkbutton(ragistration_frame,text="DS",variable = ds_var,font=("Arial",16),bg="ghostwhite")
ds_entry.place(x=750,y=300)
# adv Java
adv_java_entry = tk.Checkbutton(ragistration_frame,text="Adv JAVA",variable = adv_java_var,font=("Arial",16),bg="ghostwhite")
adv_java_entry.place(x=750,y=330)
# Core Python
core_py_entry = tk.Checkbutton(ragistration_frame,text="Core Python",variable = core_py_var,font=("Arial",16),bg="ghostwhite")
core_py_entry.place(x=750,y=360)
# PHP
php_entry = tk.Checkbutton(ragistration_frame,text="PHP",variable = php_var,font=("Arial",16),bg="ghostwhite")
php_entry.place(x=750,y=390)
# Node JS
node_js_entry = tk.Checkbutton(ragistration_frame,text="Node Js",variable = node_js_var,font=("Arial",16),bg="ghostwhite")
node_js_entry.place(x=750,y=420)
# PDBMS
pdbms_entry = tk.Checkbutton(ragistration_frame,text="PDBMS",variable = pdbms_var,font=("Arial",16),bg="ghostwhite")
pdbms_entry.place(x=750,y=450)
# TCS
tcs_entry = tk.Checkbutton(ragistration_frame,text="TCS",variable = tcs_var,font=("Arial",16),bg="ghostwhite")
tcs_entry.place(x=750,y=480)
# Block Chain
block_chain_entry = tk.Checkbutton(ragistration_frame,text="Block Chain",variable = block_chain_var,font=("Arial",16),bg="ghostwhite")
block_chain_entry.place(x=750,y=510)
# Advanced C
advanced_c_entry = tk.Checkbutton(ragistration_frame,text="Advanced C",variable = advanced_c_var,font=("Arial",16),bg="ghostwhite")
advanced_c_entry.place(x=750,y=540)
#----------------------------
# C++
cpp_entry = tk.Checkbutton(ragistration_frame,text="C++",variable = cpp_var,font=("Arial",16),bg="ghostwhite")
cpp_entry.place(x=950,y=300)
# .NET
dotnet_entry = tk.Checkbutton(ragistration_frame,text=".NET",variable = dotnet_var,font=("Arial",16),bg="ghostwhite")
dotnet_entry.place(x=950,y=330)
# Adv Python
adv_py_entry = tk.Checkbutton(ragistration_frame,text="Advance Python",variable = adv_py_var,font=("Arial",16),bg="ghostwhite")
adv_py_entry.place(x=950,y=360)
# Adv PHP
adv_php_entry = tk.Checkbutton(ragistration_frame,text="Advance PHP",variable = adv_php_var,font=("Arial",16),bg="ghostwhite")
adv_php_entry.place(x=950,y=390)
# Hadoop(Big Data)
hadoop_entry = tk.Checkbutton(ragistration_frame,text="Hadoop",variable = Hadoop_var,font=("Arial",16),bg="ghostwhite")
hadoop_entry.place(x=950,y=420)
# Stats
stats_entry = tk.Checkbutton(ragistration_frame,text="Stats",variable = stats_var,font=("Arial",16),bg="ghostwhite")
stats_entry.place(x=950,y=450)
# QS(sys prq)
QS_entry = tk.Checkbutton(ragistration_frame,text="QS(SYS PRQ)",variable = QS_var,font=("Arial",16),bg="ghostwhite")
QS_entry.place(x=950,y=480)
# SE
se_entry = tk.Checkbutton(ragistration_frame,text="SE",variable = se_var,font=("Arial",16),bg="ghostwhite")
se_entry.place(x=950,y=510)

# Note Label
tk.Label(ragistration_frame,text="NOTE:DOCUMENT--> Zerox Copy Of Adhar Card",font=("Arial",12,"bold"),bg="ghostwhite").place(x=550,y=580)
# Condition check box
tk.Checkbutton(ragistration_frame,
               text="I am Accept term and condition below",
               font=("Arial",12,"bold"),
               bg="ghostwhite",
               variable = condition_box_var).place(x=550,y=600)

tk.Label(
    ragistration_frame,
    text="1) Once the Admission taken cannot cancel",
    font=("Arial",12,"bold"),
    bg="ghostwhite",).place(x=550,y=630)

tk.Label(
    ragistration_frame,
    text="2) Fees once paid cannot refunded",
    font=("Arial",12,"bold"),
    bg="ghostwhite",).place(x=900,y=630)

# sign:
# student Sign
tk.Label(ragistration_frame,text="Student Sign: ",font=("Arial",12),bg="ghostwhite").place(x=550,y=685)

std_sign_entry = tk.Entry(ragistration_frame,font=("Arial",12),bg="lightyellow")
std_sign_entry.place(x=650,y=685)

#Cordinator Sign
tk.Label(ragistration_frame,text="Cordinator Sign: ",font=("Arial",12),bg="ghostwhite").place(x=870,y=685)

std_sign_entry = tk.Entry(ragistration_frame,font=("Arial",12),bg="lightyellow")
std_sign_entry.place(x=990,y=685)
# Submit Button
btn = tk.Button(
    ragistration_frame,
    text="Submit",
    font=("Arial",16,"bold"),
    bg="green",
    fg="white",
    command=show_info
    )
btn.place(x=500,y=720)
root.mainloop()
        
