import tkinter

#window
window = tkinter.Tk()
window.title("Secret_note")
window.minsize(width=500,height=700)
#window



#file
Secret_notes = open("C:/Users/windb/OneDrive/Masaüstü/Python_secret_notes/notes", "w")

Secret_notes.close()
#file



#title
title_label = tkinter.Label(
    text="Enter your title",
    fg="black",
)
title_label.pack()

title_entry = tkinter.Entry(
    width=50,
)
title_entry.pack()
#title


#secret
secret_label = tkinter.Label(
    text="Enter your secret",
    fg="black",
)
secret_label.pack()

text =tkinter.Text(width=30,height=5)
text.pack()
#secret

#key
key_label = tkinter.Label(
    text="enter master key",
    fg="black",
)
key_label.pack()

key_entry = tkinter.Entry(
    width=50,
)
key_entry.pack()
#key


#save and encrypt
def encrypt_button_fun():
    pass

encrypt_button = tkinter.Button(
    text="save and encrypt",
    command=encrypt_button_fun(),
)
encrypt_button.pack(pady=20)
#save and encrypt


#decrypt
def decrypt_button_fun():
    pass

decrypt_button = tkinter.Button(
    text="Decrypt",
    command=decrypt_button_fun(),
)
decrypt_button.pack()
#decrypt


window.mainloop()