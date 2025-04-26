def registrar_productos():
 
    productos = []
    for i in range(3):
        print(f"Registro del producto {i + 1}:")
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio del producto: "))
        stock = int(input("Stock del producto: "))
        producto = {"nombre": nombre, "precio": precio, "stock": stock}
        productos.append(producto)
    return productos

def mostrar_productos(productos):

    print("\nProductos registrados:")
    for i, producto in enumerate(productos, start=1):
        print(f"Producto {i}:")
        print(f"  Nombre: {producto['nombre']}")
        print(f"  Precio: {producto['precio']}")
        print(f"  Stock: {producto['stock']}")

if __name__ == "__main__":
    productos = registrar_productos()
    mostrar_productos(productos)