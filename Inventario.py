from logging import exception
from math import trunc
from queue import PriorityQueue
from symtable import Class
from xml.dom.minidom import ProcessingInstruction

import  claseProducto

class Inventario:
    def __init__(self):
        self.diccProductos = {}

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
                    if codigo in self.diccProductos:
                        print("El codigo ya existe")
                        return
                    break
                except ValueError:
                    print("Solo se permite numeros enteres. intente de nuevo")

            while True:
                try:
                    nombre=input("Ingrese el nombre del producto: ")
                    if nombre in self.diccProductos:
                        print("El producto ya se encuetra registrado")
                        return
                    break
                except ValueError:
                    print("Solo se permite numeros enteros. intente de nuevo")

            while True:
                try:
                    categoria=input("Seleccione el tipo de categoria: ")
                    print("(1)Alimentos fresco, (2)lacteos , (3)bebidas, (4)liempieza")
                    break
                except ValueError:
                    print("Intente de nuevo")

            while True:
                try:
                    precio=float(input("Ingrese el precio del producto: "))
                    break
                except ValueError:
                    print("Solo se permite numero. Intente de nuevo")

                self.diccProductos[codigo]= claseProducto.Producto(codigo, nombre, categoria, precio)
                print("\nProducto Agregado Con exito")


    def eliminarProducto(self):
        codigo = input("Ingrese el código del producto a eliminar: ")
        if codigo in self.diccProductos:
            producto=self.diccProductos[codigo]
            confirmar=input(f"\nEsta seguro que desea eliminar este producto {producto.codigo}? (s/n): ")
            if confirmar.lower() == "s":
                del self.diccProductos[codigo]
                print("\nProducto eliminado con exito")
            else:
                print("\nNo se elimino nada")
                return
        else:
            print("\nProducto no registrado")

    def modificarProducto(self):
        codigo=input("Ingrese el codigo del producto. ")
        if codigo in self.diccProductos:
            producto=self.diccProductos[codigo]
            producto(f"\n{producto.nombre}")

            seleccion =""
            while seleccion != "0":
                print("\nQue datos desea Modificar? ")
                print("1. Nombre")
                print("2. Categoria")
                print("3. Precio")
                print("4. Stock")
                print("5. salir")
                seleccion =int(input())

            match seleccion:
                case "1":
                    nuevoNombre=input("Ingrese el nuevo nombre: ")
                    producto.nombre(nuevoNombre)
                    print("\nProducto modificado con exito")









