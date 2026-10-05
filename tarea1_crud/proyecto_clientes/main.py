"""VISTA de Clientes: solo menú, input() y print()."""
from models import CAMPOS_CLIENTE
from shared.herramientas import (
    imprimir_titulo, imprimir_exito, imprimir_error, imprimir_info, confirmar
)
from views import (
    crear_cliente, obtener_todos, obtener_por_id, buscar_clientes,
    actualizar_cliente, eliminar_cliente, estadisticas, clientes_por_ciudad
)


def pausa():
    input("\nPresione Enter para continuar...")


def pedir_id():
    try:
        return int(input("Id del cliente: "))
    except ValueError:
        imprimir_error("El id debe ser un número entero")
        return None


def mostrar_resultado(exito, mensaje):
    (imprimir_exito if exito else imprimir_error)(mensaje)


def mostrar_tabla(clientes):
    print(f"{'ID':<5}{'NOMBRE':<25}{'EMAIL':<28}{'CIUDAD':<15}{'TELÉFONO':<12}")
    print("-" * 85)
    for c in clientes:
        print(f"{c.id:<5}{c.obtener_nombre_completo():<25}{c.email:<28}{c.ciudad:<15}{c.telefono:<12}")
    print("-" * 85)
    imprimir_info(f"Total: {len(clientes)} cliente(s)")


def opcion_crear():
    imprimir_titulo("CREAR NUEVO CLIENTE")
    datos = {campo: input(f"{campo.capitalize()}: ") for campo in CAMPOS_CLIENTE}
    mostrar_resultado(*crear_cliente(datos))
    pausa()


def opcion_ver_todos():
    imprimir_titulo("LISTA DE CLIENTES")
    clientes = obtener_todos()
    if not clientes:
        imprimir_info("Todavía no hay clientes. Use la opción 1 para crear el primero.")
    else:
        mostrar_tabla(clientes)
    pausa()


def opcion_buscar():
    imprimir_titulo("BUSCAR CLIENTE")
    termino = input("Nombre, email, teléfono o ciudad: ")
    encontrados = buscar_clientes(termino)
    if not encontrados:
        imprimir_info(f"Ningún cliente coincide con '{termino}'.")
    else:
        mostrar_tabla(encontrados)
    pausa()


def opcion_ver_por_id():
    imprimir_titulo("VER CLIENTE POR ID")
    id_cliente = pedir_id()
    if id_cliente is None:
        return pausa()
    cliente = obtener_por_id(id_cliente)
    if not cliente:
        imprimir_error(f"No existe un cliente con id {id_cliente}")
    else:
        for clave, valor in cliente.a_diccionario().items():
            print(f"  {clave.capitalize():<12}: {valor}")
    pausa()


def opcion_actualizar():
    imprimir_titulo("ACTUALIZAR CLIENTE")
    id_cliente = pedir_id()
    if id_cliente is None:
        return pausa()
    cliente = obtener_por_id(id_cliente)
    if not cliente:
        imprimir_error(f"No existe un cliente con id {id_cliente}")
        return pausa()

    imprimir_info(f"Editando a {cliente.obtener_nombre_completo()}")
    print("Deje en blanco el campo que no quiera cambiar.\n")
    cambios = {}
    for campo in CAMPOS_CLIENTE:
        nuevo = input(f"{campo.capitalize()} [{getattr(cliente, campo)}]: ").strip()
        if nuevo:
            cambios[campo] = nuevo
    mostrar_resultado(*actualizar_cliente(id_cliente, cambios))
    pausa()


def opcion_eliminar():
    imprimir_titulo("ELIMINAR CLIENTE")
    id_cliente = pedir_id()
    if id_cliente is None:
        return pausa()
    cliente = obtener_por_id(id_cliente)
    if not cliente:
        imprimir_error(f"No existe un cliente con id {id_cliente}")
        return pausa()
    imprimir_info(f"Se eliminará: {cliente}")
    if confirmar("¿Confirma la eliminación?"):
        mostrar_resultado(*eliminar_cliente(id_cliente))
    else:
        imprimir_info("Operación cancelada")
    pausa()


def opcion_estadisticas():
    imprimir_titulo("ESTADÍSTICAS")
    d = estadisticas()
    print(f"  Clientes registrados : {d['total']}")
    print(f"  Ciudades distintas   : {len(d['ciudades'])} -> {', '.join(d['ciudades'])}")
    print(f"  Dominios de email    : {', '.join(d['dominios'])}")
    print(f"  Sin teléfono         : {len(d['sin_telefono'])}")
    pausa()


def opcion_por_ciudad():
    imprimir_titulo("CLIENTES POR CIUDAD")
    grupos = clientes_por_ciudad()
    if not grupos:
        imprimir_info("No hay clientes.")
    for ciudad, nombres in sorted(grupos.items()):
        print(f"  {ciudad:<15}: {', '.join(nombres)}")
    pausa()


def salir():
    imprimir_info("¡Hasta luego! 👋")
    return "salir"


# DICCIONARIO de opciones: tecla -> (texto, función)
OPCIONES = {
    "1": ("Crear cliente", opcion_crear),
    "2": ("Ver todos", opcion_ver_todos),
    "3": ("Buscar", opcion_buscar),
    "4": ("Ver por id", opcion_ver_por_id),
    "5": ("Actualizar", opcion_actualizar),
    "6": ("Eliminar", opcion_eliminar),
    "7": ("Estadísticas", opcion_estadisticas),
    "8": ("Clientes por ciudad", opcion_por_ciudad),
    "0": ("Salir", salir),
}


def mostrar_menu():
    imprimir_titulo("SISTEMA DE GESTIÓN DE CLIENTES")
    for tecla, (texto, _f) in OPCIONES.items():
        print(f"  {tecla}. {texto}")
    print()


def main():
    while True:
        mostrar_menu()
        tecla = input("Seleccione una opción: ").strip()
        if tecla not in OPCIONES:
            imprimir_error("Opción no válida")
            pausa()
            continue
        if OPCIONES[tecla][1]() == "salir":
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
