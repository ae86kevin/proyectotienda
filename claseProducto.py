class claseProducto:
    def __init__(self,codigo,nombre,categoria,precio,stock):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def mostrarProducto(self):
        return self.codigo,self.nombre,self.categoria,self.precio,self.stock

