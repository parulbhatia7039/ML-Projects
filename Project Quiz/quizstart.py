from tkinter import *
from PIL import Image,ImageTk
import user_welc
import quiz_pageM
import gkquiz

class quiz:
    def __init__(self, userDetails):
        self.userDetails = userDetails
        self.root=Tk()
        self.root.geometry('400x280')
        self.root.resizable(False,False)
        self.root.title('MASTER MINDS')

        # background image
        self.im = Image.open('5.jpg').resize((400, 280))
        self.imtk = ImageTk.PhotoImage(self.im)
        self.img = Label(self.root, image=self.imtk)
        self.img.place(x=-2, y=0)

        # menubar
        self.menu = Menu(self.root)
        self.menu1 = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='File', menu=self.menu1)
        self.menu1.add_command(label='Back', command=self.back)

        self.root.config(menu=self.menu)

        #buttons
        self.btn1=Button(self.root,text='MATHS',font='calibri 19 bold',command=self.addmt)
        self.btn1.place(x=100,y=125,anchor='center')

        self.btn2 = Button(self.root, text='GK',font='calibri 19 bold',command=self.addgk)
        self.btn2.place(x=300, y=125,anchor='center')

        self.root.mainloop()

    def back(self):
        self.root.destroy()
        user_welc.user(self.userDetails)

    def addmt(self):
        self.root.destroy()
        quiz_pageM.run(self.userDetails)
        # quiz_pageM.quiz()

    def addgk(self):
        self.root.destroy()
        gkquiz.run1(self.userDetails)

if __name__=='__main__':
    quiz()