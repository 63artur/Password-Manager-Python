from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    import random
    password_entry.delete(0,'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]
    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char

    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        return

    new_data = {website: {"email": email, "password": password}}

    try:
        with open("data.json", "r") as data_file:
            content = data_file.read()
            if not content:
                data = {}
            else:
                data = json.loads(content)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    data.update(new_data)

    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

    website_entry.delete(0, 'end')
    password_entry.delete(0, 'end')





# ---------------------------- SEARCH ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found")
    else:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
            if website in data:
                messagebox.showinfo(title="Founded!", message=f"Email: {data[website]['email']}\n Password: {data[website]['password']}")
                website_entry.delete(0, 'end')
            else:
                messagebox.showerror(title="Error", message="Not details for the webiste:")
# ---------------------------- UI SETUP ------------------------------- #
import tkinter
window = tkinter.Tk()
window.title("Mypass")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
mypass = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass)
canvas.grid(column=1, row=0, columnspan=2)

label_website = tkinter.Label(text="Website:")
label_website.grid(column=0, row=1, sticky="e")
website_entry = tkinter.Entry(width=32)
website_entry.grid(column=1, row=1, sticky="w")
website_entry.focus()
search_button = tkinter.Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

label_email = tkinter.Label(text="Email/Username:")
label_email.grid(column=0, row=2, sticky="e")
email_entry = tkinter.Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_entry.insert(0, "twojemail@gmail.com")

label_password = tkinter.Label(text="Password:")
label_password.grid(column=0, row=3, sticky="e")
password_entry = tkinter.Entry(width=32)
password_entry.grid(column=1, row=3, sticky="w")
password_button = tkinter.Button(text="Generate Password", width=14, command=generate)
password_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2, pady=5)
window.mainloop()