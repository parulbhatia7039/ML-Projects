from tkinter import *
from PIL import Image,ImageTk
import userLoginSignup
import signup,firstpage
import database
from tkinter import messagebox

class sign:
    def __init__(self):
        self.root=Tk()
        self.root.geometry('900x600')
        self.root.resizable(False,False)
        self.root.title('MASTER MINDS')

        #background image
        self.im=Image.open('2.png').resize((900,600))
        self.imtk=ImageTk.PhotoImage(self.im)
        self.img = Label(self.root, image=self.imtk)
        self.img.place(x=0,y=0)

        #menu bar
        self.menubar = Menu(self.root)
        self.file = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', menu=self.file)
        self.file.add_command(label='Back', command=self.back1)
        self.root.config(menu=self.menubar)

        #Title
        self.head=Label(self.img,text="SIGN UP",font=('algerian 20 bold'),width=12,justify=CENTER,bg='#8fbe40',borderwidth=2,relief=RAISED)
        self.head.place(x=450,y=30,anchor='n')

        #login details
        self.name=Label(self.img,text='Name',font=('Cambria 15 bold'),width=12,justify=CENTER)
        self.name.place(x=250,y=120)

        self.nameE=Entry(self.img,font=('comicsansms 15 '))
        self.nameE.place(x=450,y=120)

        self.age = Label(self.img, text='Age', font=('Cambria 15 bold'),width=12,justify=CENTER)
        self.age.place(x=250,y=180)

        self.ageE = Entry(self.img, font=('comicsansms 15 '))
        self.ageE.place(x=450,y=180)

        self.email = Label(self.img, text='Email', font=('Cambria 15 bold'), width=12,justify=CENTER)
        self.email.place(x=250, y=240)

        self.emailE = Entry(self.img, font=('comicsansms 15 '))
        self.emailE.place(x=450, y=240)

        self.number = Label(self.img, text='Phone Number', font=('Cambria 15 bold'),width=12,justify=CENTER)
        self.number.place(x=250, y=300)

        self.numberE = Entry(self.img, font=('comicsansms 15 '))
        self.numberE.place(x=450, y=300)

        self.usern = Label(self.img, text='Set Username', font=('Cambria 15 bold'), width=12, justify=CENTER)
        self.usern.place(x=250, y=360)

        self.usernE = Entry(self.img, font=('comicsansms 15 '))
        self.usernE.place(x=450, y=360)

        self.pas = Label(self.img, text='Set Password', font=('Cambria 15 bold'), width=12, justify=CENTER)
        self.pas.place(x=250, y=420)

        self.pasE = Entry(self.img, font=('comicsansms 15 '))
        self.pasE.place(x=450, y=420)


        # submit button
        self.btn=Button(self.img,text='SUBMIT',font='times 17 bold',width=12,bg='#58C1CD',command=self.back)
        self.btn.place(x=450,y=520,anchor='center')

        self.root=mainloop()

    def back(self):
        n=self.nameE.get().title().strip()
        a=self.ageE.get().strip()
        m=self.emailE.get().strip()
        p=self.numberE.get().strip()
        u=self.usernE.get().strip()
        pa=self.pasE.get()

        if n and a and m and p and u and pa:
            det=(n,a,m,p,u,pa)
            enter=database.signupp(det)
            # print(det)
            if enter:
                messagebox.showinfo('SUBMITTED', 'Details saved successfully!')
            else:
                messagebox.showerror('ERROR','Something went wrong!!!')

            self.root.destroy()
            userLoginSignup.Userlogin()
        else:
            messagebox.showerror('ERROR','One or more fields are empty! Please fill all the details.')

    def back1(self):
        self.root.destroy()
        firstpage.first()


    # def submit(self):
if __name__=='__main__':
    sign()