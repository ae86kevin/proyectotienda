class Buscador:
    # Metodo busca si el codigo(clave) está en la lista(diccionario) y retorna el valor(Objeto)
    def por_codigo(self, lista, codigo):
        if codigo in lista:
            return lista[codigo]
        return None

    # Metodo busca si un producto(objeto) en la lista(diccionario) tiene el nombre a buscar y retorna un nuevo diccionario de los objetos que coinciden
    def por_nombre(self, lista, nombre):
        return [producto for producto in lista.values() if producto.nombre.lower() == nombre.lower()] # Lista por comprensión

    # Metodo busca si un producto(objeto) en la lista(diccionario) tiene la categoría a buscar y retorna un nuevo diccionario de los objetos que coinciden
    def por_categoria(self, lista, categoria):
        return [producto for producto in lista.values() if producto.categoria.lower() == categoria.lower()] # Lista por comprensión
