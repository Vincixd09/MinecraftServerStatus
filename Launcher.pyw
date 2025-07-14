import customtkinter as ctk
from PIL import Image
from MinecraftStatusServers import info

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("600x500")
app.title("Minecraft Server Status")

img = Image.open("background.jpg")
img_background = ctk.CTkImage(light_image=img, dark_image=img, size=(1366, 768))

label_background = ctk.CTkLabel(app, image=img_background, text="")
label_background .place(x=0, y=0, relwidth=1, relheight=1)

entrada = ctk.CTkEntry(app, placeholder_text="Server IP")
entrada.pack(pady=10)

resultado = ctk.CTkTextbox(app, width=550, height=350)
resultado.pack(pady=10)

def search():
    serverip = entrada.get()
    resultado.delete("0.0", "end")
    text = info(serverip)
    resultado.insert("0.0", text)

button = ctk.CTkButton(app, text="Server Query", command=search)
button.pack(pady=5)


app.mainloop()
