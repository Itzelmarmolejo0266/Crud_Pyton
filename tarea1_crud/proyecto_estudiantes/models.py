# TUPLA de campos editables/pedidos al crear (orden fijo)
CAMPOS_ESTUDIANTE = ("nombre", "apellido", "email", "carnet")


class Estudiante:
    """MODELO: usa las cuatro colecciones (dict, list, set, tuple)."""

    def __init__(self, id_estudiante, nombre, apellido, email, carnet, notas=None, materias=None):
        self.id = id_estudiante
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.carnet = carnet
        # DICCIONARIO DE LISTAS: {"Matemática": [18, 19]}
        self.notas = notas if notas else {}
        # CONJUNTO: materias inscritas, sin repetidos
        self.materias = set(materias) if materias else set()

    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def inscribir_materia(self, materia):
        self.materias.add(materia)

    def agregar_nota(self, materia, nota):
        self.inscribir_materia(materia)
        self.notas.setdefault(materia, []).append(nota)

    def obtener_promedio(self):
        todas = []
        for lista_notas in self.notas.values():
            todas.extend(lista_notas)
        if not todas:
            return 0
        return round(sum(todas) / len(todas), 2)

    def materias_en_comun(self, otro):
        # INTERSECCIÓN de conjuntos
        return self.materias & otro.materias

    def a_diccionario(self):
        return {
            "id": self.id, "nombre": self.nombre, "apellido": self.apellido,
            "email": self.email, "carnet": self.carnet,
            "notas": self.notas,
            "materias": sorted(self.materias),   # JSON no guarda sets
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos["id"], datos["nombre"], datos["apellido"], datos["email"], datos["carnet"],
            notas=datos.get("notas", {}),
            materias=set(datos.get("materias", [])),   # lista -> set
        )

    def __str__(self):
        return f"[{self.carnet}] {self.obtener_nombre_completo()} - Promedio: {self.obtener_promedio()}"
