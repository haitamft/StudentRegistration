from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient
import os


client = MongoClient('localhost', 27017)
db = client['user_database']
users = db['users']

def login():
    username = user.get()
    password = passW.get()

    userr = users.find_one({'username': username, 'password': password})

    if userr:
        messagebox.showinfo("Success", "Welcome "+username+" !" )
        root.destroy()
        os.system('python main.py')
    else:
        messagebox.showerror('Invalid','Invalid username or password')


def signup():
    root.destroy()
    os.system('python signup.py')



root = Tk()
root.title('Login Page')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)


img = PhotoImage(file="signin.png")


Label(root,image=img, bg='white').place(x=50, y=80)
frame=Frame(root, width=350, height=350, bg="white") 
frame.place(x=480, y=70)
heading=Label(frame, text='Login',fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold')) 
heading.place(x=100, y=5)



def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')


user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11)) 
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=110)


def on_enter(e):
    passW.delete(0, 'end')
    passW.config(show="*")
def on_leave(e):
    name=passW.get()
    if name=='':
        passW.config(show="")
        passW.insert(0,'Password')


passW = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11)) 
passW.place(x=30,y=130)
passW.insert(0,'Password')
passW.bind('<FocusIn>',on_enter)
passW.bind('<FocusOut>',on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=160)



Button(frame, width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0,command=login).place(x=35, y=190) 
label=Label(frame, text="I don't have an acounte ?", fg='black', bg='white', font=('Microsoft YaHei UI Light',9)) 
label.place(x=75, y=250)





sign_in= Button(frame,width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a1f8',command=signup)
sign_in.place(x=220,y=251)

root.mainloop()









    









