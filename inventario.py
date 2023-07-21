#Implementación de un sistema de gestión de inventario:
#Crea un sistema de gestión de inventario para una tienda, donde se puedan agregar productos,
#controlar el stock, realizar ventas y generar informes de ventas. Utiliza clases como "Producto", 
#"Inventario" y "Venta" para representar el sistema y utiliza métodos para gestionar las operaciones.
class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def get_codigo(self):
        return self.codigo

    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio

    def get_stock(self):
        return self.stock

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def agregar_stock(self, cantidad):
        self.stock += cantidad

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            venta_total = cantidad * self.precio
            print(f"Venta realizada: {cantidad} unidades de {self.nombre}. Total: {venta_total}")
        else:
            print("No hay suficiente stock disponible.")

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_producto(self, codigo):
        for producto in self.productos:
            if producto.get_codigo() == codigo:
                return producto
        return None

    def generar_informe_stock(self):
        print("Informe de Stock:")
        for producto in self.productos:
            print(producto)

    def listar_productos(self):
        print("Listado de Productos:")
        for producto in self.productos:
            print(f"Código: {producto.get_codigo()}, Nombre: {producto.get_nombre()}")


class Venta:
    def __init__(self, cliente_miembro=False):
        self.productos_vendidos = []
        self.cliente_miembro = cliente_miembro

    def agregar_producto_vendido(self, producto, cantidad):
        self.productos_vendidos.append({"producto": producto, "cantidad": cantidad})
#--IMPORTANTE-- Agregado el metodo que aplique un descuento del 20% a miembros.
    def calcular_total_venta(self):
        total = 0
        for item in self.productos_vendidos:
            subtotal = item["producto"].get_precio() * item["cantidad"]
            total += subtotal

        if self.cliente_miembro:
            total *= 0.8  # Aplicar descuento del 20% para clientes miembros

        return total

    def generar_factura(self):
        print("Factura de Venta:")
        for item in self.productos_vendidos:
            subtotal = item['cantidad'] * item['producto'].get_precio()
            print(f"{item['producto'].get_nombre()} - Cantidad: {item['cantidad']} - Subtotal: {subtotal}")

        total_venta = self.calcular_total_venta()
        print(f"Total: {total_venta}")

#----Crear algunos productos y agregarlos al inventario
producto1 = Producto(1, "Camiseta", 25.0, 50)
producto2 = Producto(2, "Pantalón", 40.0, 30)
producto3 = Producto(3, "Zapatos", 60.0, 20)

inventario = Inventario()
inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)
inventario.agregar_producto(producto3)

#Realizar una venta para un cliente miembro
venta_cliente_miembro = Venta(cliente_miembro=True)
producto_vendido1 = inventario.buscar_producto(1)
producto_vendido2 = inventario.buscar_producto(3)

if producto_vendido1 and producto_vendido2:
    venta_cliente_miembro.agregar_producto_vendido(producto_vendido1, 3)
    venta_cliente_miembro.agregar_producto_vendido(producto_vendido2, 2)

venta_cliente_miembro.generar_factura()

#Realizar otra venta para un cliente no miembro
venta_cliente_no_miembro = Venta()
producto_vendido3 = inventario.buscar_producto(2)

if producto_vendido3:
    venta_cliente_no_miembro.agregar_producto_vendido(producto_vendido3, 1)

venta_cliente_no_miembro.generar_factura()