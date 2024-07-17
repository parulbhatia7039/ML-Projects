from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox

import adminWc
import database,userdetails
import edit


class details:
    def __init__(self):
        self.root=Tk()
        self.root.geometry('800x550')
        self.root.resizable(False,False)
        self.root.title('MASTER MINDS')

        self.menubar = Menu(self.root)
        self.file = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', menu=self.file)
        self.file.add_command(label='Back', command=self.back)
        self.root.config(menu=self.menubar)


        self.col=['Id','Name','Age','Email','No','Username','Edit','Delete']
        self.tree=Treeview(self.root,columns=self.col,show='headings')
        self.tree.heading('Id',text='ID')
        self.tree.column('# 1',anchor=CENTER,stretch=NO,width=30)

        self.tree.heading('Name', text='NAME')
        self.tree.column('# 2', anchor=CENTER, stretch=NO, width=120)

        self.tree.heading('Age', text='AGE')
        self.tree.column('# 3', anchor=CENTER, stretch=NO, width=50)

        self.tree.heading('Email', text='EMAIL')
        self.tree.column('# 4', anchor=CENTER, stretch=NO, width=180)

        self.tree.heading('No', text='PHONE NUMBER')
        self.tree.column('# 5', anchor=CENTER, stretch=NO, width=120)

        self.tree.heading('Username', text='USERNAME')
        self.tree.column('# 6', anchor=CENTER, stretch=NO, width=120)

        self.tree.heading('Edit', text='EDIT')
        self.tree.column('# 7', anchor=CENTER, stretch=NO, width=50)

        self.tree.heading('Delete', text='DELETE')
        self.tree.column('# 8', anchor=CENTER, stretch=NO, width=50)

        res=database.getuser()
        # print(res)
        res.reverse()
        for i in res:           #inserting values in treeview
            # print(i[0])
            self.tree.insert('',0,text=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5],'Edit','Delete'))

        self.s=Scrollbar(self.root,orient='vertical')
        self.s.pack(side='right',fill ='y')
        self.tree.bind('<Double-Button-1>',self.action)    #this will run command 'action' when there will be double click on treeview

        self.tree.pack(fill=X)
        self.root.mainloop()

    def action(self,e):     #used to get the value of double click on treeview
        print(e)
        #used to identify column which is being clicked ('Edit' or 'Delete')
        colu=self.tree.identify_column(e.x)
        print(colu)

        #used to identify the focus of the element which is being clicked
        row=self.tree.focus()
        items=self.tree.item(row)
        print(items)
        #7- Edit 8-Delete
        gup=(self.tree.item(row).get('text'),)   #it stores the text of the item being clicked
        print(gup)

        if colu=='#7':   #Edit
            self.root.destroy()
            edit.editt(gup)



        if colu=='#8':   #Delete
            confirm=messagebox.askyesno('CONFIRM','Do you really want to delete this record?')
            if confirm:
                deleted=database.delete(gup)
                if deleted:
                    messagebox.showinfo('DELETED','Details deleted successfully!!!')
                    self.root.destroy()
                    userdetails.details()
                else:
                    messagebox.showerror('ERROR','Something wen wrong. Please try again!')

    def back(self):
        self.root.destroy()
        adminWc.Monika()




if __name__=='__main__':
    details()