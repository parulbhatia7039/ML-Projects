import database
from tkinter import *
from tkinter import messagebox
import adminWc

class AddGK:
    def __init__(self):
        self.root=Tk()
        self.root.geometry('600x490')
        self.root.resizable(False,False)
        self.root.title('MASTER MINDS')

        self.fr = Frame(self.root, bg='light green', height=490, width=600)
        self.fr.place(x=0, y=0)

        self.head = Label(self.root, text='GENERAL KNOWLEDGE', font='times 22 bold')
        self.head.place(x=300, y=30, anchor=CENTER)

        #menu
        self.menubar = Menu(self.root)
        self.file = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', menu=self.file)
        self.file.add_command(label='Back', command=self.back)
        self.root.config(menu=self.menubar)


        #add question label and entries
        self.Ques=Label(self.root,text='Question: ',font='calibri 15 bold')
        self.Ques.place(x=150,y=110,anchor=CENTER)

        self.QuesE=Entry(self.root,font='calibri 15 ',width=30)
        self.QuesE.place(x=350,y=110,anchor=CENTER)

        self.O1 = Label(self.root, text='Option 1: ', font='calibri 15 bold')
        self.O1.place(x=150, y=160, anchor=CENTER)

        self.O1E = Entry(self.root, font='calibri 15 ', width=30)
        self.O1E.place(x=350, y=160, anchor=CENTER)

        self.O2 = Label(self.root, text='Option 2: ', font='calibri 15 bold')
        self.O2.place(x=150, y=210, anchor=CENTER)

        self.O2E = Entry(self.root, font='calibri 15 ', width=30)
        self.O2E.place(x=350, y=210, anchor=CENTER)

        self.O3 = Label(self.root, text='Option 3: ', font='calibri 15 bold')
        self.O3.place(x=150, y=260, anchor=CENTER)

        self.O3E = Entry(self.root, font='calibri 15 ', width=30)
        self.O3E.place(x=350, y=260, anchor=CENTER)

        self.O4 = Label(self.root, text='Option 4: ', font='calibri 15 bold')
        self.O4.place(x=150, y=310, anchor=CENTER)

        self.O4E = Entry(self.root, font='calibri 15 ', width=30)
        self.O4E.place(x=350, y=310, anchor=CENTER)

        self.CO = Label(self.root, text='Correct opt: ', font='calibri 15 bold')
        self.CO.place(x=140, y=360, anchor=CENTER)

        self.COE = Entry(self.root, font='calibri 15 ', width=30)
        self.COE.place(x=350, y=360, anchor=CENTER)

        self.add=Button(self.root,text='ADD QUESTION',font='times 15 bold',command=self.ADD)
        self.add.place(x=300,y=430,anchor=CENTER)



        self.root.mainloop()
    def ADD(self):
        Q=self.QuesE.get().strip()
        O1=self.O1E.get().strip()
        O2 = self.O2E.get().strip()
        O3 = self.O3E.get().strip()
        O4 = self.O4E.get().strip()
        CO=self.COE.get().strip()
        if Q and O1 and O2 and O3 and O4 and CO:
            data=(Q,O1,O2,O3,O4,CO)
            database.addQue(data)
            messagebox.showinfo('SUCCESS','Question added successfully')
            self.root.destroy()
            adminWc.Monika()
        else:
            messagebox.showwarning('ERROR','One or more feilds are empty!! Please try again')


    def back(self):
        self.root.destroy()
        adminWc.Monika()

if __name__=='__main__':
    AddGK()