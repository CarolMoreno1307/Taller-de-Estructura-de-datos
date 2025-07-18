class GestorNumeros:
    def __init__(self):
        self.lista_numeros = []
        self.tupla_pares = ()
        self.tupla_impares = ()
    

    # FUNCIONES DE LISTA

    def agregar_par(self, num1, num2):
        self.lista_numeros.append([num1, num2])

    def eliminar_ultimo(self):
        if self.lista_numeros:
            return self.lista_numeros.pop()
        else:
            return None

    def insertar_en_posicion(self, posicion, num1, num2):
        if 0 <= posicion <= len(self.lista_numeros):
            self.lista_numeros.insert(posicion, [num1, num2])
            return True
        return False

    def eliminar_par(self, num1, num2):
        try:
            self.lista_numeros.remove([num1, num2])
            return True
        except ValueError:
            return False

    def buscar_par(self, num1, num2):
        try:
            return self.lista_numeros.index([num1, num2])
        except ValueError:
            return -1

    def obtener_lista(self):
        return self.lista_numeros

    # FUNCIONES DE TUPLAS

    def crear_tupla_pares(self, lista):
        self.tupla_pares = tuple(
            [
                n for n in lista if n % 2 == 0
            ]
        )

    def crear_tupla_impares(self, lista):
        self.tupla_impares = tuple(
            [
                n for n in lista if n % 2 != 0
            ]
        )

    def modificar_tupla(self, tipo, indice, nuevo_valor):
        if tipo == "par":
            if 0 <= indice < len(self.tupla_pares):
                l = list(self.tupla_pares)
                l[indice] = nuevo_valor
                self.tupla_pares = tuple(l)
                return True
        elif tipo == "impar":
            if 0 <= indice < len(self.tupla_impares):
                l = list(self.tupla_impares)
                l[indice] = nuevo_valor
                self.tupla_impares = tuple(l)
                return True
        return False

    def eliminar_de_tupla(self, tipo, valor):
        if tipo == "par":
            if valor in self.tupla_pares:
                l = list(self.tupla_pares)
                l.remove(valor)
                self.tupla_pares = tuple(l)
                return True
        elif tipo == "impar":
            if valor in self.tupla_impares:
                l = list(self.tupla_impares)
                l.remove(valor)
                self.tupla_impares = tuple(l)
                return True
        return False

    def obtener_tuplas(self):
        return self.tupla_pares, self.tupla_impares
