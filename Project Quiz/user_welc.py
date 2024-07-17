from tkinter import *
from PIL import Image,ImageTk
import quizstart,firstpage
import os
import udet
class user:
    def __init__(self, userDetails):
        self.userDetails = userDetails
        self.root=Tk()
        self.root.geometry('700x500')
        self.root.resizable(False,False)
        self.root.title('MASTER MINDS')
        # self.root.eval('tk::PlaceWindow . north')

        #background image
        self.im1 = Image.open('3.jpg').resize((700, 500))
        self.imtk1 = ImageTk.PhotoImage(self.im1)
        self.img1 = Label(self.root, image=self.imtk1)
        self.img1.place(x=-2, y=0)

        self.im = Image.open('R.jpeg').resize((600, 400))
        self.imtk = ImageTk.PhotoImage(self.im)
        self.img = Label(self.root, image=self.imtk)
        self.img.place(x=50, y=50)

        #heading
        self.head=Label(self.img,text='Welcome User',font='algerian 35 bold',bg="#feda52")
        self.head.place(x=300,y=20,anchor='n')

        #other options
        self.btn1=Button(self.img,text='START QUIZ',font='times 20 bold',bg="#feda52",command=self.quizs)
        self.btn1.place(x=300,y=150,anchor='center')

        self.btn2 = Button(self.img, text='VIEW PAST RECORDS',font='times 20 bold',bg="#feda52",command=self.pr)
        self.btn2.place(x=300, y=250, anchor='center')

        self.btn3 = Button(self.img, text='LOG OUT',font='times 20 bold',bg="#feda52",command=self.log)
        self.btn3.place(x=300, y=350, anchor='center')

        self.root = mainloop()

    def quizs(self):
        self.root.destroy()
        quizstart.quiz(self.userDetails)
    
    def pr(self):
        self.root.destroy()
        udet.Ud(self.userDetails)

    def log(self):
        self.root.destroy()
        firstpage.first()

if __name__=='__main__':
    user()
