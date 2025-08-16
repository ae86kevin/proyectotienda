import  claseProducto

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregarProducto(self):
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad de productos: "))
                if cantidad < 0:
                    print("No esta agregando ningun articulo. Intente de nuevo")
                    continue
                break
            except ValueError:
                print("Solo se permite numeros enteres. intente de nuevo")

            for i in range(cantidad):
                print(f"\n ingrese la informacion del producto {i+1}")

                while True:
                    try:
                        codigo=input("Ingrese el codigo del producto: ")
                        if codigo in self.productos:
                            print("El codigo ya existe")
                            return
                        break
                    except ValueError:
                        print("Solo se permite numeros enteres. intente de nuevo")

                while True:
                    nombre=input("Ingrese el nombre del producto: ")
                    if nombre in self.productos:
                        print("El nombre ya existe")
                        return
                    break





