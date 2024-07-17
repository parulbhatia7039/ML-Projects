from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import adminWc,admin
import firstpage


class Adminlogin:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("700x500")
        self.root.resizable(False,False)
        self.root.title('MASTER MINDS')

        self.menubar = Menu(self.root)
        self.file = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', menu=self.file)
        self.file.add_command(label='Back', command=self.back)
        self.root.config(menu=self.menubar)

        self.img=Image.open("9.png").resize((700,500))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.lb=Label(self.root,image=self.imgTk)
        self.lb.place(x=0,y=0)
        
    
        self.lb1=Label(self.lb,text="Admin ",bg="#fcd4e2",font=("ALGERIAN",30,"bold"),borderwidth=3,relief=GROOVE)
        self.lb1.place(x=350,y=45,anchor='center')
        
        self.lb2=Label(self.lb,text="Username :",bg="#fcd4e2",font=("Georgia",20,"bold"))
        self.lb2.place(x=175,y=150,anchor="center")
        self.userEntry=Entry(self.lb,width=20,font=("Georgia",17,"bold"))
        self.userEntry.place(x=450,y=150,anchor="center")

        self.lb3=Label(self.lb,text="Password :",bg="#fcd4e2",font=("Georgia",20,"bold"))
        self.lb3.place(x=175,y=250,anchor="center")
        self.passEntry=Entry(self.lb,show="*",font=("Georgia",17,"bold"),width=20)
        self.passEntry.place(x=450,y=250,anchor="center")

        self.lb4=Button(self.lb,text="Login",bg="#fcd4e2",font=("Georgia",20,"bold"),command=self.log)
        self.lb4.place(x=350,y=350,anchor="center")
        self.root.mainloop()


    def log(self):
        if self.userEntry.get()=='123' and self.passEntry.get()=='123':
            self.root.destroy()
            adminWc.Monika()
        else:
            messagebox.showerror('ERROR','Wrong Id or Password!!')
            self.root.destroy()
            admin.Adminlogin()

    def back(self):
        messagebox.showinfo('SUCCESSFUL','Welcome Admin.')
        self.root.destroy()
        firstpage.first()




if __name__=='__main__':
    Adminlogin()