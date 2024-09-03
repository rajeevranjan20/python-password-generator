from tkinter import*
import random,string
import pyperclip

root=Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title("Password Generator")

Label(root,text='Password Generator',font='arial 15 bold').pack()
Label(root,text='Python',font='arial 15 bold').pack(side=BOTTOM)

pass_label=Label(root,text='Password Length',font='arial 10 bold').pack()
pass_len=IntVar()
length=Spinbox(root,from_=8,to_=32,textvariable=pass_len,width=15).pack()
pass_str=StringVar()

def Generator():
    password=[]

    if pass_len.get()>=4:
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.digits))
        password.append(random.choice(string.punctuation))

        for _ in range(pass_len.get()-4):
            password.append(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation))
        random.shuffle(password)
    else:
        for _ in range(pass_len.get()):
            password.append(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation))
    pass_str.set(''.join(password))


def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root,text='Generate Password',command=Generator).pack(pady=5)
Entry(root,textvariable=pass_str).pack()
Button(root,text='Copy To Clipboard',command=Copy_password).pack(pady=5)

root.mainloop()