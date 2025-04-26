import random

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

def buscar_producto(productos, nombre):
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None

def realizar_compra(productos):
    total_compra = 0

    while True:
        nombre_producto = input("\nIngrese el nombre del producto a comprar (o 'fin' para finalizar): ")
        if nombre_producto.lower() == "fin":
            break

        producto = buscar_producto(productos, nombre_producto)
        if producto is None:
            print("El producto no existe. Intente nuevamente.")
            continue

        cantidad = int(input(f"Ingrese la cantidad de '{producto['nombre']}' a comprar: "))
        if cantidad > producto["stock"]:
            print("No hay suficiente stock disponible. Intente con una cantidad menor.")
            continue

        subtotal = producto["precio"] * cantidad
        total_compra += subtotal
        producto["stock"] -= cantidad
        print(f"Subtotal por {cantidad} unidad(es) de '{producto['nombre']}': ${subtotal:.2f}")

    if total_compra > 0:
        descuento = random.randint(1, 10)
        total_con_descuento = total_compra * (1 - descuento / 100)
        print(f"\nTotal de la compra: ${total_compra:.2f}")
        print(f"Descuento sorpresa: {descuento}%")
        print(f"Total con descuento: ${total_con_descuento:.2f}")
    else:
        print("\nNo se realizó ninguna compra.")

if __name__ == "__main__":
    print("Registro de productos:")
    productos = registrar_productos()
    print("\nProductos registrados exitosamente.")
    realizar_compra(productos)