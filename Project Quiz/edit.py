from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import database,userdetails

class editt:
    def __init__(self,row):
        self.root=Tk()
        self.root.geometry('900x600')
        self.root.resizable(False,False)
        self.root.title('MASTER MINDS')

        self.row=row

        #background image
        self.img=Image.open('4.png').resize((900,600))
        self.imgtk=ImageTk.PhotoImage(self.img)
        self.img= Label(self.root, image=self.imgtk)
        self.img.place(x=0,y=0)


        self.im=Image.open('n.jpg').resize((600,500))
        self.imtk=ImageTk.PhotoImage(self.im)
        self.im = Label(self.img, image=self.imtk)
        self.im.place(x=150,y=50)

        #Title
        self.head=Label(self.img,text="Edit Details",font=('algerian 23 bold'),width=12,justify=CENTER,bg='#aeeeee',borderwidth=4,relief=RAISED)
        self.head.place(x=450,y=60,anchor='n')

        #login details
        self.name=Label(self.img,text='Name',font=('Cambria 15 bold'),bg='#aeeeee',width=12,justify=CENTER)
        self.name.place(x=250,y=130)

        self.nameE=Entry(self.img,font=('comicsansms 17 '))
        self.nameE.place(x=450,y=130)

        self.age = Label(self.img, text='Age', font=('Cambria 17 bold'),bg='#aeeeee',width=12,justify=CENTER)
        self.age.place(x=250,y=190)

        self.ageE = Entry(self.img, font=('comicsansms 17 '))
        self.ageE.place(x=450,y=190)

        self.email = Label(self.img, text='Email', font=('Cambria 15 bold'),bg='#aeeeee', width=12,justify=CENTER)
        self.email.place(x=250, y=250)

        self.emailE = Entry(self.img, font=('comicsansms 17 '))
        self.emailE.place(x=450, y=250)

        self.number = Label(self.img, text='Phone Number', font=('Cambria 17 bold'),bg='#aeeeee',width=12,justify=CENTER)
        self.number.place(x=250, y=310)

        self.numberE = Entry(self.img, font=('comicsansms 17 '))
        self.numberE.place(x=450, y=310)

        self.usern = Label(self.img, text='Set Username', font=('Cambria 17 bold'),bg='#aeeeee', width=12, justify=CENTER)
        self.usern.place(x=250, y=370)

        self.usernE = Entry(self.img, font=('comicsansms 17 '))
        self.usernE.place(x=450, y=370)

        self.pas = Label(self.img, text='Set Password', font=('Cambria 17 bold'),bg='#aeeeee', width=12, justify=CENTER)
        self.pas.place(x=250, y=430)

        self.pasE = Entry(self.img, font=('comicsansms 17 '))
        self.pasE.place(x=450, y=430)


        # submit button
        self.btn=Button(self.img,text='SUBMIT',font='times 19 bold',width=12,bg='sky blue',command=self.back,borderwidth=4,relief=RAISED)
        self.btn.place(x=450,y=500,anchor='center')

        self.root=mainloop()

    def back(self):
        n=self.nameE.get().title().strip()
        a=self.ageE.get().strip()
        m=self.emailE.get().strip()
        p=self.numberE.get().strip()
        u=self.usernE.get().strip()
        pa=self.pasE.get()
        r=self.row[0]     #this stores the id or S.No of the row to be updated

        if n and a and m and p and u and pa:
            det=(n,a,m,p,u,pa,r)
            enter=database.EditDetails(det)
            print(det)
            if enter:
                messagebox.showinfo('UPDATED', 'Details updated successfully!')
            else:
                messagebox.showerror('ERROR','Something went wrong!!!')

            self.root.destroy()
            userdetails.details()
        else:
            messagebox.showerror('ERROR','One or more fields are empty! Please try again.')

if __name__=='__main__':
    editt(('1',))