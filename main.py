import Inventario
import Buscador
import Ordenador

inventario = Inventario.Inventario()
buscador = Buscador.Buscador()
ordenador = Ordenador.Ordenador()

def menu_principal():
    print("\n## MENU PRINCIPAL ##")
    print("1. Agregar productos")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Modificar producto")
    print("5. Eliminar producto")
    print("0. Salir")

    return input("Seleccione una opcion: ")

def menu_buscador():
    print("\n## BUSCADOR DE PRODUCTOS ##")
    while True:
        print("1. Buscar por codigo")
        print("2. Buscar por nombre")
        print("3. Buscar por categoria")
        print("0. Volver al menu principal")
        op = input("Seleccione una opcion: ")

        if op == "1":
            producto_buscado = buscador.por_codigo(inventario.diccProductos, input("Ingrese el codigo del producto a buscar: "))
            menu_acciones()
        elif op == "2":
            productos_buscados = buscador.por_nombre(inventario.diccProductos, input("Ingrese el nombre a buscar: "))
            menu_acciones()
        elif op == "3":
            buscador.por_categoria(inventario.diccProductos)
            menu_acciones()
        elif op == "0":
            print("Volviendo al menu principal...")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

def menu_acciones():
    print("\n## ACCIONES ##")
    while True:
        print("1. Modificar producto")
        print("2. Eliminar producto")
        print("3. Agregar producto")
        print("0. Volver al menu anterior")
        accion = input("Seleccione una accion: ")
        if accion == "1":
            inventario.modificarProducto()
        elif accion == "2":
            inventario.eliminarProducto()
        elif accion == "3":
            inventario.agregarProducto()
        elif accion == "4":
            print("Volviendo al buscador...")
            return

def menu_ordenar():
    print("\n## ORDENAR PRODUCTOS ##")
    while True:
        print("1. Ordenar por nombre")
        print("2. Ordenar por precio")
        print("3. Ordenar por stock")
        print("0. Volver al menu principal")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            ordenador.por_nombre(inventario.diccProductos)
            menu_acciones()
        elif opcion == "2":
            ordenador.por_precio(inventario.diccProductos)
            menu_acciones()
        elif opcion == "3":
            ordenador.por_stock(inventario.diccProductos)
            menu_acciones()
        elif opcion == "0":
            print("Volviendo al menu principal...")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

print("_** BIENVENIDO AL SISTEMA DE INVENTARIO **_")

while True:
    opcion = menu_principal()
    match opcion:
        case "1":
            inventario.agregarProducto()
        case "2":
            inventario.mostrarProductos()
            menu_ordenar()
        case "3":
            menu_buscador()
        case "4":
            inventario.modificarProducto()
        case "5":
            inventario.eliminarProducto()
        case "0":
            print("Saliendo del programa...")
            break
        case _:
            print("Opcion no valida. Intente de nuevo.")