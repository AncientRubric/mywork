from tkinter import *
import urllib.request
import re
import os



           
Holster = Tk()





def self():
    Subjectreturn = subject.get()
    subjectreturn = re.compile(re.escape('[firstname]'), re.IGNORECASE)
    subjectreturn.sub('[[dVar=FirstName]]', subject.get())
    Modsubject = subjectreturn.sub('[[dVar=FirstName]]',subject.get())
    subjectreturns = Label(Holster,text=Modsubject)
    text_file = open("Subjectline.txt", "w")
    text_file.write(Modsubject)
    text_file.close()
    os.popen('notepad.exe Subjectline')
   

def selff():
    page = urllib.request.urlopen (subjects.get())
    lower = page.read().decode("utf8")
    finish = lower.replace('<meta','[[meta]]',)
    text = re.compile(re.escape('[firstname]'), re.IGNORECASE)
    text.sub('[[dVar=FirstName]]', finish)
    done = text.sub('[[dVar=FirstName]]', finish)
    text_file = open("Subjectlined.txt", "w")
    text_file.write(done)
    text_file.close()
    os.popen('notepad.exe Subjectlined')

subject = StringVar()
subjects = StringVar()
 
Holster.title('Relevator')

             







b = Button(Holster, text="please enter subjectline?",command = self).pack()

E = Entry(Holster,textvariable=subject).pack()





b1 = Button(Holster, text="please enter HTML URL?",command = selff).pack()

e1 = Entry(Holster,textvariable=subjects).pack()




mainloop()

