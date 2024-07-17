from tkinter import *
from PIL import Image,ImageTk
import adminWc
import userdetails


class Ad():
    def __init__(self):
        self.root=Tk()
        self.root.geometry("400x300")
        self.root.resizable(False,False)
        self.root.title('MASTER MINDS')

        self.menubar = Menu(self.root)
        self.file = Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label = 'File', menu=self.file)
        self.file.add_command(label = 'Back', command = self.back)
        self.root.config(menu = self.menubar)

        self.img=Image.open("bg3.jpg").resize((400,300))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.lb=Label(self.root,image=self.imgTk)
        self.lb.place(x=-2,y=0)
        
        self.lb2=Button(self.root,text="View User Details",font=("times",20,"bold"),fg="white",bg="black",command=self.user)
        self.lb2.place(x =200,y=50,anchor="center")

        self.lb3=Button(self.root,text="Correction in User Details",font=("times",20,"bold"),fg="white",bg="black",command=self.user)
        self.lb3.place(x =200,y=150,anchor="center")

        self.lb4=Button(self.root,text="Remove User",font=("times",20,"bold"),fg="white",bg="black",command=self.user)
        self.lb4.place(x=200,y=250,anchor="center")

        self.root.mainloop()
    def back(self):
        self.root.destroy()
        adminWc.Monika()

    def user(self):
        self.root.destroy()
        userdetails.details()


if __name__=='__main__':
  Ad()