from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk 
import database
import textwrap
import random
import user_welc,score_page_GK

x=0
score=0

class Gkmann:
    def __init__(self, userDetails):
        self.userDetails = userDetails
        self.root=Tk()
        self.root.geometry('1000x600')
        self.root.resizable(False,False)
        self.root.title('MASTER MINDS')
        self.score=0

        self.img=Image.open("mann.jpg").resize((1000,598))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.img=Label(self.root,image=self.imgTk)
        self.img.place(x=-2,y=0)

        self.menubar = Menu(self.root)
        self.file = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', menu=self.file)
        self.file.add_command(label='Quit',command=self.Quitgk)
        self.root.config(menu=self.menubar)
         
        m=(random.randint(1,50),)
        qd=database.fetchQue(m)
        self.Qgk=list(qd)

        self.question=Label(self.img,text="Q. " f'{self.Qgk[1]}',font='Times 24 bold',borderwidth=5,relief=RIDGE,bg="white",fg="black",wraplength=950)
        self.question.place(x=20,y=20)

        self.O=StringVar()
        self.O.set('mn')
        Op1=self.Qgk[2]
        Op2=self.Qgk[3]
        Op3=self.Qgk[4]
        Op4=self.Qgk[5]
        self.OPg=Radiobutton(self.img,text='A. 'f'{Op1}',variable=self.O,value='A',bg="white",borderwidth=3,relief=RAISED,fg="black",font='times 20 bold')
        self.OPg.place(x=70,y=150)

        self.OPg = Radiobutton(self.img, text='B. 'f'{Op2}',variable=self.O,value='B',bg="white",borderwidth=3,relief=RAISED,fg="black" ,font='times 20 bold')
        self.OPg.place(x=70, y=250)

        self.OPg = Radiobutton(self.img, text='C. 'f'{Op3}',variable=self.O,value='C',bg="white",borderwidth=3,relief=RAISED,fg="black", font='times 20 bold')
        self.OPg.place(x=70, y=350)

        self.OPg = Radiobutton(self.img, text='D. 'f'{Op4}',variable=self.O,value='D',bg="white",borderwidth=3,relief=RAISED,fg="black", font='times 20 bold')
        self.OPg.place(x=70, y=450)

        self.submit=Button(self.img,text='SUBMIT',font='times 22 bold',command=self.subgk,borderwidth=8,relief=RAISED,bg="#0000FF",fg="WHITE")
        self.submit.place(x=500,y=550,anchor=CENTER)

        self.root.mainloop()

    def Quitgk(self):
        global x
        x=1
        self.root.destroy()
        user_welc.user(self.userDetails)

    def subgk(self):
        pass
        x=self.O.get()
        # print(self.O)
        if x==self.Qgk[6]:
            global score
            score += 1
            messagebox.showinfo('CORRECT','Your answer is correct!')
        else:
            messagebox.showwarning('WRONG','OOPS!! Wrong answer!!!')

        self.root.destroy()


def run1(userDetails):
# if __name__=="__main__":
    for i in range(0,10):
        if x==0:
            Gkmann(userDetails)
    score_page_GK.Sc(score, userDetails)


