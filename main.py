import datetime as dt
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pymongo import *

cnx = MongoClient("mongodb://localhost:27017")
db = cnx.G_Students
        
Data_list = []

app = Tk()

app_width = 1050
app_height = 655
center_width = int((app.winfo_screenwidth() / 2) - (app_width / 2))
center_height = int((app.winfo_screenheight() / 2) - (app_height / 2))
app.geometry(f"{app_width}x{app_height}+{center_width}+{center_height}")
app.resizable(False, False)

#APP Functions:
##function that clears all the items present in Treeview
def clear_all():
    for item in tree.get_children():
      tree.delete(item)

def refresh_treeView():
    for item in tree.get_children():
      tree.delete(item)
    for student in db.Students.find():
        tree.insert('', END, values=(student['FullName'], student['PlaceOfBirth'], student['BirthDate'], student['Gender'], student['PhoneNumber'], student['MoreInfo']))

def search_by_name(event):
    match s_n.get():
        case "":
            refresh_treeView()
            messagebox.showwarning(title='Empty Field', message='Please Fill out all the name field correctly')
        case _:
            clear_all()
            for student in db.Students.find({"FullName": s_n.get()}):
                tree.insert('', END, values=(student['FullName'], student['PlaceOfBirth'], student['BirthDate'], student['Gender'], student['PhoneNumber'], student['MoreInfo']))


def search_by_phone(event):
    match s_p.get():
        case "":
            refresh_treeView()
            messagebox.showwarning(title='Empty Field', message='Please Fill out all the phone number field correctly')
        case _:
            clear_all()
            for student in db.Students.find({"PhoneNumber": s_p.get()}):
                tree.insert('', END, values=(student['FullName'], student['PlaceOfBirth'], student['BirthDate'], student['Gender'], student['PhoneNumber'], student['MoreInfo']))

def Add_student():
    fn = full_name.get()
    pob = place_of_birth.get()
    g = gender.get()
    ph = phone.get()
    mi = More_info.get()
    b2 = Birthdate_2.get()
    if len(fn)==0 or len(pob)==0 or ph==0 or len(mi)==0 or len(b2)==0:
        messagebox.showwarning(title='Empty Fields', message='Please Fill out all the fields correctly')
    else:
        db.Students.insert_one({'FullName': fn, 'PlaceOfBirth': pob, 'BirthDate': b2, 'Gender': g, 'PhoneNumber': str(ph), 'PhotoPath': "", 'MoreInfo': mi})
        ##Empty all the fields:
        Full_name_entry.delete(0, END)
        Place_of_birth_entry.delete(0,END)
        phone.set(212)
        photo_path.set('')
        More_info.set('')
        ##Refreshing TreeView
        refresh_treeView()
        messagebox.showinfo(title='Message', message='Student has been added successfully!')



def Delete_student():
    selected_items = tree.selection()
    match len(selected_items):
        case 0:
            messagebox.showwarning(title='No student selected', message='Please select a student to delete')
        case _:
            for item in selected_items:
                temp = tree.item(item, 'values')
                db.Students.delete_one({'FullName': temp[0], 'PlaceOfBirth': temp[1], 'BirthDate': temp[2], 'Gender': temp[3], 'PhoneNumber': temp[4], 'MoreInfo': temp[5]})
    refresh_treeView()
    messagebox.showinfo(title='Message', message='Student has been deleted successfully!')

    
def Edit_student():
    selected = tree.focus()
    match selected:
        case "":
            messagebox.showwarning(title='No student selected', message='Please select a student to modify')
        case _:
            fn = full_name.get()
            pob = place_of_birth.get()
            g = gender.get()
            ph = phone.get()
            mi = More_info.get()
            b2 = Birthdate_2.get()
            if len(fn)==0 or len(pob)==0 or ph==0 or len(mi)==0 or len(b2)==0:
                messagebox.showwarning(title='Empty Fields', message='Please Fill out all the fields correctly')
            else:
                temp = tree.item(selected, 'values')
                db.Students.update_one({'FullName': temp[0], 'PlaceOfBirth': temp[1], 'BirthDate': temp[2], 'Gender': temp[3], 'PhoneNumber': temp[4], 'MoreInfo': temp[5]}, {"$set": {'FullName': fn, 'PlaceOfBirth': pob, 'BirthDate': b2, 'Gender': g, 'PhoneNumber': str(ph), 'PhotoPath': "", 'MoreInfo': mi}})
                refresh_treeView()
                messagebox.showinfo(title='Message', message='Student has been modified successfully!')


def Browse():
    image_path = filedialog.askopenfilename(title='Select Your Image:', filetypes=(('PNG Image', '*.png'),('JPG Image', '*.jpg'), ('GIF image', '*.gif')))
    photo_path.set(image_path)
#APP HEADER
title_label = Label(app, text='Student Registration', fg='White', bg='lightblue', font=('Times', 30, 'bold'), width=20)
title_label.grid(row=0, column=0)
#Searching section
search_section_label = ttk.Labelframe(app, text='Search by:',  width=475, height=100)
search_section_label.grid(row=1, column=0)
##Searching Labels
search_name_label = ttk.Labelframe(search_section_label, text='Name', labelanchor=N, width=230, height=50)
search_name_label.grid(row=0,column=0, padx=5, pady=5, sticky=W)
search_phone_label = ttk.Labelframe(search_section_label, text='Phone', labelanchor=N, width=230, height=50)
search_phone_label.grid(row=0,column=1, padx=5, pady=5, sticky=E)
##Searching Entries
s_n = StringVar()
s_p = StringVar()

