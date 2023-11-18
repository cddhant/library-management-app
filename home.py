from tkinter import *
import mysql.connector
 
from add import *
from delete import *
from issue import * 
from Return import *
from view import *
 
db = mysql.connector.connect(host ="localhost", user = "root", password = 'paassword', database='libdb')
cursor = db.cursor()
 
window=Tk()
window.title("Library Management App")

window.geometry("800x600")
 
greet = Label(window, font = ('Segoe UI', 30, 'bold'), text = "Welcome!")
greet.grid(row = 0,columnspan = 3)
 
addbtn=Button(window,text="Add Books",command=addBooks,bg="aqua",fg="white",font = ('Segoe UI', 20, 'bold'))
addbtn.grid(row=3,columnspan=3)
 
deletebtn=Button(window,text="Delete Books",command=deleteBooks,bg="aquamarine4",fg="white",font = ('Segoe UI', 20, 'bold'))
deletebtn.grid(row=5,columnspan=3)
 
issuebtn=Button(window,text="Issue Books",command=issueBooks,bg="aquamarine2",fg="white",font = ('Segoe UI', 20, 'bold'))
issuebtn.grid(row=7,columnspan=3)
 
returnbtn=Button(window,text="Return Books",command=returnBooks,bg="aquamarine3",fg="white",font = ('Segoe UI', 20, 'bold'))
returnbtn.grid(row=9,columnspan=3)
 
viewbtn=Button(window,text="View Books",command=viewBooks,bg="aquamarine1",fg="white",font = ('Segoe UI', 20, 'bold'))
viewbtn.grid(row=11,columnspan=3)
 
greet = Label(window, font = ('Segoe UI', 15, 'bold'), text = "Thank you")
greet.grid(row = 13,columnspan = 3)
 
window.mainloop()