class Ordenador:
    def por_nombre(self, lista):
        if len(lista) <= 1:
            return lista

        pivote = lista[0].nombre
        menores = [x for x in lista[1:] if x.nombre < pivote]
        iguales = [x for x in lista if x.nombre == pivote]
        mayores = [x for x in lista[1:] if x.nombre > pivote]

        return self.por_nombre(menores) + iguales + self.por_nombre(mayores)

    def por_precio(self, lista):
        if len(lista) <= 1:
            return lista

        pivote = lista[0].precio
        menores = [x for x in lista[1:] if x.precio < pivote]
        iguales = [x for x in lista if x.precio == pivote]
        mayores = [x for x in lista[1:] if x.precio > pivote]

        return self.por_precio(menores) + iguales + self.por_precio(mayores)

    def por_stock(self, lista):
        if len(lista) <= 1:
            return lista

        pivote = lista[0].stock
        menores = [x for x in lista[1:] if x.stock < pivote]
        iguales = [x for x in lista if x.stock == pivote]
        mayores = [x for x in lista[1:] if x.stock > pivote]

        return self.por_nombre(menores) + iguales + self.por_nombre(mayores)

ordenador = Ordenador()

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrarProducto(self):
        return f"{self.nombre} {self.precio} {self.stock}"


lista = {
    "001": Producto("Manzana", 1.5, 80),
    "002": Producto("Banana", 1.0, 150),
    "003": Producto("Naranja", 2.0, 100),
    "004": Producto("Pera", 1.2, 200),
    "005": Producto("Uva", 3.0, 60)
}

lista_productos = list(lista.values())
print("Lista original:")
for producto in lista_productos:
    print(producto.mostrarProducto())

print("\nOrdenando por nombre:")
lista_ordenada_nombre = ordenador.por_nombre(lista_productos)
for producto in lista_ordenada_nombre:
    print(producto.mostrarProducto())

print("\nOrdenando por precio:")
lista_ordenada_precio = ordenador.por_precio(lista_productos)
for producto in lista_ordenada_precio:
    print(producto.mostrarProducto())

print("\nOrdenando por stock:")
lista_ordenada_stock = ordenador.por_stock(lista_productos)
for producto in lista_ordenada_stock:
    print(producto.mostrarProducto())