from cgitb import text
from ctypes import alignment
from email.mime import image
from ipaddress import collapse_addresses
from tkinter import *
from turtle import left
from tkinter import messagebox

FONT_NAME = "Courier"
YELLOW = "#f7f5dd"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_field.get()
    e = email_field.get()
    password = password_field.get()

    if website == '':
        messagebox.showwarning(title=f'{website}', message='Please enter website')
        website_field.focus()
    elif password == '':
        messagebox.showwarning(title=f'{password}', message='Please enter password')
        password_field.focus()
    elif e == '':
        messagebox.showwarning(title=f'{e}', message='Please enter email')
        email_field.focus()
    else:
        # messagebox.showinfo(title='Title', message='Message')
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \n' 
                                                    f'Email: {e}' 
                                                    f'\nPassword: {password}\n' 
                                                    '\nIs it ok to save?')
        if is_ok:
            with open('pass.txt', 'a') as f:
                f.write(f'{website} | {e} | {password}\n')
                website_field.delete(0, END)
                password_field.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title('Password Manager')
windows.config(padx=50, pady=50)

#Image
canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=0, columnspan=3) 


#Labels
website_text = Label(text='Website:', padx=3, pady=5)
website_text.grid(row=1, column=0) #sticky=E 
email = Label(text='Email/Username:') #padx=3, pady=5
email.grid(row=2, column=0) #sticky=E
password = Label(text='Password:') #padx=3, pady=5
password.grid(row=3, column=0) #sticky=E
test_label = Label()
test_label.grid(row=6, column=0)

#Fields
website_field = Entry(width=39)
website_field.grid(row=1, column=1, columnspan=2, sticky=W)
website_field.focus()
email_field = Entry(width=39)
email_field.grid(row=2, column=1, columnspan=2, sticky=W)
email_field.insert(0, 'r.serogka@gmail.com')
password_field = Entry(width=20, show='*')
password_field.grid(row=3, column=1, sticky=W) #sticky=W



#Buttons
password_generate = Button(text='Generate Password')
password_generate.grid(row=3, column=1, sticky=E) 
add = Button(text='Add', width=33, command=save)
add.grid(row=4, column=1, columnspan=1)

windows.mainloop()