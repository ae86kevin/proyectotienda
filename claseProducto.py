class Producto:
    def __init__(self,codigo,nombre,categoria,precio,stock):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def mostrarProducto(self):
        return f"Codigo: {self.codigo} Nombre: {self.nombre} Categoria: {self.categoria} Precio: {self.precio} Stock: {self.stock}"

