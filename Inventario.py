from logging import exception
from math import trunc
from queue import PriorityQueue
from symtable import Class
from traceback import print_tb
from xml.dom.minidom import ProcessingInstruction

import  claseProducto

class Inventario:
    def __init__(self):
        self.diccProductos = {}


    def agregarProducto(self):
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad de productos: "))
                if cantidad <= 0:
                    print("No esta agregando ningun articulo. Intente de nuevo")
                    continue
                break
            except ValueError:
                print("Solo se permite numeros enteres. intente de nuevo")

            for i in range(cantidad):
                print(f"\n ingrese la informacion del producto {i+1}")

                while True:
                    try:
                        codigo=int(input("Ingrese el codigo del producto: "))
                        if codigo in self.diccProductos:
                            print("El codigo ya existe. intente de nuevo")
                            return
                        break
                    except ValueError:
                        print("Solo se permite numeros enteres. intente de nuevo")

                while True:
                    nombre=input("Ingrese el nombre del producto: ")
                    if nombre =="":
                        print("Deber ingresar un nombre.Intente de nuevo")
                    else:
                        break


                while True:
                    print("(1)Alimentos fresco, (2)lacteos , (3)bebidas, (4)liempieza")
                    categaria=input("seleccine la tipo de categoria ")
                    if categaria in ["1", "2", "3", "4"]:
                        categarias={
                            "1":"Alimentos fresco",
                            "2":"Lacteos ",
                            "3":"Bebidas ",
                            "4":"Liempieza"

                        }
                        categaria=categarias[categaria]
                        break
                    else:
                        print("Debe seleccionar una categoria")

                while True:
                    try:
                        precio=float(input("Ingrese el precio del producto: "))
                        break
                    except ValueError:
                        print("Solo se permite numero. Intente de nuevo")

                while True:
                    try:
                        stock=int(input("Ingrese el stock del producto: "))
                        if stock<0:
                            print("el stcok no puede ser menor a 0. intente de nuevo")
                            continue
                        break
                    except ValueError:
                        print("Solo se permite numero. Intente de nuevo")


                self.diccProductos[codigo]=claseProducto.Producto(codigo, nombre, categaria, precio,stock)
                print("\nProducto agregado con exito")


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

        else:
            print("\nProducto no registrado")



    def modificarProducto(self):
        codigo=input("Ingrese el codigo del producto. ")
        if codigo in self.diccProductos:
            producto=self.diccProductos[codigo]
            producto(f"\n{producto.nombre}")


            while True:
                print("\nQue datos desea Modificar? ")
                print("1. Nombre")
                print("2. Precio")
                print("3. Stock")
                print("0. salir")
                seleccion =input("seleccione una opcion: ")


                match seleccion:
                    case "1":
                        nuevoNombre = input("Ingrese el nuevo nombre: ")
                        producto.nombre=nuevoNombre
                        print("\nProducto modificado con exito")

                    case "2":
                        while True:
                            try:
                                nuevoPrecio = float(input("Ingrese el precio del producto: "))
                                producto.precio = nuevoPrecio
                                print("\nProducto modificado con exito")
                                break
                            except ValueError:
                                print("Solo se permite numeros. intente de nuevo")
                    case "3":
                        try:
                            nuevoStock = float(input("Ingrese el stock del producto: "))
                            producto.stockd = nuevoStock
                            print("\nProducto modificado con exito")
                        except ValueError:
                            print("Cantidad invalida")


                    case "0":
                        print("saliendo del del menu")
                        break
        else:
            print("\nProducto no encotrado")


    def modificadoStock(self):
        codigo = int(input("ingrese el codigo del producto: "))
        if codigo in self.diccProductos:
            producto=self.diccProductos[codigo]
            print(f"stock actual de '{producto.nombre}' : {producto.stockd}")
            try:
                nuevoStock = float(input("Ingrese el stock del producto: "))
                if nuevoStock < 0:
                    print("la cantidad no debe ser menor a 0. intente de nuevo")
                else:
                    producto.stockd = nuevoStock
                    print("\nProducto modificado con exito")
            except ValueError:
                print("Debe ser numero entero.intente de nuevo")
        else:
            print("Producto no registrado")




    def Mostarinvetario(self):
        if not self.diccProductos:
            print("\nEl invetario esta vacio")
            return
        print("\n INVERTARIOS DE LA TIENDA")
        for codigo,producto in self.diccProductos.items():
            print(f"\nCodigo: {producto.codigo}")
            print(f"Nombre: {producto.nombre}")
            print(f"Categoris: {producto.categoria}")
            print(f"Precio: {producto.precio:.2f}")
            print(f"stoc: {producto.stock}")















