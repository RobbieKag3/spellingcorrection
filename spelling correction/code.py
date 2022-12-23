from tkinter import *
from textblob import TextBlob
import textblob
def clearall():
    word1.delete(0,END)
    word2.delete(0,END)
def correction():
    input=word1.get()
    obj=TextBlob(input)
    correctedword=str(obj.correct())
    word2.delete(0,END)
    word2.insert(10,correctedword)
if __name__=="__main__":
    root=Tk()
    root.configure(background="lightgreen")
    root.geometry("400x150")
    root.title("Spelling Corrector App")
    heading=Label(root,text="WELCOME TO THE SPELLING CORRECTION APP")
    heading.grid(row=0, column=1)
    label1=Label(root,text="Input Word",fg="black",bg="dark green")
    label1.grid(row=1,column=0,padx=10)
    label2=Label(root,text="Corrected Word", fg="black",bg="dark green")
    label2.grid(row=3,column=0,padx=10)
    word1=Entry()
    word2=Entry()
    word1.grid(row=1,column=1,padx=10,pady=10)
    word2.grid(row=3,column=1,padx=10,pady=10)
    button1=Button(root,text="Correction", bg="red",fg="black",command=correction)
    button1.grid(row=2,column=1)
    button2=Button(root,text="Clear All", bg="red", fg="black",command=clearall)
    button2.grid(row=4,column=1)
    root.mainloop()