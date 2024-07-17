from tkinter import *
from PIL import Image,ImageTk
import Type_in,Speech_input,First_page

class Second:
    def __init__(self):
        self.root=Tk()
        self.root.geometry('600x350+500+190')
        self.root.config(bg='#BAF8F9')
        self.root.title('SEMTIMENT INSIGHT')

        self.im = Image.open('2.png').resize((600, 350))
        self.imtk = ImageTk.PhotoImage(self.im)
        self.img = Label(self.root, image=self.imtk)
        self.img.place(x=-2, y=0)

        # menu
        self.menubar = Menu(self.root)
        self.file = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', menu=self.file)
        self.file.add_command(label='Back', command=self.back)
        self.root.config(menu=self.menubar)

        self.head=Label(self.root,text='SENTIMENT INSIGHT',font=('times 28 bold'),relief='solid',bg='#C3EFFD')
        self.head.place(x=300,y=20,anchor='n')

        self.body=Label(self.root,text='Choose your preferred method for using Sentiment Insight : '
                                       'TYPE your thoughts or SPEAK them for instant emotional analysis.',
                        font=('helvetica 20'),wraplength=600,justify='center',relief='groove',bg='#C3EFFD')
        self.body.place(x=300,y=95,anchor='n')

        self.text=Button(self.root,text='Type in',bg='#92E4FF',font=('helvetica 17'),command=self.type_in)
        self.text.place(x=150,y=240,anchor='n')

        self.text=Button(self.root,text='Speak',bg='#92E4FF',font=('helvetica 17'),command=self.speak)
        self.text.place(x=450,y=240,anchor='n')

        self.root.mainloop()

    def type_in(self):
        self.root.destroy()
        Type_in.Type_emotions()


    def speak(self):
        self.root.destroy()
        Speech_input.Speech_input()

    def back(self):
        self.root.destroy()
        First_page.First()

if __name__ =='__main__':
    Second()