from tkinter import *
from tkinter import messagebox
import mysql.connector

def delete_db():
 
    global id
 
    bid=id.get()
    
    db = mysql.connector.connect(host ="localhost",user = "root",password = 'Siddhant#007',database='libdb')
    cursor = db.cursor()
    
    print(bid,end='--')
    print("delete")
 
    sqlquery= "delete from books where bid='"+bid+"';"
    print(sqlquery)
 
    try:
        cursor.execute(sqlquery)
        db.commit()
        messagebox.showinfo('Success',"Book deleted Successfully")
    except:
        messagebox.showinfo("Error","Book with given id does not exist")
    
    window = Tk()
    window.destroy()
 
def deleteBooks():
 
    global id
 
    window=Tk()
    window.title('Library Management App')

    window.geometry("800x600")
 
    greet = Label(window, font = ('Segoe UI', 30, 'bold'), text = "Delete Books")
    greet.grid(row = 0,columnspan = 3)
 
    #----------id-------------------
 
    L = Label(window, font = ('Segoe UI', 15, 'bold'), text = "Enter Book id: ")
    L.grid(row = 2, column = 1)
 
    L = Label(window, font = ('Segoe UI', 15, 'bold'), text = "   ")
    L.grid(row = 2, column = 2)
 
    id=Entry(window,width=5,font =('Segoe UI', 15, 'bold'))
    id.grid(row=2,column=3)
 
    submitbtn=Button(window,text="Submit",command=delete_db,bg="DodgerBlue2",fg="white",font = ('Segoe UI', 15, 'bold'))
    submitbtn.grid(row=8,columnspan=3)
        
    print("delete")
    pass