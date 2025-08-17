# 🛒 Proyecto SmartStock

Este proyecto simula el funcionamiento básico de un sistema de inventario para una tienda, utilizando clases orientadas a objetos y algoritmos clásicos como Quick Sort y búsqueda secuencial.

---

## 👥 Integrantes

- **Yefry** – Encargado de las clases `Buscador` y `Ordenador`
- **Compañero** – Encargado de las clases `Producto` e `Inventario`

---

## 📦 Estructura del Proyecto

```plaintext
main.py               # Archivo principal que ejecuta el programa
├── Producto          # Clase que representa un producto con atributos como nombre, precio, stock, etc.
├── Inventario        # Clase que gestiona el diccionario de productos (clave = código, valor = Producto)
├── Buscador          # Clase que permite buscar productos por código, nombre o categoría
├── Ordenador         # Clase que ordena productos por nombre, precio o stock usando Quick Sort
```

## 🧑‍💻 Tareas por integrante
### 🔹 Yefry – Lógica de búsqueda y ordenamiento
#### Clase Buscador
- Buscar productos por:

* Código (acceso directo desde el diccionario)

* Nombre (coincidencia parcial, sin importar mayúsculas)

* Categoría (coincidencia parcial)

* Retorna listas de objetos Producto para facilitar el ordenamiento

#### Clase Ordenador
- Ordena listas de productos por:

* Nombre

* Precio

* Stock

* Utiliza el algoritmo Quick Sort

* Recibe listas derivadas del diccionario del inventario

### 🔹 Kevin – Gestión de productos e inventario
#### Clase Producto
- Atributos:

* Código

* Nombre

* Precio

* Stock

* Categoría

* Métodos para mostrar información y validar datos

#### Clase Inventario
**Almacena productos en un diccionario {codigo: Producto}**

- Métodos para:

* Agregar productos

* Eliminar productos

* Actualizar stock

* Obtener lista de productos para búsqueda y ordenamiento

## ⚙️ Funcionalidades principales
* Agregar productos al inventario

* Buscar productos por diferentes criterios

* Ordenar productos según atributos

* Mostrar resultados en consola

## 📌 Notas técnicas
* El algoritmo Quick Sort se aplica sobre listas, por lo que el diccionario del inventario se convierte en lista antes de ordenar.

* Las búsquedas por nombre y categoría se realizan sobre los valores del diccionario (.values()).

* Se recomienda retornar listas en lugar de imprimir directamente para mantener modularidad y reutilización.

## 🚀 Estado del proyecto
- * ✅ Estructura base completada

- * 🛠️ Clases en desarrollo

- * 🔄 Integración en main.py pendiente