from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import random
import database
import textwrap
import user_welc
import quiz_pageM
import score_page

score=0
x1=0
class quiz:
    def __init__(self, userDetails):
        # self.score=score
        self.userDetails = userDetails
        self.root=Tk()
        self.root.geometry('900x700')
        self.root.resizable(False,False)
        # self.score=0

        # background image
        self.im = Image.open('20.jpg').resize((900, 700))
        self.imtk = ImageTk.PhotoImage(self.im)
        self.img = Label(self.root, image=self.imtk)
        self.img.place(x=-2, y=0)

        # menu bar
        self.menubar = Menu(self.root)
        self.file = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', menu=self.file)
        self.file.add_command(label='Quit',command=self.Quit)
        self.root.config(menu=self.menubar)


        #fetch question detils
        a=(random.randint(1,53),)
        # print(a)
        QDetails=database.fetchQuestionM(a)

        self.Q=list(QDetails)
        #0-QN 1-Question 2-opt1 3-opt2 4-opt3 5-opt4 7-A,B,C,D

        #question label
        # q=QDetails[1]
        self.question=Label(self.img,text='Q. 'f'{self.Q[1]}',font='Times 22 bold',width=42,wraplength=650,borderwidth=3,relief=RAISED)
        self.question.place(x=80,y=120,anchor='w')

        self.O=StringVar()
        self.O.set('E')
        o1=self.Q[2]
        o2=self.Q[3]
        o3=self.Q[4]
        o4=self.Q[5]
        self.OP=Radiobutton(self.img,text='A. 'f'{o1}',variable=self.O,value='A',font='comicsansms 18 bold',borderwidth=3,relief=RAISED)
        self.OP.place(x=90,y=230)

        self.OP = Radiobutton(self.img, text='B. 'f'{o2}',variable=self.O,value='B', font='comicsansms 18 bold',borderwidth=3,relief=RAISED)
        self.OP.place(x=90, y=300)

        self.OP = Radiobutton(self.img, text='C. 'f'{o3}',variable=self.O,value='C', font='comicsansms 18 bold',borderwidth=3,relief=RAISED)
        self.OP.place(x=90, y=370)

        self.OP = Radiobutton(self.img, text='D. 'f'{o4}',variable=self.O,value='D', font='comicsansms 18 bold',borderwidth=3,relief=RAISED)
        self.OP.place(x=90, y=440)

        # O.get()
        # print(O)

        #buttons
        self.submit=Button(self.img,text='SUBMIT',font='times 19 bold',command=self.sub)
        self.submit.place(x=450,y=600,anchor=CENTER)



        self.root.mainloop()

    def Quit(self):
        global x1
        x1=1
        self.root.destroy()
        user_welc.user(self.userDetails)

    def sub(self):
        pass
        x=self.O.get()
        # print(self.O)
        if x==self.Q[7]:
            global score
            score += 1
            messagebox.showinfo('CORRECT','Your answer is correct!')
        else:
            messagebox.showwarning('WRONG','OOPS!! Wrong answer!!!')

        self.root.destroy()




def run(userDetails):     #this function will run only when called
    # if __name__=='__main__':
    for i in range(0, 10):
        # global x
        if x1==0:
            quiz(userDetails)
    score_page.Sc(score, userDetails)


# print(score)