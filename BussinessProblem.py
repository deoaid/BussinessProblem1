from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("Enter Title Here")

#Set size of window
root.geometry("425x550")

# Create buttons
title = Button(root, text="NoteTaker", background='white')
file = Button(root, text="File", background='white')
save = Button(root, text="Save", background='white')
newtab = Button(root, text="New Tab", background='white')



# Place widgets in window (with pack function!)
title.grid(row=0, column=0)
file.grid(row=0, column=1)
save.grid(row=0, column=2)
newtab.grid(row=0, column=3)



# Start the GUI event loop
root.mainloop()