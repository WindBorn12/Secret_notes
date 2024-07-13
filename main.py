import tkinter
from tkinter import messagebox
from tkinter import PhotoImage, END
import base64

#ecnrypt and decrypt
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)
#ecnrypt and decrypt


def save_and_encrypt_notes():
    title = title_entry.get()
    message = secret_text.get("1.0", END)
    master_secret = key_entry.get()

    if len(title) == 0 or len(message) == 0 or len(master_secret) == 0:
        messagebox.showerror(title="Error!",message="Please enter all info")
    else:
        #encryptiom
        message_encrypted = encode(master_secret, message)

        try:
            with open("mysecret.txt", "a") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")

        except FileNotFoundError:
            with open("mysecret.txt", "w") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        finally:
            title_entry.delete(0,END)
            secret_text.delete("1.0",END)
            key_entry.delete(0,END)

def decrypt_notes():
    message_encrypted = secret_text.get("1.0",END)
    master_secret = key_entry.get()

    if len(message_encrypted) == 0 or len(master_secret) == 0:
        messagebox.showerror(title="Error!",message="Please enter all info")
    else:
        try:
            decrypted_message = decode(master_secret,message_encrypted)
            secret_text.delete("1.0",END)
            secret_text.insert("1.0",decrypted_message)
        except:
            messagebox.showerror(title="Error!", message="please enter encrypted text")


#window
window = tkinter.Tk()
window.title("Secret_note")
window.minsize(width=500,height=700)
#window



#ui


## photo
photo = PhotoImage(file = "img.png")
#photo_button = tkinter.Label(image=photo)
#photo_button.pack()

canvas = tkinter.Canvas(height=200,width=200)
canvas.create_image(100,100,image=photo)
canvas.pack()
## photo




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
    width=50,
)
secret_label.pack()

secret_text= tkinter.Text(width=30, height=5)
secret_text.pack()
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




encrypt_button = tkinter.Button(
    text="save and encrypt",
    command=save_and_encrypt_notes,
)
encrypt_button.pack(pady=20)
#save and encrypt



decrypt_button = tkinter.Button(
    text="Decrypt",
    command=decrypt_notes,
)
decrypt_button.pack()
#decrypt


window.mainloop()