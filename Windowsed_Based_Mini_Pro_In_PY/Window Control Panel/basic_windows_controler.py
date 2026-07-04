# Window Control Pannel
# Practice Question

# Requirements
'''
1. ✅✅
Set the title to "Window Control Panel".
Set the initial size to 700x500.
Set the background color to any color you like.

'''

import tkinter as tk
root = tk.Tk()
# Set the title
root.title("Window Control Pannel")
# Set initial size
root.geometry("700x500")
# Set BG
root.configure(bg="lightblue")

root.mainloop()
'''
2.
Disable resizing.
Set a minimum size of 500x400.
Set a maximum size of 900x700.
'''

import tkinter as tk
root=tk.Tk()

root.resizable(True,True)
root.minsize(500,400)
root.maxsize(900,700)


root.mainloop()

'''
3.

