class Buscador:
    # Metodo busca si el codigo(clave) está en la lista(diccionario) y retorna el valor(Objeto)
    def por_codigo(self, lista, codigo):
        if codigo in lista:
            print("...Producto encontrado:")
            print(lista[codigo].mostrarProducto())
            return lista[codigo]
        print("...No se encontró un producto con ese código.\n")
        return None

    # Metodo busca si un producto(objeto) en la lista(diccionario) tiene el nombre a buscar y retorna un nuevo diccionario de los objetos que coinciden
    def por_nombre(self, lista, nombre):
        nueva_lista = [producto for producto in lista.values() if producto.nombre.lower() == nombre.lower()] # Lista por comprensión
        # Imprimir los productos encontrados
        if nueva_lista:
            print(f"## Productos encontrados con el nombre '{nombre}':")
            for producto in nueva_lista:
                print(producto.mostrarProducto())
            return nueva_lista
        print("...No se encontraron productos con ese nombre.\n")
        return None

    # Metodo busca si un producto(objeto) en la lista(diccionario) tiene la categoría a buscar y retorna un nuevo diccionario de los objetos que coinciden
    def por_categoria(self, lista):
        while True:
            print("(1)Alimentos frescos, (2)lacteos , (3)bebidas, (4)limpieza")
            num_categor = input("seleccine la tipo de categoria ")
            if num_categor in ["1", "2", "3", "4"]:
                categorias = {
                    "1": "Alimentos frescos",
                    "2": "Lacteos",
                    "3": "Bebidas",
                    "4": "Limpieza"
                }
                categoria = categorias[num_categor]
                break
            else:
                print("Debe seleccionar una categoria")

        nueva_lista = [producto for producto in lista.values() if producto.categoria.lower() == categoria.lower()]  # Lista por comprensión
        # Imprimir los productos encontrados
        if nueva_lista:
            print(f"## Productos encontrados en la categoria '{categoria}':")
            for producto in nueva_lista:
                print(producto.mostrarProducto())
            return nueva_lista
        print("...No se encontraron productos de esa categoria.\n")
        return None

