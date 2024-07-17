from tkinter import *
from PIL import Image, ImageTk
import user_welc
import gkquiz,userLoginSignup,database


class Sc():
    def __init__(self, score, userDetails):
        self.userDetails = userDetails
        self.s = score
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.title('MASTER MINDS')

        self.img = Image.open("15.jpg").resize((500, 500))
        self.imgTk = ImageTk.PhotoImage(self.img)
        self.lb = Label(self.root, image=self.imgTk)
        self.lb.place(x=-2, y=0)

        self.lb1 = Label(self.lb, text="YOUR SCORE", font=("ALGERIAN", 30, "bold"), fg="white", bg="#090909",
                         borderwidth=3, relief=GROOVE)
        self.lb1.place(x=250, y=50, anchor="center")

        self.lb3 = Button(self.lb, text=f'{self.s}/10', command=self.back, font=("times", 22, "bold"), fg="white",
                          bg="#151515")
        self.lb3.place(x=250, y=215, anchor="center")

        self.lb2 = Button(self.lb, text="Back to Main Menu", command=self.back, font=("times", 22, "bold"), fg="white",
                          bg="#151515")
        self.lb2.place(x=250, y=380, anchor="center")



        # det=userLoginSignup.username()
        # res = database.GetMarks(det)
        # if res:
        #     marks = (self.s, x)
        #     database.UpdateMarksGK(marks)
        # else:
        #     details = (x, self.s)
        #     database.AddMarksGK(details)

        database.addps((self.userDetails[5], "GK", f'{self.s}/10'))


        self.root.mainloop()

    def back(self):
        self.root.destroy()
        user_welc.user(self.userDetails)


if __name__ == '__main__':
    Sc(gkquiz.score)