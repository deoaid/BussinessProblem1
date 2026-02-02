from tkinter import *
from tkmacosx import Button


with open("text.txt", "r") as File:
	textsave = File.read()


root = Tk()

print(textsave)
root.title("Creating File")
root.geometry("500x500")


textbox = Text(root, height=28, width=52)

def save():
	with open("text.txt", "w") as File:
		File.write(textbox.get("1.0", END))

textbox.insert(END, textsave)


button = Button(text="Save", command=save)

textbox.pack()

button.pack()	

root.mainloop()






