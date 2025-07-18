import base_datos

def pedir_par():
    """Solicita al usuario dos números enteros"""
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    return num1, num2

def pedir_lista():
    """Solicita al usuario una lista de números"""
    entrada = input("Ingrese varios números separados por espacio: ")
    return [int(n) for n in entrada.split()]

def submenu_tuplas(tipo):
    """Submenú para modificar o eliminar elementos de tuplas"""
    while True:
        print(f"\n--- SUBMENÚ TUPLA {tipo.upper()} ---\n1. Modificar un valor de la tupla \n2. Eliminar un valor de la tupla \n3. Mostrar tupla \n4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            indice = int(input("Ingrese el índice que desea modificar: "))
            nuevo_valor = int(input("Ingrese el nuevo valor: "))
            if base_datos.modificar_tupla(tipo, indice, nuevo_valor):
                print("Valor modificado.")
            else:
                print("Índice inválido.")

        elif opcion == "2":
            valor = int(input("Ingrese el valor que desea eliminar: "))
            if base_datos.eliminar_de_tupla(tipo, valor):
                print("Valor eliminado.")
            else:
                print("Valor no encontrado.")

        elif opcion == "3":
            pares, impares = base_datos.obtener_tuplas()
            print("Tupla Par:", pares)
            print("Tupla Impar:", impares)

        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

def mostrar_menu():
    """Imprime el menú de opciones"""
    print(" \n --- MENÚ --- \n 1. Agregar nuevo par \n 2. Eliminar el último par (pop) \n 3. Insertar par en una posición específica \n 4. Eliminar un par específico (remove) \n 5. Buscar índice de un par (index) \n 6. Mostrar todos los pares \n 7. Crear tupla con números pares \n 8. Crear tupla con números impares \n 9. Gestionar tupla de pares \n 10. Gestionar tupla de impares \n11. Salir")

def main():
    """Punto de entrada principal del programa"""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            num1, num2 = pedir_par()
            base_datos.agregar_par(num1, num2)
            print("Par agregado exitosamente.")

        elif opcion == "2":
            eliminado = base_datos.eliminar_ultimo()
            print(f"Par eliminado: {eliminado}" if eliminado else "La lista está vacía.")

        elif opcion == "3":
            try:
                posicion = int(input("Ingrese la posición en la que desea insertar: "))
                num1, num2 = pedir_par()
                if base_datos.insertar_en_posicion(posicion, num1, num2):
                    print("Par insertado correctamente.")
                else:
                    print("Posición inválida.")
            except ValueError:
                print("Entrada inválida. Ingrese solo números.")

        elif opcion == "4":
            num1, num2 = pedir_par()
            if base_datos.eliminar_par(num1, num2):
                print("Par eliminado exitosamente.")
            else:
                print("Par no encontrado en la lista.")

        elif opcion == "5":
            num1, num2 = pedir_par()
            indice = base_datos.buscar_par(num1, num2)
            print(f"El par se encuentra en la posición: {indice}" if indice != -1 else "Par no encontrado.")

        elif opcion == "6":
            pares = base_datos.obtener_lista()
            print("Lista actual de pares:")
            for i, par in enumerate(pares):
                print(f"{i}: {par}")

        elif opcion == "7":
            lista = pedir_lista()
            base_datos.crear_tupla_pares(lista)
            print("Tupla de pares creada.")

        elif opcion == "8":
            lista = pedir_lista()
            base_datos.crear_tupla_impares(lista)
            print("Tupla de impares creada.")

        elif opcion == "9":
            submenu_tuplas("par")

        elif opcion == "10":
            submenu_tuplas("impar")

        elif opcion == "11":
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
