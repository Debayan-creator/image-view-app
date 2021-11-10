from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('LOL')
root.iconbitmap('Martz90-Circle-Plex.ico')

img = ImageTk.PhotoImage(Image.open("eye.png"))
img1 = ImageTk.PhotoImage(Image.open("arrow.png"))
img2= ImageTk.PhotoImage(Image.open("Youtubr.png"))

imglist = [img, img1, img2]

label = Label(image=img)
label.grid(row=0, column=0, columnspan=3)


def back(img_no):
    global label
    global Button_next
    global Button_back

    if img_no==1:
        Button_next = Button(root, text=">>",state=DISABLED)

    label.grid_forget()
    label = Label(image=imglist[img_no-1])
    Button_next = Button(root, text=">>", command=lambda: forward(img_no+1))
    Button_back = Button(root, text="<<", command=lambda: forward(img_no-1))

def forward(img_no):
    global label
    global Button_next
    global Button_back

    label.grid_forget()
    label = Label(image=imglist[img_no-1])
    Button_next = Button(root, text=">>", command=lambda: forward(img_no+1))
    Button_back = Button(root, text="<<", command=lambda: forward(img_no-1))

    Button_back.grid(row=1, column=0)
    Button_next.grid(row=1, column=2)
    label.grid(row=0, column=0, columnspan=3) 

    if img_no==2:
        Button_next = Button(root, text=">>",state=DISABLED)

    Button_back.grid(row=1, column=0)
    Button_next.grid(row=1, column=2)
    label.grid(row=0, column=0, columnspan=3)


Button_back = Button(root, text="<<", command=back)
Button_exit = Button(root, text="Exit", command=root.quit)
Button_next = Button(root, text=">>", command=lambda: forward(1))

Button_back.grid(row=1, column=0)
Button_exit.grid(row=1, column=1)
Button_next.grid(row=1, column=2)

root.mainloop()
