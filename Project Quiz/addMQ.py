import database
#list=[t1,t2,....] where t1,t2=(tuples)
# QN	Question	O1	O2	O3	O4	CO
# in correct option we will put the answer an not the option
questions=[]
for i in range(0,4):
    # qn=int(input('Enter question number'))
    Q=input('Enter Question')
    A=input('1st option')
    B = input('2nd option')
    C = input('3rd option')
    D = input('4th option')
    CO=input('enter correct option')
    t=(Q,A,B,C,D,CO)
    questions.append(t)
print(questions)

for i in questions:
    database.addQuestionsM(i)



