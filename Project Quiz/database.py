#for now keepin this commented


import mysql.connector
Info = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    db="project_quiz"
)
cursor=Info.cursor()

def signupp(data):
    try:
        cursor.execute('INSERT INTO `signup` (`Name`,`Age`,`Email`,`Phone Number`,`Username`,`Password`) VALUES (%s, %s,%s, %s,%s, %s)', data)
        Info.commit()
        return True
    except Exception as e:
        print('exception is',e)
        return False

def getuser():
    try:
        cursor.execute('SELECT * from `signup`')
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return False

def delete(id):
    try:
        cursor.execute('DELETE from `signup` WHERE `S.No`=%s',id)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False

def login(data):
    try:
        cursor.execute('SELECT * from `signup` WHERE `username`=%s AND `password`=%s',data)
        return cursor.fetchone()
    except Exception as e:
        print(e)
        return False

def EditDetails(data):
    try:
        cursor.execute('UPDATE `signup` SET `Name`=%s,`Age`=%s,`Email`=%s,`Phone Number`=%s,`Username`=%s,`Password`=%s  WHERE `S.No`=%s',data)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False

#quiz questions database

def addQuestionsM(add):
    try:
        cursor.execute('INSERT INTO `m_questions`(`Question`, `O1`, `O2`, `O3`, `O4`, `CO1`) VALUES (%s,%s,%s,%s,%s,%s)',add)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False

def fetchQuestionM(id):
    try:
        cursor.execute('SELECT * FROM `m_questions` where `QN`=%s',id)
        return cursor.fetchone()
    except Exception as e:
        print(e)
        return False

def addQue(add):
    try:
        cursor.execute('INSERT INTO `gkque`(`Ques`, `Op1`, `Op2`, `Op3`, `Op4`, `CorrectOp`) VALUES (%s,%s,%s,%s,%s,%s)',add)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False

def fetchQue(id):
    try:
        cursor.execute('SELECT * FROM `gkque` where `Qnum`=%s',id)
        return cursor.fetchone()
    except Exception as e:
        print(e)
        return False


#marks database

def GetMarks(usern):
    try:
        cursor.execute('SELECT * FROM `quiz_marks` WHERE `username`= %s',usern)
        return cursor.fetchone()
    except Exception as e:
        print(e)
        return False

def AddMarksM(details):
    try:
        cursor.execute('INSERT INTO `quiz_marks`(`username`, `Maths`) VALUES (%s,%s)',details)
        return True
    except Exception as e:
        print(e)
        return False

def addps(add):
    try:
        cursor.execute('INSERT INTO `score`( `Username`, `Type`, `Past Record`) VALUES (%s,%s,%s)',add)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False


def AddMarksGK(details):
    try:
        cursor.execute('INSERT INTO `quiz_marks`(`username`, `GK`) VALUES (%s,%s)',details)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False

def UpdateMarksM(marks):
    try:
        cursor.execute('UPDATE `quiz_marks` SET `Maths`=%s WHERE `username`=%s',marks)
        return True
    except Exception as e:
        print(e)
        return False

def UpdateMarksGK(marks):
    try:
        cursor.execute('UPDATE `quiz_marks` SET `GK`=%s WHERE `username`=%s',marks)
        return True
    except Exception as e:
        print(e)
        return False



def s(data):   
    try:
        cursor.execute('SELECT * from `score` where username=%s',(data,))
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return False   


