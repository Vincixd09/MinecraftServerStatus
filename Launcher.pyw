import customtkinter as ctk
from PIL import Image
from MinecraftStatusServers import info

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("600x500")
app.title("Minecraft Server Status")

imagen = Image.open("background.jpg")
imagen_fondo = ctk.CTkImage(light_image=imagen, dark_image=imagen, size=(1366, 768)) #Resulucion del pc 1366x768 

label_fondo = ctk.CTkLabel(app, image=imagen_fondo, text="")
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

entrada = ctk.CTkEntry(app, placeholder_text="Server IP")
entrada.pack(pady=10)

resultado = ctk.CTkTextbox(app, width=550, height=350)
resultado.pack(pady=10)

def buscar():
    serverip = entrada.get()
    resultado.delete("0.0", "end")
    texto = info(serverip)
    resultado.insert("0.0", texto)

button = ctk.CTkButton(app, text="Server Query", command=buscar)
button.pack(pady=5)


app.mainloop()