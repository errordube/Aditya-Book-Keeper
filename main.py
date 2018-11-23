#importing all the modules

import sqlite3
from tkinter import *
import tkinter.messagebox
import splash



#All about the database
#applying the concept of object oriented 
class DB:#The __init__ method represents a constructor in Python.
    def __init__(self): #the self variable represents the instance of the object itself
        self.conn=sqlite3.connect("mybooks.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title TEXT, author TEXT, isbn INTEGER )")#creating the table
        self.conn.commit()


    def __del__(self): #this is destrcutor
        self.conn.close()

    #get all books

    def view(self):
        self.cur.execute("SELECT * FROM books") #getting  all the records from the database
        rows = self.cur.fetchall() #get all rows of the db
        return rows

    #insert data

    def insert(self,title,author,isbn):
        self.cur.execute("INSERT INTO books VALUES (NULL,?,?,?)", (title,author,isbn)) #inserting the values in the database
        self.conn.commit()
        self.view()

    
    #update db

    #def update(self,id,title,author,isbn):
        #self.cur.execute("UPDATE books SET title=?,author=?,isbn=? WHERE id=?",(title,author,isbn, id))
        #self.view()
    
        


    #delete from db
    def delete(self,id):
        self.cur.execute("DELETE from books WHERE id=?",(id,)) #deleting the selected record from the database. 
        self.conn.commit()
        self.view()

    #search into db

    def search(self,title="",author="",isbn=""):
        self.cur.execute("SELECT * FROM books WHERE title=? OR author=? OR isbn=?",(title,author,isbn)) #searching in the database
        rows = self.cur.fetchall()
        return rows

db = DB()

def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
    except IndexError:
        pass 

def view_command():
    list1.delete(0,END)
    for row in db.view():
        list1.insert(END,row)
    tkinter.messagebox.showinfo("View All", "All the Data is in the list box")


def search_command():
    list1.delete(0,END)
    for row in db.search(title_text.get(),author_text.get(),isbn_text.get()):
        list1.insert(END,row)
        tkinter.messagebox.showinfo("Searched Data", "Searched Data is in the list box")

def add_command():
    if title_text.get() == '' or author_text.get() == '' or isbn_text.get() == '':
        tkinter.messagebox.showerror("Warning","Please fill up the boxes")
    else:
        db.insert(title_text.get(),author_text.get(),isbn_text.get())
        list1.delete(0,END)
        list1.insert(END,(title_text.get(),author_text.get(),isbn_text.get()))
        tkinter.messagebox.showinfo("Success",str(title_text.get()) + " Successfully Added")
    

def delete_command():
    db.delete(selected_tuple[0])
    view_command()
    tkinter.messagebox.showinfo("Deleted",str(title_text.get()) + " Successfully Deleted")
    

    

#Tkinter Starts
    
root = Tk()

root.title("Aditya Book Keeper")

root.geometry("850x455")

root.config(bg="dodgerblue") #bg color

tops=Frame(root,width=400,height=200)
tops.pack(side=TOP)

a = PhotoImage(file='books.gif')
Label(tops,image=a,bd=5,relief="sunken").grid(row=0,column=1)

bottoms=Frame(root,width=400,height=200,bg='steelblue',borderwidth=3,relief="raised",bd=6)
bottoms.pack(side=BOTTOM)


l1=Label(bottoms,text="Title",bg="#1B76B3",height=2,width=15,bd=5,borderwidth=2,relief="ridge",font='arial 10 bold')
l1.grid(row=1,column=0,padx=2,pady=2)

l2=Label(bottoms,text="Author",bg="#1B76B3",height=2,width=15,bd=5,borderwidth=2,relief="ridge",font='arial 10 bold')
l2.grid(row=1,column=3,padx=2,pady=2)

l3=Label(bottoms,text="ISBN",bg="#1B76B3",height=2,width=15,bd=5,borderwidth=2,relief="ridge",font='arial 10 bold')
l3.grid(row=2,column=0,padx=2,pady=2)

#Entry of the text 
title_text = StringVar()
e1 = Entry(bottoms,textvariable=title_text,borderwidth=2,relief="sunken",bd=6)
e1.grid(row=1,column=1,padx=2,pady=2)

author_text = StringVar()
e2 = Entry(bottoms,textvariable=author_text,borderwidth=2,relief="sunken",bd=6)
e2.grid(row=1, column=4,padx=2,pady=2)

isbn_text = StringVar()
e3 = Entry(bottoms,textvariable=isbn_text,borderwidth=2,relief="sunken",bd=6)
e3.grid(row=2,column=1,padx=2,pady=2)

list1 = Listbox(bottoms,height=6,width=38,borderwidth=5,relief="solid") #listbox
list1.grid(row=5,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(bottoms,borderwidth=5,relief="solid") #scrollbar
sb1.grid(row=5, column=1, columnspan=3,rowspan=5)

list1.configure(yscrollcommand=sb1.set,borderwidth=2,relief="sunken",bd=4) #configuring the scroll bar with list box
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row) #adding the records in the listbox whenever we add the book.

b1 = Button(bottoms,text="View All",width=12,command=view_command,bg="#1B76B3",borderwidth=2,relief="raised",activeforeground="white",activebackground="black",bd=4)
b1.grid(row=5,column=3,padx=2,pady=2,rowspan=1,columnspan=2)

b2 = Button(bottoms,text="Search Entry",width=12,command=search_command,bg="#1B76B3",borderwidth=2,relief="raised",activeforeground="white",activebackground="black",bd=4)
b2.grid(row=6,column=3,padx=2,pady=2,rowspan=1,columnspan=2)

b3 = Button(bottoms,text="Add Entry",width=12,command=add_command,bg="#1B76B3",borderwidth=2,relief="raised",activeforeground="white",activebackground="black",bd=4)
b3.grid(row=7,column=3,padx=2,pady=2,rowspan=1,columnspan=2)

b4 = Button(bottoms,text="Delete Selected",width=12,command=delete_command,bg="#1B76B3",borderwidth=2,relief="raised",activeforeground="white",activebackground="black",bd=4)
b4.grid(row=8,column=3,padx=2,pady=2,rowspan=1,columnspan=2)

b6 = Button(bottoms,text="Close",width=12,command=root.destroy,borderwidth=2,bg="#1B76B3",relief="raised",activeforeground="white",activebackground="black",bd=4)
b6.grid(row=9,column=3,padx=2,pady=2,rowspan=1,columnspan=2)


root.mainloop()


#©Aditya Dube
