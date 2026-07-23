#Importar las colecciones y configuraciones.
from datos import productos, movimientos, categorias, CONFIGURACION
#Importar las funciones de validación
from validaciones import (leer_texto,
    leer_entero_no_negativo,
    leer_numero_positivo,
    leer_opcion)

#pesos chilenos
def formatear_pesos(valor):
    return f"${valor:,.0f}".replace(",", ".")

#precio con IVA.
def calcular_precio_con_iva(precio):
    iva = CONFIGURACION[1]
    precio_con_iva = precio + (precio * iva)

    return precio_con_iva

# Función para actualizar las categorías registradas
def actualizar_categorias():
    categorias.clear()

    for producto in productos.values():
        categorias.add(producto["categoria"])

#agregar un producto
def agregar_producto():
    print("\n--- AGREGAR PRODUCTO ---")

    codigo = leer_texto("Ingrese el código del producto: ").upper()

    if codigo in productos:
        print("Ya existe un producto con ese código.")
        return False

    nombre = leer_texto("Ingrese el nombre del producto: ").title()
    categoria = leer_texto("Ingrese la categoría: ").title()
    precio = leer_numero_positivo("Ingrese el precio sin IVA: $")
    stock = leer_entero_no_negativo("Ingrese el stock inicial: ")

    productos[codigo] = {   
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
        }

    categorias.add(categoria)
    if stock > 0:
        movimientos.append({
            "codigo": codigo,
            "producto": nombre,
            "tipo": "Entrada inicial",
            "cantidad": stock
        })
    print(f"El producto '{nombre}' fue agregado correctamente.")
    return True

#mostrar los productos.
def mostrar_productos():
    print("\n--- LISTA DE PRODUCTOS ---")
    if len(productos) == 0:
        print("No hay productos registrados.")
        return
    for codigo, producto in productos.items():

        precio_con_iva = calcular_precio_con_iva(
            producto["precio"]
        )
        if producto["stock"] == 0:
            estado = "Sin stock"
        elif producto["stock"] <= 5:
            estado = "Stock bajo"
        else:
            estado = "Disponible"

        print("\n------------------------------")
        print(f"Código: {codigo}")
        print(f"Nombre: {producto['nombre']}")
        print(f"Categoría: {producto['categoria']}")
        print(
            f"Precio sin IVA: "
            f"{formatear_pesos(producto['precio'])}"
        )
        print(
            f"Precio con IVA: "
            f"{formatear_pesos(precio_con_iva)}"
        )
        print(f"Stock: {producto['stock']}")
        print(f"Estado: {estado}")

    print("------------------------------")
def obtener_producto(codigo):
    codigo = codigo.upper()
    return productos.get(codigo)

def buscar_producto():
    print("\n--- Buscar producto ---")
    codigo = leer_texto(
        "Ingrese el código del producto: "
    ).upper()

    producto = obtener_producto(codigo)
    if producto is None:
        print("Producto no encontrado.")
        return

    precio_con_iva = calcular_precio_con_iva(
        producto["precio"]
    )

    print("\nProducto encontrado")
    print(f"Código: {codigo}")
    print(f"Nombre: {producto['nombre']}")
    print(f"Categoría: {producto['categoria']}")
    print(
        f"Precio sin IVA: "
        f"{formatear_pesos(producto['precio'])}"
    )
    print(
        f"Precio con IVA: "
        f"{formatear_pesos(precio_con_iva)}"
    )
    print(f"Stock: {producto['stock']}")

def modificar_producto():
    print("\n--- Modificar producto ---")

    codigo = leer_texto(
        "Ingrese el código del producto: "
    ).upper()

    producto = obtener_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
        return False

    while True:
        print("\n1. Modificar nombre")
        print("2. Modificar categoría")
        print("3. Modificar precio")
        print("4. Volver al menú principal")

        opcion = leer_opcion(
            "Seleccione una opción: ",
            ("1", "2", "3", "4")
        )

        if opcion == "1":
            nuevo_nombre = leer_texto(
                "Ingrese el nuevo nombre: "
            ).title()

            producto["nombre"] = nuevo_nombre

            print("Nombre modificado correctamente.")

        elif opcion == "2":
            nueva_categoria = leer_texto(
                "Ingrese la nueva categoría: "
            ).title()

            producto["categoria"] = nueva_categoria
            actualizar_categorias()

            print("Categoría modificada correctamente.")

        elif opcion == "3":
            nuevo_precio = leer_numero_positivo(
                "Ingrese el nuevo precio: $"
            )

            producto["precio"] = nuevo_precio

            print("Precio modificado correctamente.")

        elif opcion == "4":
            print("Regresando al menú principal...")
            break

    return True

