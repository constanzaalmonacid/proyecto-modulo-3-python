# Importamos la configuración del sistema.
from datos import CONFIGURACION

# Importamos las funciones del programa.
from funciones import (
    agregar_producto,
    mostrar_productos,
    buscar_producto,
    modificar_producto,
    eliminar_producto,
    registrar_entrada,
    registrar_salida,
    mostrar_valor_inventario,
    mostrar_categorias,
    mostrar_movimientos
)


# Función que muestra el menú principal.
def mostrar_menu():
    print(CONFIGURACION[0].upper())
    print("---------------------------------")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Modificar producto")
    print("5. Eliminar producto")
    print("6. Registrar entrada de stock")
    print("7. Registrar salida de stock")
    print("8. Calcular valor total del inventario")
    print("9. Mostrar categorías")
    print("10. Mostrar movimientos")
    print("11. Salir")


# Función principal.
def main():
    while True:
        mostrar_menu()

        opcion = input(
            "Seleccione una opción: "
        ).strip()

        if opcion == "1":
            agregar_producto()

        elif opcion == "2":
            mostrar_productos()

        elif opcion == "3":
            buscar_producto()

        elif opcion == "4":
            modificar_producto()

        elif opcion == "5":
            eliminar_producto()

        elif opcion == "6":
            registrar_entrada()

        elif opcion == "7":
            registrar_salida()

        elif opcion == "8":
            mostrar_valor_inventario()

        elif opcion == "9":
            mostrar_categorias()

        elif opcion == "10":
            mostrar_movimientos()

        elif opcion == "11":
            print("\nPrograma finalizado.")
            print("¡Hasta pronto!")
            break

        else:
            print("\nOpción inválida.")
            print("Intente nuevamente.")
            continue


# Iniciamos el programa.
if __name__ == "__main__":
    main()