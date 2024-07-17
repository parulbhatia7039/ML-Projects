from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import user_welc

import database,userLoginSignup


import database


class Ud():
    def __init__(self, userDetails):
        self.userDetails = userDetails
        self.root=Tk()
        self.root.geometry("700x400")
        self.root.resizable(False,False)
        self.root.title("MASTER MINDS")
        
        self.menubar = Menu(self.root)
        self.file = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', menu=self.file)
        self.file.add_command(label='Back', command=self.back)
        self.root.config(menu=self.menubar)
   
        self.col=["Id","Username","Type","GK"]
        self.tree=Treeview(self.root,columns=self.col,show="headings")

        self.tree.heading("Id",text="Id")
        self.tree.column("1",anchor=CENTER,stretch=NO,width=160)


        self.tree.heading("Username",text="Username")
        self.tree.column("2",anchor=CENTER,stretch=NO,width=160)

        self.tree.heading("Type",text="Type")
        self.tree.column("#3",anchor=CENTER,stretch=NO,width=160)

        self.tree.heading("GK",text="Marks(out of 10)")
        self.tree.column("#4",anchor=CENTER,stretch=NO,width=160)



        # det=userLoginSignup.username()
        # res= database.GetMarks(det)
        # print(res)
        # # res.reverse()
        # # for i in res:
        # #     self.tree.insert('',0,text=i[0],values=(i[1],i[2],i[3]))

        res= database.s(userDetails[5])
        res.reverse()
        for i in res:
         self.tree.insert('',0,text=i[0],values=(i[0],i[1],i[2],i[3]))


        self.s=Scrollbar(self.root,orient='vertical')
        self.s.pack(side='right',fill='y')
        self.tree.pack(fill=X)


        self.root.mainloop()
    def back(self):
       self.root.destroy()
       user_welc.user(self.userDetails) 
     
if __name__=="__main__":
    Ud(('1',))

