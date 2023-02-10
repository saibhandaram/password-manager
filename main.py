from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip
import json


# ------------------------- Search --------------------------------------------- #
def search_website():
    website_info = website_input.get()
    if len(website_info) == 0:
        messagebox.showinfo(title="error", message="Please enter website info")
    else:
        # Read the JSON File and place in dictionary
        try:
            with open("datafile.json", "r") as datafile:
                data_json = json.load(datafile)
        except:
            messagebox.showinfo(title="Error", message="File not found")

        else:

            if website_info in data_json:
                email_info = data_json[website_info]["email"]
                password_info = data_json[website_info]["password"]

                messagebox.showinfo(title=website_info, message=f"Email is {email_info} \n password is {password_info}")

            else:
                messagebox.showinfo(title="Error", message="Website not found")


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

    newdata = {
        website_name:
            {
                "email": email_name,
                "password": password_name,

            }
    }

    if len(website_name) < 1 or len(password_name) < 1:
        messagebox.showerror(title="Error", message="Please enter all fields")

    else:

        is_ok = messagebox.askokcancel(title=website_name, message=f'These are the details entered :\n '
                                                                   f'Email: {email_name} \n Password: {password_name} '
                                                                   f'\n Is it ok to Save ')

        if is_ok:

            try:
                # read the file
                f = open("datafile.json", "r")
                data = json.load(f)
                data.update(newdata)
            except FileNotFoundError:
                f = open("datafile.json", "w")
                json.dump(newdata, f, indent=1)
            else:
                # update the data
                f = open("datafile.json", "w")
                json.dump(data, f, indent=4)
            finally:
                f.close()
                website_input.delete(0, END)
                # email_input.delete(0, END)
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

website_input = Entry(width=20)
website_input.grid(row=1, column=1)
website_input.focus()

search_button = Button(text="Search", width=15, command=search_website)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)

email_input = Entry(width=40)
email_input.grid(row=2, columnspan=2, column=1)
email_input.insert(0, "test@testemail.com")

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

password_input = Entry(width=20)
password_input.grid(row=3, column=1)

gen_password_button = Button(text="Generate Password", command=gen_password)
gen_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=30, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
