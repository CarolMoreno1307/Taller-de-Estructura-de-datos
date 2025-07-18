from base_datos import GestorNumeros


class InterfazConsola:
    def __init__(self):
        self.gestor = GestorNumeros()

    def pedir_par(self):
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        return num1, num2

    def pedir_lista(self):
        entrada = input("Ingrese varios números separados por espacio: ")
        return [int(n) for n in entrada.split()]

    def submenu_tuplas(self, tipo):
        while True:
            print(f"\n--- SUBMENÚ TUPLA {tipo.upper()} ---\n1. Modificar un valor de la tupla \n2. Eliminar un valor de la tupla \n3. Mostrar tupla \n4. Volver al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                indice = int(input("Ingrese el índice que desea modificar: "))
                nuevo_valor = int(input("Ingrese el nuevo valor: "))
                if self.gestor.modificar_tupla(tipo, indice, nuevo_valor):
                    print("Valor modificado.")
                else:
                    print("Índice inválido.")
            elif opcion == "2":
                valor = int(input("Ingrese el valor que desea eliminar: "))
                if self.gestor.eliminar_de_tupla(tipo, valor):
                    print("Valor eliminado.")
                else:
                    print("Valor no encontrado.")
            elif opcion == "3":
                pares, impares = self.gestor.obtener_tuplas()
                print("Tupla Par:", pares)
                print("Tupla Impar:", impares)
            elif opcion == "4":
                break
            else:
                print("Opción inválida.")

    def mostrar_menu(self):
        print(" \n --- MENÚ --- \n 1. Agregar nuevo par \n 2. Eliminar el último par (pop) \n 3. Insertar par en una posición específica \n 4. Eliminar un par específico (remove) \n 5. Buscar índice de un par (index) \n 6. Mostrar todos los pares \n 7. Crear tupla con números pares \n 8. Crear tupla con números impares \n 9. Gestionar tupla de pares \n 10. Gestionar tupla de impares \n11. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                num1, num2 = self.pedir_par()
                self.gestor.agregar_par(num1, num2)
                print("Par agregado exitosamente.")

            elif opcion == "2":
                eliminado = self.gestor.eliminar_ultimo()
                print(f"Par eliminado: {eliminado}" if eliminado else "La lista está vacía.")

            elif opcion == "3":
                try:
                    posicion = int(input("Ingrese la posición en la que desea insertar: "))
                    num1, num2 = self.pedir_par()
                    if self.gestor.insertar_en_posicion(posicion, num1, num2):
                        print("Par insertado correctamente.")
                    else:
                        print("Posición inválida.")
                except ValueError:
                    print("Entrada inválida. Ingrese solo números.")

            elif opcion == "4":
                num1, num2 = self.pedir_par()
                if self.gestor.eliminar_par(num1, num2):
                    print("Par eliminado exitosamente.")
                else:
                    print("Par no encontrado en la lista.")

            elif opcion == "5":
                num1, num2 = self.pedir_par()
                indice = self.gestor.buscar_par(num1, num2)
                print(f"El par se encuentra en la posición: {indice}" if indice != -1 else "Par no encontrado.")

            elif opcion == "6":
                pares = self.gestor.obtener_lista()
                print("Lista actual de pares:")
                for i, par in enumerate(pares):
                    print(f"{i}: {par}")

            elif opcion == "7":
                lista = self.pedir_lista()
                self.gestor.crear_tupla_pares(lista)
                print("Tupla de pares creada.")

            elif opcion == "8":
                lista = self.pedir_lista()
                self.gestor.crear_tupla_impares(lista)
                print("Tupla de impares creada.")

            elif opcion == "9":
                self.submenu_tuplas("par")

            elif opcion == "10":
                self.submenu_tuplas("impar")

            elif opcion == "11":
                print("Saliendo del programa.")
                break

            else:
                print("Opción inválida. Intente de nuevo.")

# Ejecución principal
if __name__ == "__main__":
    app = InterfazConsola()
    app.ejecutar()
