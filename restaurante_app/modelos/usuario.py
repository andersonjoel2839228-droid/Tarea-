class Usuario:
    def __init__(self, id, nombre, usuario, password):
        self.id = id
        self.nombre = nombre
        self.usuario = usuario
        self.password = password

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "password": self.password
        }