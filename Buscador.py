class Buscador:
    def por_codigo(self, lista, codigo):
        if codigo in lista:
            return lista[codigo]
        return None
