class lista_numeros:
    def __init__(self):
        self.lista_numero = []
        
    def guardar_numero(self, dato_numero):
        """Guarda un par de números en la lista"""
        if isinstance(dato_numero, list) and len(dato_numero) == 2:
            self.lista_numero.append(dato_numero)
            print(f"Guardado: {dato_numero} | Lista actual: {self.lista_numero}")
        else:
            print("Error: Debe ingresar una lista con 2 números")
    
    def incluir_lista(self, lista_nueva):
        """Extiende la lista con múltiples pares"""
        if all(isinstance(par, list) and len(par) == 2 for par in lista_nueva):
            self.lista_numero.extend(lista_nueva)
            print(f"Lista extendida | Total: {len(self.lista_numero)} pares")
        else:
            print("Error: Todos los elementos deben ser listas de 2 números")
    
    def insertar_dato(self, posicion, dato):
        """Inserta un par en posición específica"""
        if 0 <= posicion <= len(self.lista_numero):
            self.lista_numero.insert(posicion, dato)
            print(f"Insertado en posición {posicion} | Lista: {self.lista_numero}")
        else:
            print("Error: Posición inválida")
        
    def eliminar_dato(self, dato):
        """Elimina un par específico"""
        if dato in self.lista_numero:
            self.lista_numero.remove(dato)
            print(f"Eliminado: {dato} | Lista actual: {self.lista_numero}")
        else:
            print(f"Error: {dato} no encontrado")
    
    def ver_numero(self):
        """Muestra todos los pares almacenados"""
        print("\n--- LISTA COMPLETA ---")
        for i, par in enumerate(self.lista_numero):
            print(f"{i+1}. {par}")
        return self.lista_numero
