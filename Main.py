import tkinter as tk
from Usuarios import Usuarios

def guardar_usuario():
    nombre = entry_nombre.get()
    nickname = entry_nickname.get()
    clave = entry_clave.get()
    nuevo_usuario = Usuarios(nombre, nickname, clave)
    nuevo_usuario.guardarUsuario()

    actualizar_lista()

def actualizar_lista():
    listbox_usuarios.delete(0, tk.END)
    for usuario in Usuarios.lista_usuarios:
        listbox_usuarios.insert(tk.END, f"Nombre: {usuario.nombre}, Nickname: {usuario.nickname}")

root = tk.Tk()
root.title("Formulario de Usuarios")

label_nombre = tk.Label(root, text="Nombre:")
label_nombre.grid(row=0, column=0)

entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1)

label_nickname = tk.Label(root, text="Nickname:")
label_nickname.grid(row=1, column=0)

entry_nickname = tk.Entry(root)
entry_nickname.grid(row=1, column=1)

label_clave = tk.Label(root, text="Clave:")
label_clave.grid(row=2, column=0)

entry_clave = tk.Entry(root, show="*")
entry_clave.grid(row=2, column=1)

boton_guardar = tk.Button(root, text="Guardar", command=guardar_usuario)
boton_guardar.grid(row=3, column=0, columnspan=2)

listbox_usuarios = tk.Listbox(root, width=50, height=10)
listbox_usuarios.grid(row=4, column=0, columnspan=2)

root.mainloop()
