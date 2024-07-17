from tkinter import *
from PIL import Image,ImageTk
import adminWc
import AddQuestionsM,AddQuestionsGK

class Adque():
    def __init__(self):
        self.root=Tk()
        self.root.geometry("300x200")
        self.root.resizable(False,False)
        self.root.title('MASTER MINDS')
        
        self.img=Image.open("bg21.jpg").resize((300,200))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.lb=Label(self.root,image=self.imgTk)
        self.lb.place(x=-2,y=0)
        self.menubar = Menu(self.root)
        self.file = Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label = 'File', menu=self.file)
        self.file.add_command(label = 'Back', command = self.back)
        self.root.config(menu = self.menubar)
        
        self.lb2=Button(self.lb,text="Methametics",font=("times",20,"bold"),fg="white",bg="black",command=self.addmt)
        self.lb2.place(x =150,y=60,anchor="center")

        self.lb3=Button(self.lb,text="GK",font=("times",20,"bold"),fg="white",bg="black",command=self.addgk)
        self.lb3.place(x =150,y=140,anchor="center")

        self.root.mainloop()
    def back(self):
         self.root.destroy()
         adminWc.Monika()

    def addmt(self):
        self.root.destroy()
        AddQuestionsM.AddM()
    def addgk(self):
        self.root.destroy()
        AddQuestionsGK.AddGK()


if __name__=='__main__':
  Adque()