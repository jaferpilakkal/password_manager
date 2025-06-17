from tkinter import *
from tkinter import messagebox, ttk
import pyperclip
import json
import random
import os

# Colors
bg = "#F5FFFF"      # light blue
button_bg = "#E9F5F5"  # button blue
entry_bg = "white"   # white entry background

# Password generator components
letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!#$%&()*+")

def generate_new_pass():
    password = "".join(
        [random.choice(letters) for _ in range(random.randint(8, 10))] +
        [random.choice(symbols) for _ in range(random.randint(2, 4))] +
        [random.choice(numbers) for _ in range(random.randint(2, 4))]
    )
    password_field.delete(0, END)
    password_field.insert(0, password)
    pyperclip.copy(password)

def store_data():
    website = website_field.get().title()
    email = email_field.get()
    password = password_field.get()

    if not website or not email or not password:
        messagebox.showerror("Oops", "Please fill all fields.")
        return

    new_data = {website: {"email": email, "password": password}}

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        data = new_data
    else:
        data.update(new_data)

    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

    website_field.delete(0, END)
    password_field.delete(0, END)
    messagebox.showinfo("Success", "Your password has been saved!")

def search():
    website = website_field.get().title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            credentials = data[website]

            # Create a Toplevel instead of messagebox
            top = Toplevel()
            top.title(website)

            Label(top, text="Username or Email:").grid(row=0, column=0, sticky='w')
            email =Entry(top, width=40)
            email.grid(row=0, column=1)
            email.insert(0, credentials['email'])

            Label(top, text="Password:").grid(row=1, column=0, sticky='w')
            password =Entry(top, width=40)
            password.grid(row=1, column=1)
            password.insert(0, credentials['password'])

    except FileNotFoundError:
        messagebox.showerror("Error", "No data file found.")
    except KeyError:
        messagebox.showerror("Error", f"No details for {website} found.")

# UI setup
root = Tk()
root.title("Password Manager")
root.config(bg=bg, padx=20, pady=20)

# Style setup
style = ttk.Style()
style.theme_use('default')
style.configure("TLabel", background=bg, font=('courier', 11))
style.configure("TEntry", fieldbackground=entry_bg, font=('courier', 11), padding = 5)
style.configure("TButton", background=button_bg, font=('courier', 11))

# Logo
script_dir = os.path.dirname(os.path.abspath(__file__))
logo_file = os.path.join(script_dir, "logo.png")
logo = PhotoImage(file=logo_file)

canvas = Canvas(root, height=200, width=200, highlightthickness=0, bg=bg)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
ttk.Label(root, text="Website:").grid(column=0, row=1, sticky='E', pady=5)
ttk.Label(root, text="Email/Username:").grid(column=0, row=2, sticky='E', pady=5)
ttk.Label(root, text="Password:").grid(column=0, row=3, sticky='E', pady=5)

# Entries
website_field = ttk.Entry(root, width=35)
website_field.grid(column=1, row=1, sticky='EW', pady=5, padx = (0,3))
website_field.focus()

email_field = ttk.Entry(root, width=35)
email_field.grid(column=1, row=2, sticky='EW', pady=5)
email_field.insert(0, "yourname@gmail.com")

password_field = ttk.Entry(root, width=21)
password_field.grid(column=1, row=3, sticky='EW', pady=5, padx = (0,3))

# Buttons
ttk.Button(root, text="Search", command=search).grid(column=2, row=1, sticky='EW', pady=5)
ttk.Button(root, text="Generate Password", command=generate_new_pass).grid(column=2, row=3, sticky='EW', pady=5)
ttk.Button(root, text="Add", command=store_data).grid(column=1, row=4, columnspan=2, sticky='EW', pady=10)

root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)


def view_all():
    """Open a new window with all credentials in a Text widget (copyable) """
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No data file found.")
        return

    view = Toplevel(root)
    view.title("All Credentials")
    view.config(bg=bg)

    text = Text(view, wrap='word', font = ("courier", 12, "normal"))
    text.pack(fill='both', expand=True, padx=10, pady=10)

    for website, credentials in data.items():
        text.insert(END, f"Website: {website}\nUsername: {credentials['email']}\nPassword: {credentials['password']}\n\n")

    text.config(state='normal')  # Allow copying

def about():
    """Open a small window with information about the app in a Text widget."""
    view = Toplevel(root)
    view.title("About")
    view.config(bg=bg)

    text = Text(view, wrap='word', font= ("arial",14,"normal"))
    text.pack(fill='both', expand=True, padx=10, pady=10)

    text.insert(END, "This password manager lets you:\n- Store credentials safely offline\n- Retrieve credentials quickly\n (Use search button after entering website name)\n- View all credentials at once\n\nDeveloped by MyPass.\nContact: jaferpilakkal@gmail.com")
    text.config(state='normal')

# Smaller style
style.configure("Small.TButton", background="#E9F5F5", font=('courier', 9), padding = 4)

# View All button on left bottom
ttk.Button(root, text="View All", command=view_all, style="Small.TButton").grid(column=0, row=6, sticky='W', pady=(15,0), padx=(0,5))

# About button on right bottom
ttk.Button(root, text="About", command=about, style="Small.TButton").grid(column=2, row=6, sticky='E', pady=(15,0), padx=(5,0))

root.mainloop()
