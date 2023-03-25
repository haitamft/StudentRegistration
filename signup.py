from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient
import os
client = MongoClient('localhost', 27017)
db = client['user_database']
collection = db['users']

def signup():
    username = user.get()
    password = passW.get()
    email = emails.get()

    if username == 'Username' or password == 'Password' or email == 'Email' or username == '' or password == '' or email == '':
        messagebox.showerror('Invalid','Please fill out all fields')

    else:
        users = {'username': username, 'password': password, 'email': email}
        collection.insert_one(users)
        messagebox.showinfo("Success", "The acounte created successfully!")
        root.destroy()
        os.system('python login.py')


def signin():
    root.destroy()
    os.system('python login.py')


root = Tk()
root.title('Signup Page')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)


img = PhotoImage(file="login.png")


Label(root,image=img, bg='white').place(x=50, y=100)
frame=Frame(root, width=350, height=350, bg="white") 
frame.place(x=480, y=70)
heading=Label(frame, text='Sign Up',fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold')) 
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


def on_enter(e):
    emails.delete(0, 'end')

def on_leave(e):
    name=emails.get()
    if name=='':
        emails.insert(0,'Email')


emails = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11)) 
emails.place(x=30,y=180)
emails.insert(0,'Email')
emails.bind('<FocusIn>',on_enter)
emails.bind('<FocusOut>',on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=210)




Button(frame, width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0,command=signup).place(x=35, y=235) 
label=Label(frame, text="Already have an acounte", fg='black', bg='white', font=('Microsoft YaHei UI Light',9)) 
label.place(x=75, y=280)



sign_in= Button(frame,width=6, text='Login', border=0, bg='white', cursor='hand2', fg='#57a1f8',command=signin)
sign_in.place(x=214,y=281)

root.mainloop()









    