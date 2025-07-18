lista_numeros = []
tupla_pares = ()
tupla_impares = ()

# FUNCIONES DE LISTA 

def agregar_par(num1, num2):
    """Agrega un par de números como sublista a la lista principal usando append()"""
    lista_numeros.append([num1, num2])

def eliminar_ultimo():
    """Elimina el último par ingresado usando pop()"""
    if lista_numeros:
        return lista_numeros.pop()
    else:
        return None

def insertar_en_posicion(posicion, num1, num2):
    """Inserta un par en una posición específica usando insert()"""
    if 0 <= posicion <= len(lista_numeros):
        lista_numeros.insert(posicion, [num1, num2])
        return True
    return False

def eliminar_par(num1, num2):
    """Elimina el primer par que coincida completamente usando remove()"""
    try:
        lista_numeros.remove([num1, num2])
        return True
    except ValueError:
        return False

def buscar_par(num1, num2):
    """Busca un par específico y devuelve su índice usando index()"""
    try:
        return lista_numeros.index([num1, num2])
    except ValueError:
        return -1

def obtener_lista():
    """Devuelve la lista completa de pares"""
    return lista_numeros

# FUNCIONES DE TUPLAS

def crear_tupla_pares(lista):
    """Crea la tupla de números pares a partir de una lista"""
    global tupla_pares
    tupla_pares = tuple(
        [
            n for n in lista if n % 2 == 0
        ]
    )

def crear_tupla_impares(lista):
    """Crea la tupla de números impares a partir de una lista"""
    global tupla_impares
    tupla_impares = tuple(
        [
            n for n in lista if n % 2 != 0
        ]
    )

def modificar_tupla(tipo, indice, nuevo_valor):
    """Modifica un valor en la tupla (par o impar) convirtiéndola a lista temporalmente"""
    global tupla_pares, tupla_impares
    if tipo == "par":
        if 0 <= indice < len(tupla_pares):
            l = list(tupla_pares)
            l[indice] = nuevo_valor
            tupla_pares = tuple(l)
            return True
    elif tipo == "impar":
        if 0 <= indice < len(tupla_impares):
            l = list(tupla_impares)
            l[indice] = nuevo_valor
            tupla_impares = tuple(l)
            return True
    return False

def eliminar_de_tupla(tipo, valor):
    """Elimina un valor de la tupla (par o impar) convirtiéndola a lista"""
    global tupla_pares, tupla_impares
    if tipo == "par":
        if valor in tupla_pares:
            l = list(tupla_pares)
            l.remove(valor)
            tupla_pares = tuple(l)
            return True
    elif tipo == "impar":
        if valor in tupla_impares:
            l = list(tupla_impares)
            l.remove(valor)
            tupla_impares = tuple(l)
            return True
    return False

def obtener_tuplas():
    """Devuelve las tuplas de pares e impares"""
    return tupla_pares, tupla_impares
