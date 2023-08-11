from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb
root = Tk()
root.title('Cw1-steganography')
root.geometry("500x400")

def Pickimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File',filetype=(("PNG file","*.png"),("JPG File","*.jpg"),("ALL file","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img
def Hide():
    global secret
    message=text1.get(1.0,END)
    secret = lsb.hide(str(filename),message)
def Show():
    clear_message= lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)
    
def save():
    secret.save("secret.png")
    

my_frame = Frame(root)
my_frame.pack(pady=20)

img_button = Button(my_frame, text="Pick image", font=("Helvetica", 18), command=Pickimage)
img_button.grid(row=0, column=0)

Hide_button = Button(my_frame, text="Hide",font=("Helvetica", 18), command=Hide)
Hide_button.grid(row=0, column=1, padx=20)

show_button = Button(my_frame, text="show",font=("Helvetica", 18), command=Show)
show_button.grid(row=0, column=2)

save_button = Button(my_frame, text="save", font=("Helvetica", 18), command=save)
save_button.grid(row=0, column=3, padx=20)

enc_label = Label(root, text="images",font=("Helvetica", 14))
enc_label.pack()    	

f=Frame(root,bd=3,bg="black",width=480,height=280,relief=GROOVE)
f.place(x=10,y=80)

lbl=Label(f,bg="black")
lbl.place(x=110,y=10)


text_label = Label(root, text="Enter your text",font=("Helvetica", 14))
text_label.pack()

frame2=Frame(root,bd=3,width=480,height=50,bg="white",relief=GROOVE)
frame2.place(x=10,y=160)

text1=Text(frame2,font="Robote 12",bg="white",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=500,height=295)
    
root.mainloop()