from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("Enter Title Here")

#Set size of window
root.geometry("300x150")

# Create buttons
title = Button(root, text="NoteTaker", background='white')
file = Button(root, text="File", background='white')
save = Button(root, text="Save", background='white')
newtab = Button(root, text="New Tab", background='white')



# Place widgets in window (with pack function!)
title.grid(row=0, collumn=0)
file.grid(row=1, collumn=0)
save.grid(row=2, collumn=0)
newtab.grid(row=3, collumn=0)



# Start the GUI event loop
root.mainloop()