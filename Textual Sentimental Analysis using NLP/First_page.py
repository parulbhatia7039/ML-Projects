from tkinter import *
from PIL import Image,ImageTk
import Second_page

class First:
    def __init__(self):
        self.root = Tk()
        self.root.title('SENTIMENT INSIGHT')
        self.root.geometry('700x500+450+160')
        self.root.config(bg='sky blue')

        self.im = Image.open('1.png').resize((700, 500))
        self.imtk = ImageTk.PhotoImage(self.im)
        self.img = Label(self.root, image=self.imtk)
        self.img.place(x=-2, y=0)

        # heading
        self.head=Label(self.img,text='WELCOME TO SENTIMENT INSIGHT',font='times 28 bold',bg='#B8F8D3',borderwidth=2,relief='solid')
        self.head.place(x=350,y=30,anchor='n')

        # body
        self.body=Label(self.img,text='Welcome to Sentiment Insight! Our application is designed to uncover your emotions from the text you provide. '
                                       'Whether you type out your feelings or speak them aloud, '
                                       'Sentiment Insight uses advanced NLP algorithms to analyze your input and reveal your current mood instantly. '
                                       'Experience a new way to connect with your emotions effortlessly!',
                        font='Tahoma 18',wraplength=680,justify='center',bg='#B8F8D3',relief='groove')
        self.body.place(x=350,y=120,anchor='n')

        self.button_text=Label(self.img,text='Click Below to Get Started ',font=('helvetica 18 bold'),bg='white')
        self.button_text.place(x=350,y=335,anchor='n')

        self.button=Button(self.img,text='Lets Go',font=('calibri 16 bold'),bg='#F0E316',command=self.second_page)
        self.button.place(x=350,y=395,anchor='n')

        self.root.mainloop()
    def second_page(self):
        self.root.destroy()
        Second_page.Second()

if __name__ == '__main__':
    First()