search_name_entry = ttk.Entry(search_name_label, textvariable=s_n, width=36)
search_name_entry.bind('<Return>', search_by_name)
search_name_entry.grid()
search_phone_entry = ttk.Entry(search_phone_label, textvariable=s_p, width=36)
search_phone_entry.bind('<Return>', search_by_phone)
search_phone_entry.grid()

#Data
##Data Variables:
full_name = StringVar()
place_of_birth = StringVar()
#gender_male = IntVar()
gender = StringVar()
#gender_female = IntVar()
phone = IntVar()
phone.set(212)
photo_path = StringVar()
More_info = StringVar()
Birthdate_2 = StringVar()
##Data Labels
Full_name_label = ttk.Labelframe(app, text='Full Name:', width=475, height=100)
Full_name_label.grid(row=2, column=0)

Place_of_birth_label = ttk.Labelframe(app, text='Place of Birth::', width=475, height=100)
Place_of_birth_label.grid(row=3, column=0)

Birthdate_form_2 = ttk.Labelframe(app, text='Birthdate: ', width=475, height=100)
Birthdate_form_2.grid(row=4, column=0)

Gender_label = ttk.Labelframe(app, text='Gender:', width=475, height=100)
Gender_label.grid(row=5, column=0)


Phone_label = ttk.Labelframe(app, text='Phone Number: ', width=475, height=100)
Phone_label.grid(row=6, column=0)

Photo_label = ttk.Labelframe(app, text='Photo:', width=475, height=100)
Photo_label.grid(row=7, column=0)

More_label = ttk.Labelframe(app, text='More Info:', width=475, height=100)
More_label.grid(row=8, column=0)
##Data Entries
Full_name_entry = ttk.Entry(Full_name_label, textvariable=full_name, width=75)
Full_name_entry.grid(padx=10, pady=10)

Place_of_birth_entry = ttk.Entry(Place_of_birth_label, textvariable=place_of_birth, width=75)
Place_of_birth_entry.grid(padx=10, pady=10)

Birthdate_form_2_entry = DateEntry(Birthdate_form_2, textvariable=Birthdate_2, width=72)
Birthdate_form_2_entry.grid(padx=10, pady=10)

Gender_male_entry = ttk.Radiobutton(Gender_label, text='Male', value='Male', var=gender, width=32)
Gender_male_entry.grid(row=0, column=0, padx=10, pady=10, sticky=W)
Gender_female_entry = ttk.Radiobutton(Gender_label, text='Female', value='Female', var=gender, width=32)
Gender_female_entry.grid(row=0, column=1, padx=10, pady=10, sticky=E)

Phone_entry = ttk.Entry(Phone_label, textvariable=phone, width=75)
Phone_entry.grid(padx=10, pady=10)

Photo_entry = ttk.Entry(Photo_label, textvariable=photo_path, width=75)
Photo_entry.grid(row=0, column=0, padx=10, pady=10, sticky=W)
Photo_browse_button = ttk.Button(Photo_label, text='Browse', command=Browse)
Photo_browse_button.grid(row=0, column=0, padx=10, pady=10, sticky=E)

More_info_entry = ttk.Entry(More_label, textvariable=More_info, width=75)
More_info_entry.grid(padx=10, pady=10)

#Options:
##Options Label:
Options_label = ttk.Labelframe(app, text='Options:', width=475, height=100, labelanchor=N)
Options_label.grid(row=9, column=0)

##Options Buttons:
Add_student = ttk.Button(Options_label, text='Add student', command=Add_student)
Add_student.grid(row=0, column=0, padx=10, pady=10, sticky=W)

Delete_student = ttk.Button(Options_label, text='Delete student', command=Delete_student)
Delete_student.grid(row=0, column=2, padx=10, pady=10, sticky=E)

Edit_student = ttk.Button(Options_label, text='Edit student', command=Edit_student)
Edit_student.grid(row=1, column=0, padx=10, pady=10, sticky=W)

Exit_student = ttk.Button(Options_label, text='Exit', command=app.quit)
Exit_student.grid(row=1, column=2, padx=10, pady=10, sticky=E)

#Showing Data in TreeView

tree = ttk.Treeview(app, columns=(1, 2, 3, 4, 5, 6), show='headings')
##TreeView Headers
tree.heading(1, text='Full Name')
tree.heading(2, text='Place of Birth')
tree.heading(3, text='Birthdate')
tree.heading(4, text='Gender')
tree.heading(5, text='Phone')
tree.heading(6, text='More Info')
##TreeView Header Config
tree.column(1, width=25)
tree.column(2, width=15)
tree.column(3, width=15)
tree.column(4, width=5)
tree.column(5, width=20)
tree.column(6, width=30)
##TreeView Position:
tree.place(x=500, y=0, height=650, width=540)

if db.Students.count_documents({}) > 0:
    for student in db.Students.find():
        tree.insert('', END, values=(student['FullName'], student['PlaceOfBirth'], student['BirthDate'], student['Gender'], student['PhoneNumber'], student['MoreInfo']))

#
app.mainloop()