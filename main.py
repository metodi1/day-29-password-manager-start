from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    new_item=random.choice(letters)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols+password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    entry_password_user.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_into_file():
    status = True
    web_site = entry_web.get()
    email_user = entry_email_user.get()
    password_user = entry_password_user.get()
    line_to_save = f'{web_site} | {email_user} | {password_user}'

    if len(web_site) == 0 or len(password_user) == 0:
        messagebox.showinfo(title="Oops",message="You left same info empty")
        status = False

    result = messagebox.askokcancel(title=web_site, message=f"This is password for {web_site}\n. Is it ok to save")
    if not result:
        status = False

    if status:
        with open('data.txt', "a") as data_file:
            data_file.write(f"{line_to_save}\n")

    entry_web.delete(0, END)
    entry_password_user.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

# ---------------labels------------------------------
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# ------------------entry---------------------------
entry_web = Entry(width=36)
entry_web.grid(column=1, row=1, columnspan=2)
entry_web.focus()
entry_email_user = Entry(width=36)
entry_email_user.grid(column=1, row=2, columnspan=2)
entry_email_user.insert(0, "metodi")
entry_password_user = Entry(width=21)
entry_password_user.grid(column=1, row=3, columnspan=2)

# ---------------buttons---------------------------
generate_button = Button(text="Generate", command=password_generator)
generate_button.grid(column=2, row=3, )

add_button = Button(text="Add", width=30, command=add_into_file)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
