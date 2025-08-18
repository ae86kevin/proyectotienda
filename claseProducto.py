class Producto:
    def __init__(self,codigo,nombre,categoria,precio):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio


    def mostrarProducto(self):
        return self.codigo,self.nombre,self.categoria,self.precio

