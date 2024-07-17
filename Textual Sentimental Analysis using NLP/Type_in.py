from tkinter import *
from PIL import Image,ImageTk
import Second_page,Sentiment_Prediction

class Type_emotions:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x350+540+190')
        self.root.title('SENTIMENT INSIGHT')
        self.root.config(bg='pink')

        self.im = Image.open('3.jpg').resize((500, 350))
        self.imtk = ImageTk.PhotoImage(self.im)
        self.img = Label(self.root, image=self.imtk)
        self.img.place(x=-2, y=0)

        # menu
        self.menubar = Menu(self.root)
        self.file = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', menu=self.file)
        self.file.add_command(label='Back', command=self.back)
        self.root.config(menu=self.menubar)

        self.word=Label(self.root,text='Type your feelings...',font=('helvetica 20 bold'),justify='left',bg='#FFD4F7')
        self.word.place(x=20,y=30)

        self.typed_input=Text(self.root,font=('calibri 15'),width=44,height=7)
        self.typed_input.place(x=20,y=90)

        self.submit=Button(text='SUBMIT',font=('helvetica 15 bold'),bg='#FFD4F7',command=self.submit)
        self.submit.place(x=250,y=280,anchor='n')

        self.root.mainloop()

    def submit(self):
        text=self.typed_input.get("1.0", END)
        # print(text)
        self.root.destroy()
        Sentiment_Prediction.Text_prediction(text)


    def back(self):
        self.root.destroy()
        Second_page.Second()


if __name__ =='__main__':
    Type_emotions()