def eliminar_producto():
    print("\n--- Eliminar producto ---")

    codigo = leer_texto(
        "Ingrese el código del producto: "
    ).upper()

    producto = obtener_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
        return False

    print(f"Producto encontrado: {producto['nombre']}")

    confirmacion = leer_opcion(
        "¿Confirma que desea eliminarlo? (si/no): ",
        ("si", "SI","sI", "Si", "chi", "no", "NO", "No", "nO", "nop")
    )

    if confirmacion.lower() == "no":
        print("Eliminación cancelada.")
        return False

    del productos[codigo]

    actualizar_categorias()

    print("Producto eliminado correctamente.")

    return True

#Stock
def registrar_entrada():
    print("\n--- Registrar entrada de stock ---")

    codigo = leer_texto(
        "Ingrese el código del producto: "
    ).upper()

    producto = obtener_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
        return False

    cantidad = leer_entero_no_negativo(
        "Ingrese la cantidad de entrada: "
    )

    if cantidad == 0:
        print("La cantidad debe ser mayor que cero.")
        return False

    producto["stock"] = producto["stock"] + cantidad

    movimientos.append({
        "codigo": codigo,
        "producto": producto["nombre"],
        "tipo": "Entrada",
        "cantidad": cantidad
    })

    print("Entrada registrada correctamente.")
    print(f"Nuevo stock: {producto['stock']}")

    return True

def registrar_salida():
    print("\n--- Registrar salida de stock ---")

    codigo = leer_texto(
        "Ingrese el código del producto: "
    ).upper()

    producto = obtener_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
        return False

    cantidad = leer_entero_no_negativo(
        "Ingrese la cantidad de salida: "
    )

    if cantidad == 0:
        print("La cantidad debe ser mayor que cero.")
        return False

    if cantidad > producto["stock"]:
        print("No existe stock suficiente.")
        print(f"Stock disponible: {producto['stock']}")

        return False

    producto["stock"] = producto["stock"] - cantidad

    movimientos.append({
        "codigo": codigo,
        "producto": producto["nombre"],
        "tipo": "Salida",
        "cantidad": cantidad
    })

    print("Salida registrada correctamente.")
    print(f"Nuevo stock: {producto['stock']}")

    return True

#valor total del inventario
def calcular_valor_inventario():
    total = 0

    for producto in productos.values():
        subtotal = producto["precio"] * producto["stock"]
        total = total + subtotal

    return total

def mostrar_valor_inventario():
    print("\n--- Valor total del inventario ---")

    if len(productos) == 0:
        print("No hay productos registrados.")
        return

    total_sin_iva = calcular_valor_inventario()

    total_con_iva = calcular_precio_con_iva(
        total_sin_iva
    )

    print(
        f"Valor total sin IVA: "
        f"{formatear_pesos(total_sin_iva)}"
    )

    print(
        f"Valor total con IVA: "
        f"{formatear_pesos(total_con_iva)}"
    )

#mostrar las categorías
def mostrar_categorias():
    print("\n--- Categorías registradas---")

    actualizar_categorias()

    if len(categorias) == 0:
        print("No hay categorías registradas.")
        return

    for categoria in sorted(categorias):
        print(f"- {categoria}")

#mostrar los movimientos
def mostrar_movimientos():
    print("\n--- Historial de movimienttos ---")

    if len(movimientos) == 0:
        print("No hay movimientos registrados.")
        return

    contador = 1

    for movimiento in movimientos:
        print(
            f"{contador}. "
            f"{movimiento['tipo']} | "
            f"Código: {movimiento['codigo']} | "
            f"Producto: {movimiento['producto']} | "
            f"Cantidad: {movimiento['cantidad']}"
        )

        contador = contador + 1
        