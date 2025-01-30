from tkinter import *
from tkinter import messagebox
import json
import random
import pyperclip

def search():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showwarning(title="Warning",message="Must create data first")
    else:
        found = False
        for key in data:
            if key.lower()== input1.get().lower():
                print("found")
                found = True
                email= data[key]["email"]
                password = data[key]["Password"]
                messagebox.showinfo(title=input1.get(), message=f"email:{email}\nPassword: {password}")
        if not found:
            messagebox.showerror(title="Error",message="Does not exist")



def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = password_numbers+password_symbols+password_numbers
    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    input3.insert(0,password)
    pyperclip.copy(input3)


def save_password():
    new_data = {
         input1.get():{
             "email": input2.get(),
             "Password": input3.get()
         }
    }

    if input1.get() != "" and input2.get() !="" and input3.get() !="":

        try:
            with open("data.json","r") as file:
                # json.dump(new_data,file,indent=4)
                data= json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json","w") as file:
                json.dump(new_data,file,indent =4)

        else:
            with open("data.json","w") as file:
                json.dump(data,file,indent=4)
        finally:
            input1.delete(0,END)
            input3.delete(0,END)

    else:
        messagebox.showwarning(title="Warning",message="Please fill out all info")


window = Tk()
window.title("Password manager")
window.config(padx=20,pady=20)

img = PhotoImage(file= "logo.png")
image_canvas = Canvas(width=200,height=200,highlightthickness=0)
image_canvas.create_image(100,100,image=img)
image_canvas.grid(row=0,column=1)


text1=Label(text="website: ")
text1.grid(column=0,row=1)

text2=Label(text="Email/Username: ")
text2.grid(column=0,row=2)


text1=Label(text="Password: ")
text1.grid(column=0,row=3)

input1 = Entry(width=17)
input1.grid(column=1,row=1,columnspan=1)
input1.focus()

input2 = Entry(width=35)
input2.grid(column=1,row=2,columnspan=2)
input2.insert(0,"Arian.khan@gmail.com")

input3 = Entry(width=17)
input3.grid(column=1,row=3,columnspan=1)

generate_button = Button(text = "Generate Password",highlightthickness=0,command=password_generator)
generate_button.grid(column=2,row=3,columnspan=1)

add_button = Button(text = "Add",width=30,highlightthickness=0,command = save_password)
add_button.grid(row=4,column=1,columnspan=2)

search_button =Button(text="Search",bg="blue",fg= "white",command=search,highlightthickness=0)
search_button.grid(row=1,column=2,columnspan=1)










window.mainloop()