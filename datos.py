#Diccionario para guardar los productos
productos = {}

#Lista para guardar las entradas y salidas de stock
movimientos = []

#Conjunto para guardar las categorías sin repetirlas
categorias = set()

#Tupla con información que no se modificará IVA
CONFIGURACION = (
    "Sistema de Gestión de Inventario",
    0.19
)