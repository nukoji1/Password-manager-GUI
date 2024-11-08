from re import search
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    lett = [ random.choice(letters) for char in range(nr_letters) ]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    sym = [random.choice(symbols) for char in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    num = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = lett+sym+num
    random.shuffle(password_list)

    password = "".join(password_list)

    # for char in password_list:
    #   password += char
    password_entry.insert(0,password)
    pyperclip.copy(password) #This copies the newly generated password to my computers clipboard

    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    # messagebox.showinfo(title = "Click Ok to proceed", message= "Do you want to proceed to enter new information?")
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password" : password,
        }

    }

    if len(password) == 0 or len(website) == 0 or len(email) == 0:
        messagebox.showwarning(title="Oooops!!", message="Please do not leave any fields empty")
    else:
        try:
            with open("my_passwords.json", "r") as file:
                # Read old data
                data = json.load(file)

        except FileNotFoundError:
            with open("my_passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            # updating old data with new data
            data.update(new_data)
            with open("my_passwords.json", "w") as file:
                #Saving updated data
                json.dump(data, file, indent=4)

        finally:
            website_entry.delete(0, 'end')
            email_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
# ---------------------------- Search Function ------------------------------- #
def search_password():
    website = website_entry.get()
    try:
        with open("my_passwords.json", "r") as file:
            stored_data = json.load(file)
            retrieved_email = stored_data[website]["email"]
            retrieved_password = stored_data[website]["password"]
    except KeyError:
            messagebox.showwarning("Ooops", message= "Website name not in password list")
    else:
        messagebox.showinfo(f"Login for {website}", f"Email: {retrieved_email} \nPassword: {retrieved_password}")
        # print(stored_data["Amazon"]["email"])

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)#, bg= "white")
canvas = Canvas(width= 200, height = 200)#, bg= "white", highlightthickness= 0)
password_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = password_img)
canvas.grid(row = 0, column = 1)

website_label = Label(text="Website:")#, font= ("Arial", 10, "bold"), bg = "white")
website_label.grid(row = 1, column = 0)

website_entry = Entry(width= 32)
website_entry.grid(row = 1, column = 1, columnspan = 1)
website_entry.focus()

email_label = Label(text="Email/Username:")#, font= ("Arial", 10, "bold"), bg = "white")
email_label.grid(row = 2, column = 0)

email_entry = Entry(width= 50)
# email_entry.index(0, "your email") #This inserts your email as a default string
email_entry.grid(row = 2, column = 1, columnspan = 2)


password_label = Label(text="Password:")#, font= ("Arial", 10, "bold"), bg = "white")
password_label.grid(row = 3, column = 0)

password_entry = Entry(width= 32)
password_entry.grid(row = 3, column = 1)

password_button = Button(text="Generate Password", command= generate_password)#, font= ("Arial", 10, "bold"), bg = "white")
password_button.grid(row = 3, column = 2)

add_button = Button(text="Add", width= 43, command= save_password)#, font= ("Arial", 10, "bold"), bg = "white")
add_button.grid(row = 4, column = 1, columnspan = 2)

search_button = Button(text="Search", padx = 31, command= search_password)
search_button.grid(row = 1, column = 2, columnspan = 1)

window.mainloop()