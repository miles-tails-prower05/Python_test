from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("이미지 출력 테스트")
root.configure(bg="white")

icon = PhotoImage(file='image/sumung.png')
root.iconphoto(True, icon)

canvas = Canvas(root, width=540, height=540)
canvas.pack()

img = PhotoImage(file="image/sumung.png")
canvas.create_image(0, 0, anchor=NW, image=img)

root.mainloop()