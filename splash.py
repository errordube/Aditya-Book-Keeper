#importing modules
from tkinter import *
root = Tk()
root.title("171B017")
root.config(bg='powder blue')#bg color of the screen
root.geometry("850x450")#specifying the screen size
img1=PhotoImage(file="screen.gif")#image extension
def fun(e):
    root.destroy()

lb=Label(root,image=img1,bd=3,relief="solid")
lb1=Label(root,text='Aditya Dube',font=('comic sans MP', 20 ,'bold'),bg='orangered',bd=3)
lb.bind('<Motion>',fun)#The mouse is moved with a mouse button being held down. 
lb.pack()
lb1.pack()
Label(root,text='171B017',font=('comic sans MP', 20 ,'bold'),bg='orangered',bd=3).pack()
Label(root,text='B1',font=('comic sans MP', 20 ,'bold'),bg='orangered',bd=3).pack()
Label(root,text='Email Id: dube.aditya8@gmail.com',font=('comic sans MP', 20 ,'bold'),bg='orangered',bd=3).pack()
Label(root,text='Mob.: 9717376337',font=('comic sans MP', 20 ,'bold'),bg='orangered',bd=3).pack()





root.mainloop()


#©Aditya Dube

