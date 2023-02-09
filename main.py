from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_password():

    chars = string.ascii_letters + string.digits + string.punctuation
    mytext = ''.join(random.choice(chars) for i in range(15))

    password_input.insert(0, mytext)

    pyperclip.copy(mytext)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website_name = website_input.get()
    email_name = email_input.get()
    password_name = password_input.get()

    if len(website_name) < 1 or len(password_name) < 1:
        messagebox.showerror(title="Error", message="Please enter all fields")

    else:

        is_ok = messagebox.askokcancel(title=website_name, message=f'These are the details entered :\n '
                                                           f'Email: {email_name} \n Password: {password_name} '
                                                           f'\n Is it ok to Save ')

        if is_ok :

            f = open('demo-file.txt', 'a')
            f.write(f'{website_name} | {email_name} | {password_name}\n')
            f.close()

            website_input.delete(0, END)
            #email_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.title("Password Manager")
window.config(width=400, height=400, pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)

email_input = Entry(width=35)
email_input.grid(row=2, columnspan=2, column=1)
email_input.insert(0, "test@testemail.com")

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

password_input = Entry(width=18)
password_input.grid(row=3, column=1)

gen_password_button = Button(text="Generate Password", command=gen_password)
gen_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=30 ,command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
