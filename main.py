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

def menu_acciones():
    print("\n## ACCIONES ##")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Modificar producto")
    print("4. Eliminar producto")

print("_** BIENVENIDO AL SISTEMA DE INVENTARIO **_")

while True:
    opcion = menu_principal()
    match opcion:
        case "1":
            inventario.agregarProducto()
        case "2":
            pass
        case "3":
            print("\n## BUSCADOR DE PRODUCTOS ##")
            while True:
                print("1. Buscar por codigo")
                print("2. Buscar por nombre")
                print("3. Buscar por categoria")
                print("0. Volver al menu principal")
                op = input("Seleccione una opcion: ")

                if op == "1":
                    producto_buscado = buscador.por_codigo(inventario.diccProductos, input("Ingrese el codigo del producto a buscar: "))
                    break
                elif op == "2":
                    productos_buscados = buscador.por_nombre(inventario.diccProductos, input("Ingrese el nombre a buscar: "))
                    break
                elif op == "3":
                    buscador.por_categoria(inventario.diccProductos, input("Ingrese la categoria a buscar: "))
                    break
                elif op == "0":
                    print("Volviendo al menu principal...")
                    break
                else: print("Opcion no valida. Intente de nuevo.")
        case "0":
            print("Saliendo del programa...")
            break
        case _:
            print("Opcion no valida. Intente de nuevo.")