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
    print("3. Ordenar productos")
    print("4. Buscar producto")
    print("5. Modificar producto")
    print("6. Eliminar producto")
    print("0. Salir")

    return input("Seleccione una opcion: ")

def menu_buscar():
    while True:
        print("\n## BUSCADOR DE PRODUCTOS ##")
        print("1. Buscar por codigo")
        print("2. Buscar por nombre")
        print("3. Buscar por categoria")
        print("0. Volver al menu principal")
        op = input("Seleccione una opcion: ")

        if op == "1":
            producto_buscado = buscador.por_codigo(inventario.diccProductos, input("Ingrese el codigo del producto a buscar: "))
        elif op == "2":
            productos_buscados = buscador.por_nombre(inventario.diccProductos, input("Ingrese el nombre a buscar: "))
        elif op == "3":
            productos_buscados = buscador.por_categoria(inventario.diccProductos)
        elif op == "0":
            print("Volviendo al menu principal...")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

def menu_ordenar():
    while True:
        print("\n## ORDENAR PRODUCTOS ##")
        print("1. Ordenar por nombre")
        print("2. Ordenar por precio")
        print("3. Ordenar por stock")
        print("0. Volver al menu principal")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            productos_ordenados = ordenador.por_nombre(list(inventario.diccProductos.values()))
            for producto in productos_ordenados:
                print(producto.mostrarProducto())
        elif opcion == "2":
            productos_ordenados =ordenador.por_precio(list(inventario.diccProductos.values()))
            for producto in productos_ordenados:
                print(producto.mostrarProducto())
        elif opcion == "3":
            productos_ordenados = ordenador.por_stock(list(inventario.diccProductos.values()))
            for producto in productos_ordenados:
                print(producto.mostrarProducto())
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
            inventario.mostrarInventario()
        case "3":
            menu_ordenar()
        case "4":
            menu_buscar()
        case "5":
            inventario.modificarProducto()
        case "6":
            inventario.eliminarProducto()
        case "0":
            print("Saliendo del programa...")
            break
        case _:
            print("Opcion no valida. Intente de nuevo.")