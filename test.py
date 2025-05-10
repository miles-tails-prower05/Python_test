from tkinter import *

root = Tk()
root.geometry("600x600")

canvas = Canvas(root, width=540, height=540)
canvas.pack()

img = PhotoImage(file="image/sumung.png")
canvas.create_image(0, 0, anchor=NW, image=img)

root.mainloop()