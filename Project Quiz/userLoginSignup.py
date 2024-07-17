from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import firstpage

import database
import user_welc,signup

user=str()
class Userlogin:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("700x500")
        self.root.resizable(False,False)
        self.root.title('MASTER MINDS')

        self.img=Image.open("7.jpg").resize((700,500))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.lb=Label(self.root,image=self.imgTk)
        self.lb.place(x=-2,y=0)

        # menubar
        self.menu = Menu(self.root)
        self.menu1 = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='File', menu=self.menu1)
        self.menu1.add_command(label='Back', command=self.back)

        self.root.config(menu=self.menu)
    
        self.lb1=Label(self.lb,text="User",bg="#6cb2bc" ,font=("ALGERIAN",30,"bold"),borderwidth=3,relief=GROOVE)
        self.lb1.place(x=350,y=45,anchor='center')
        
        self.lb2=Label(self.lb,text="Username :",bg="#6cb2bc",font=("Georgia",20,"bold"))
        self.lb2.place(x=175,y=150,anchor="center")
        self.userEntry=Entry(self.lb,width=20,font=("Georgia",17,"bold"))
        self.userEntry.place(x=450,y=150,anchor="center")

        self.lb3=Label(self.lb,text="Password :",bg="#6cb2bc",font=("Georgia",20,"bold"))
        self.lb3.place(x=175,y=250,anchor="center")
        self.passEntry=Entry(self.lb,show="*",font=("Georgia",17,"bold"),width=20)
        self.passEntry.place(x=450,y=250,anchor="center")

        self.lb4=Button(self.lb,text="Sign up",bg="#6cb2bc",font=("Georgia",20,"bold"),command=self.signup)
        self.lb4.place(x=275,y=350,anchor="center")

        self.lb4=Button(self.lb,text="Login",bg="#6cb2bc",font=("Georgia",20,"bold"),command=self.login)
        self.lb4.place(x=450,y=350,anchor="center")
        self.root.mainloop()

    def login(self):
        details=(self.userEntry.get(),self.passEntry.get())
        log=database.login(details)
        if log:
            global user
            user=self.userEntry.get()
            messagebox.showinfo('SUBMITTED','Login successful!!!')
            self.root.destroy()
            user_welc.user(log)
        else:
            messagebox.showwarning('ERROR','You are not registered user. Sign up!!')

    def signup(self):
        self.root.destroy()
        signup.sign()

    def back(self):
        self.root.destroy()
        firstpage.first()


def username():
    global user
    xy=user
    return xy


if __name__=='__main__':
    Userlogin()