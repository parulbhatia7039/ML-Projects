from tkinter import *
from PIL import Image,ImageTk
import admin
import userLoginSignup
class first:
    def __init__(self):
        self.root=Tk()
        self.root.geometry('700x450')
        self.root.resizable(False,False)
        self.root.title('MASTER MINDS')
        
        #background image
        self.im = Image.open('28.jpg').resize((700, 450))
        self.imtk = ImageTk.PhotoImage(self.im)
        self.img = Label(self.root, image=self.imtk)
        self.img.place(x=-2, y=0)

        #heading
        self.head=Label(self.img,text='MASTER MINDS',font='algerian 35 bold',bg='#37e5e4',fg="black",borderwidth=2,relief=GROOVE)
        self.head.place(x=360,y=60,anchor='n')


        #buttons
        self.btn1=Button(self.img,text='ADMIN LOGIN',font='times 20 bold',bg='#d29ad7',fg="black",height=3,command=self.adminl)
        self.btn1.place(x=185,y=250,anchor='center')

        self.btn2 = Button(self.img, text='USER LOGIN', font='times 20 bold',height=3,bg='#d29ad7',fg="black",command=self.userl)
        self.btn2.place(x=525, y=250, anchor='center')
        self.root = mainloop()

    def adminl(self):
        self.root.destroy()
        admin.Adminlogin()



    def userl(self):
        self.root.destroy()
        userLoginSignup.Userlogin()








if __name__=='__main__':
    first()