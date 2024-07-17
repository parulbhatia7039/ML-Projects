from tkinter import *
from PIL import Image,ImageTk
import Second_page
import pickle as pkl
import pandas as pd
from nltk.stem import PorterStemmer
import Second_page

text = 'i love you'

class Text_prediction:
    def __init__(self,text):
        self.root=Tk()
        self.root.geometry('400x250+570+200')
        self.root.title('SENTIMENT INSIGHT')
        self.root.config(bg='#EDAB85')

        self.im = Image.open('5.jpg').resize((400, 250))
        self.imtk = ImageTk.PhotoImage(self.im)
        self.img = Label(self.root, image=self.imtk)
        self.img.place(x=-2, y=0)

        # Load pre-trained models
        naive_model = pkl.load(open('Naive_model.pkl', 'rb'))
        tfidf_model = pkl.load(open('Text_to_vector_model.pkl', 'rb'))

        symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                   '_', '-', '+', '=', '{', '}', '[', ']', '|', '\\',
                   ':', ';', '\'', '\"', '<', '>', ',', '.', '?', '/']

        def set_tweet_content(self,content):
            content = content.split()
            temp = []
            for word in content:
                if '@' in word:
                    continue
                else:
                    for symbol in symbols:
                        if symbol in word:
                            word = word.replace(symbol, '')
                    temp.append(word)
            return temp

        Stemmer_model = PorterStemmer()

        def stem_words(content):
            temp = []
            for word in content:
                temp.append(Stemmer_model.stem(word))
            return ' '.join(temp)

        # text = 'i love you'
        text=text

        if text:  # Check if text is not empty
            text_in_list = set_tweet_content(self,text)
            text = stem_words(text_in_list)
            text = pd.Series(text)
            text_vector = tfidf_model.transform(text).toarray()
            prediction = naive_model.predict(text_vector)
            # print(prediction[0])
        else:
            print("No input received.")

        # if prediction[0]=='Love':
        #     co = '#EDAB85'
        # elif prediction[0]==''

        self.mood=Label(self.root,text=f'Your Current Mood is {prediction[0]}',font=('times 20 bold'),bg='#C0EFFF')
        self.mood.place(x=200,y=70,anchor='n')



        self.again=Button(self.root,text='PREDICT AGAIN',font=('helvetica 12'),command=self.again,bg='#C0EFFF')
        self.again.place(x=120,y=150,anchor='n')

        self.exit=Button(self.root,text='EXIT',font=('helvetica 12'),command=self.exit,bg='#C0EFFF')
        self.exit.place(x=300,y=150,anchor='n')

        self.root.mainloop()

    def again(self):
        self.root.destroy()
        Second_page.Second()

    def exit(self):
        self.root.destroy()


if __name__ == '__main__':
    Text_prediction(text)