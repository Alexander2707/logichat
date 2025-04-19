from customtkinter import *
from PIL import Image

from socket import*
import threading

client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 1488))

# 
load_image = Image.open("image/send_icon.png")
img = CTkImage(light_image=load_image, size=(20, 20))
    
# ---------------- WINDOW ----------------
window = CTk()
window.geometry("390x500")
window.configure(fg_color='royalblue')

# ---------------- FRAME 1 ----------------
f1 = CTkFrame(window, width=350, height=380, fg_color="white",border_width=3, border_color="darkgrey", corner_radius=10)
f1.pack_propagate(False)
text_pole = CTkTextbox(f1, width=345, height=370, border_width=1)
text_pole.pack(pady=5, padx=5)

# ---------------- FRAME 2 ----------------
f2 = CTkFrame(window, width=350, height=60, fg_color='white')
f2.pack_propagate(False)
ent = CTkEntry(f2, width=230, height=40, placeholder_text="enter your message .....", font=("Arial", 14))
ent.place(x=10, y=10)

# ---------------- SEND MESSAGE ----------------
def click():
    msg = ent.get()
    ent.delete(0, END)
    text_pole.configure(state="normal")
    text_pole.insert(END, "Sasha_simba: " + msg + "\n\n")
    text_pole.configure(state="disabled")
    client.send(f"Sasha_simba: {msg}".encode())
   
def on_enter(event):
    click()
    


# ---------------- GET MESSAGE ----------------   
def recieve():
    while 1:
        try:
            message = client.recv(1024).decode().strip()
            print(message)
            text_pole.configure(state="normal")
            text_pole.insert(END, "server:" + message + "\n\n")
            text_pole.configure(state="disabled")
        except:
            pass
        
threading.Thread(target=recieve).start()

b1 = CTkButton(f2, width=70, height=30, fg_color="royalblue", corner_radius=20, text="SEND", image=img, command=click)
b1.pack_propagate(False)
b1.pack(side="right", padx=10)

f1.pack(pady=20)
f2.pack()

ent.bind("<Return>", on_enter)

window.mainloop()