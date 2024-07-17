from tkinter import *
from PIL import Image,ImageTk
import speech_recognition as sr
import Second_page,Sentiment_Prediction

class Speech_input:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x350+540+190')
        self.root.title('SENTIMENT INSIGHT')
        self.root.config(bg='lightblue')

        self.im = Image.open('4.png').resize((500, 350))
        self.imtk = ImageTk.PhotoImage(self.im)
        self.img = Label(self.root, image=self.imtk)
        self.img.place(x=-2, y=0)

        # menu
        self.menubar = Menu(self.root)
        self.file = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', menu=self.file)
        self.file.add_command(label='Back', command=self.back)
        self.root.config(menu=self.menubar)

        self.word = Label(self.root, text='Speak your feelings...', font=('helvetica', 20, 'bold'), justify='left', bg='#BEFCFD')
        self.word.place(x=20, y=30)

        self.typed_input = Text(self.root, font=('calibri', 15), width=44, height=7)
        self.typed_input.place(x=20, y=84)

        self.record_button = Button(text='RECORD', font=('helvetica', 15, 'bold'), bg='#BEFCFD', command=self.record_speech)
        self.record_button.place(x=125, y=280, anchor='n')

        self.submit_button = Button(text='SUBMIT', font=('helvetica', 15, 'bold'), bg='#BEFCFD',command=self.submit_speech)
        self.submit_button.place(x=375, y=280, anchor='n')

        self.root.mainloop()

    def record_speech(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.typed_input.delete('1.0', END)  # Clear the text box
            self.word.config(text="Listening...")
            audio_data = recognizer.listen(source)

        try:
            self.text = recognizer.recognize_google(audio_data)
            self.typed_input.insert(END, self.text)
            self.word.config(text="Speak your feelings...")
        except sr.UnknownValueError:
            self.typed_input.insert(END, "Could not understand the audio")
        except sr.RequestError as e:
            self.typed_input.insert(END, f"Could not request results; {e}")

    def submit_speech(self):
        # print(self.text)
        self.root.destroy()
        Sentiment_Prediction.Text_prediction(self.text)


    def back(self):
        self.root.destroy()
        Second_page.Second()


if __name__ == '__main__':
    Speech_input()

