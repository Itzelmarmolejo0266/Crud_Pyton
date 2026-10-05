import json

# TUPLA de campos: orden y nombres fijos
CAMPOS_CLIENTE = ("nombre", "apellido", "email", "telefono", "ciudad", "direccion")


class Cliente:
    """MODELO: representa a un cliente."""

    def __init__(self, id_cliente, nombre, apellido, email, telefono, ciudad, direccion):
        self.id = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.ciudad = ciudad
        self.direccion = direccion

    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def a_diccionario(self):
        return {
            "id": self.id, "nombre": self.nombre, "apellido": self.apellido,
            "email": self.email, "telefono": self.telefono,
            "ciudad": self.ciudad, "direccion": self.direccion,
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos["id"], datos["nombre"], datos["apellido"], datos["email"],
            datos["telefono"], datos.get("ciudad", ""), datos.get("direccion", ""),
        )

    def a_json(self):
        return json.dumps(self.a_diccionario(), ensure_ascii=False)

    def __str__(self):
        return f"[{self.id}] {self.obtener_nombre_completo()} - {self.email}"
