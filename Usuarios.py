class Usuarios:
    lista_usuarios = []

    def __init__(self, nombre, nickname, clave):
        self.nombre = nombre
        self.nickname = nickname
        self.clave = clave

    def guardarUsuario(self):
        Usuarios.lista_usuarios.append(self)
