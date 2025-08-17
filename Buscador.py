class Buscador:
    # Metodo busca si el codigo(clave) está en la lista(diccionario) y retorna el valor(Objeto)
    def por_codigo(self, lista, codigo):
        if codigo in lista:
            return lista[codigo]
        return None

    # Metodo busca si el nombre está en la lista(diccionario) y retorna un nuevo diccionario de los objetos que coinciden
    def por_nombre(self, lista, nombre):
        nueva_lista = {}
        nombre = nombre.lower()
        for clave, producto in lista.items():
            if producto.nombre.lower() == nombre:
                nueva_lista[clave] = producto
        return nueva_lista
