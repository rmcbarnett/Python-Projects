# This Tkinter app allows the user to save a list of passwords for websites and search for already saved passwords. 
# The user can also generate a new password randomly if they choose. 


from tkinter import *
from tkinter import messagebox
import random
import json
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generate():
    #Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    #
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)
    password= "".join(password_list)


    print(f"Your password is: {password}")
    password_input.delete(0, END)
    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email":email,
            "password":password
        }



    }

    if len(website) == 0 or len(password) ==0:
        messagebox.showinfo(title = 'Wait a Minute!', message = "Please enter both website and password")

    else:
        try:
            with open('./data.json',"r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # updating old data with new data
                data.update(new_data)

        except FileNotFoundError:
            with open('./data.json', "w") as data_file:
            # Reading old data
                json.dump(new_data, data_file, indent=4)

        else:
            with open('./data.json', "w") as data_file:
                json.dump(data, data_file, indent= 4)
        finally:
            website_input.delete(0,'end')
            password_input.delete(0,'end')
            website_input.focus()


def find_password():
    try:
        with open('./data.json','r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File found")

    else:
        website = website_input.get()
        if website in data:
            password = data[website]['password']
            email =  data[website]['email']

            print("Found")
            print(password)
            print((email))
            messagebox.showinfo(title=website, message=f"{password}\n{email}")
        else:
            messagebox.showinfo(title = "Info", message="No details for this website exist")





        pass



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")

window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100,100,image = logo_img)
canvas.grid(column = 1,row = 0)

website_label = Label(text = "Website:",  font= ("Courier", 8,"normal"))
website_label.grid(column = 0,row = 1)

email_label = Label(text = "Email/Username:",  font= ("Courier", 8,"normal"))
email_label.grid(column = 0,row = 2)

password_label = Label(text = "Password:",  font= ("Courier", 8,"normal"))
password_label.grid(column = 0,row = 3)

website_input = Entry()
website_input.grid(column = 1, row  = 1, columnspan= 2, sticky="EW")
website_input.focus()

email_input = Entry()
email_input.grid(column = 1, row  = 2, columnspan= 2, sticky="EW")
email_input.insert(0,"r_mcbarnett@hotmail.com")

password_input = Entry()
password_input.grid(column = 1, row  =3, sticky="EW")

password_btn = Button(text="Generate password", command = password_generate, bg="white")
password_btn.grid(column = 2, row = 3, sticky="EW")

add_btn =  Button(text="Add", command =save_password, width = 36,  bg="white" )
add_btn.grid (column = 1, row = 4, columnspan = 2,sticky="EW")

search_btn = Button(text="Search", command =find_password,  bg="white" )
search_btn.grid (column = 2, row = 1 ,sticky="EW")






window.mainloop()
