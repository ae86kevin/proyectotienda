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

