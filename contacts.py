from tkinter import *
from tkinter import messagebox
from db import Database

db = Database("contacts.db")

root = Tk()
root.geometry("800x500")
root.config(bg = '#e1e1e3')

# poulate list with conacts
def populate_list():
    list.delete(0,END)
    for row in db.fetch():
        list.insert(END, row)

# add button fontction
def add_contact ():
    if last_name_text.get() == '' or first_name_text.get() == '' or email_adress_text.get() =='' or phone_number_text =='':
        messagebox.showerror('Error', 'theres is one or more field that is empty ! please check your input ! ')
    else :
        db.insert(first_name_text.get(),last_name_text.get(), email_adress_text.get(),phone_number_text.get())
        list.delete(0,END)
        list.insert(END,(first_name_text.get(),last_name_text.get(), email_adress_text.get(),phone_number_text.get()))
        clear_field()
        populate_list()

def select_item(event):
    try:
        global selected_item
        index = list.curselection()[0]
        selected_item = list.get(index)

        first_name_text.set(selected_item[1])
        last_name_text.set(selected_item[2])
        email_adress_text.set(selected_item[3])
        phone_number_text.set(selected_item[4])

    except IndexError:
        pass


def delete_contact():
    db.remove(selected_item[0])
    clear_field()
    populate_list()

def update_contact ():
    db.update(selected_item[0],first_name_text.get(),last_name_text.get(), email_adress_text.get(),phone_number_text.get())
    populate_list()

def clear_field():
    first_name_text.set('')
    last_name_text.set('')
    email_adress_text.set('')
    phone_number_text.set('')


# creating main labels
# first name of the contact
first_name_text = StringVar()
# label
first_name_label = Label(root, text = 'First Name : ', bg = '#e1e1e3',fg = 'black', font = ("Helvetica", 15))
first_name_label.place(x = 10, y = 10)
# entry
first_name_entry = Entry(root,text = first_name_text, bg = '#e1e1e3', font = ("helvetica", 15)).place(x = 150, y = 10)

# last name of the contact
last_name_text = StringVar()
# label
last_name_lebel = Label(root, text = 'Last Name : ', bg = '#e1e1e3', font = ("Helvetica", 15))
last_name_lebel.place(x = 400, y = 10)
# entry
last_name_entry = Entry(root,text = last_name_text, bg = '#e1e1e3', font = ("helvetica", 15)).place(x = 550, y = 10)

# email adress
email_adress_text = StringVar()
email_adress_label = Label(root, text = 'Email Adress :', bg = '#e1e1e3',fg = 'black', font = ("Helvetica", 15))
email_adress_label.place(x = 10, y = 50)
# entry
email_adress_entry = Entry(root,text = email_adress_text, bg = '#e1e1e3', font = ("helvetica", 15)).place(x = 150, y = 50)

# phone_number of the contact
phone_number_text = StringVar()
# label
phone_number_lebel = Label(root, text = 'Phone Number :', bg = '#e1e1e3', font = ("Helvetica", 15))
phone_number_lebel.place(x = 400, y = 50)
# entry
phone_number_entry = Entry(root,text = phone_number_text, bg = '#e1e1e3', font = ("helvetica", 15)).place(x = 550, y = 50)

# adding a add buton
add_button = Button(root, text = "Add Contact" ,font= ("Helvetica", 15),width = 12, command = add_contact)
add_button.place(x  = 20, y = 120)

# delete button
delete_button = Button(root, text = "Delete Contact" ,font= ("Helvetica", 15),width = 12, command = delete_contact)
delete_button.place(x  = 200, y = 120)

# update button
update_button = Button(root, text = "Update contact" ,font= ("Helvetica", 15), width = 12, command = update_contact)
update_button.place(x  = 400, y = 120)

# clear button
clear_button = Button(root, text = "Clear field" ,font= ("Helvetica", 15), width = 12, command = clear_field)
clear_button.place(x  = 600, y = 120)

# list box
list = Listbox(root, height = 16, width = 100)
list.place(x = 10, y = 200)
# adding a scrollbar
scrollbar = Scrollbar(root)
scrollbar.place(x = 612, y = 200)
#link the scrookbar
list.configure(yscrollcommand = scrollbar.set)
scrollbar.configure(command= list.yview)
# bind select
list.bind('<<ListboxSelect>>', select_item)

populate_list()


root.mainloop()