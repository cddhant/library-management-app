from tkinter import *
from tkinter import messagebox
import mysql.connector
 
def viewBooks():
 
    global id
 
    window=Tk()
    window.title('Library Management System')

    window.geometry("800x600")
 
    greet = Label(window, font = ('Segoe UI', 30, 'bold'), text = "View Books")
    greet.grid(row = 0,columnspan = 3)
 
    db = mysql.connector.connect(host ="localhost",user = "root",password = 'Siddhant#007', database='libdb')
    cursor = db.cursor()
 
    sqlquery= "select * from books ;"
    print(sqlquery)
 
    try:
        cursor.execute(sqlquery)
        # db.commit()
        L = Label(window, font = ('Segoe UI', 20), text = "%-10s%-20s%-20s%-20s"%('BID','Title','Author','Available'))
        L.grid(row = 1,columnspan = 4)
 
        L = Label(window, font = ('Segoe UI', 20), text = "----------------------------------------------------------------")
        L.grid(row = 2,columnspan = 4)
 
        x=4
        for i in cursor:
            L = Label(window, font = ('Segoe UI', 15), text = "%-10s%-20s%-20s%-20s"%(i[0],i[1],i[2],i[3]))
            L.grid(row = x,columnspan = 4)
            x+=1   
 
    except:
        messagebox.showinfo("Error","Cannot Fetch data.")
    
    print("view")
    pass