from tkinter import *
from PIL import Image,ImageTk
import admin
import cuser,firstpage
import addq
class Monika():
    def __init__(self):
        self.root=Tk()
        self.root.geometry("600x400")
        self.root.resizable(False,False)
        self.root.title('MASTER MINDS')
        
        self.img=Image.open("14.jpg").resize((600,400))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.lb=Label(self.root,image=self.imgTk)
        self.lb.place(x=-2,y=0)
        self.lb1=Label(self.lb,text="Welcome Admin",fg="white",bg="black",font=("ALGERIAN",30,"bold"),borderwidth=3,relief=GROOVE)
        self.lb1.place(x=300,y=40,anchor="center")
          
        self.lb2=Button(self.lb,text="User Details",font=("times",20,"bold"),fg="white",bg="black",command=self.mann)
        self.lb2.place(x =300,y=140,anchor="center")

        self.lb3=Button(self.lb,text="Add Questions",font=("times",20,"bold"),fg="white",bg="black",command=self.adq)
        self.lb3.place(x =300,y=240,anchor="center")

        self.lb4=Button(self.lb,text="Log Out",font=("times",20,"bold"),fg="white",bg="black",command=self.logout)
        self.lb4.place(x=300,y=340,anchor="center")

        self.root.mainloop()

    def mann(self):
        self.root.destroy()
        cuser.Ad()
    def adq(self):
        self.root.destroy()
        addq.Adque() 
    # def back(self):
    #     self.root.destroy()
    #     admin.Mann()

    def logout(self):
        self.root.destroy()
        firstpage.first()
if __name__=='__main__':      
  Monika()