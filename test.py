from tkinter import *
from tkmacosx import Button

root = Tk()


root.title("Creating FIle")
root.geometry("500x500")


textbox = Text(root, height=28, width=52)

def save():
	with open("text.txt", "w") as File:
		File.write(textbox.get("1.0", END))

button = Button(text="text", command=save)

textbox.pack()

button.pack()	

root.mainloop()






