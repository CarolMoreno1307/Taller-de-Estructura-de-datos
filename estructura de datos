import sqlite3

class ListaCalculadora:
    def __init__(self):
        self.lista = []  # Array en memoria
        self.conn = sqlite3.connect('datos.db')
        self.c = self.conn.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS numeros(valor REAL)')
        self.conn.commit()

    def menu(self):
        while True:
            print("\n1. Añadir 2. Calcular 3. Mostrar 0. Salir")
            op = input("> ")
            
            if op == '1':
                num = float(input("Número: "))
                self.lista.append(num)  # Guarda en el array
                self.c.execute('INSERT INTO numeros VALUES(?)', (num,))  # Guarda en DB
                self.conn.commit()
            
            elif op == '2':
                if len(self.lista) < 2:
                    print("Necesitas 2 números")
                    continue
                a, b = self.lista[-2], self.lista[-1]  # Usa los últimos 2 del array
                print(f"Suma: {a+b}, Resta: {a-b}, Multi: {a*b}, Div: {a/b if b!=0 else 'Error'}")
            
            elif op == '3':
                print("\nArray actual:", self.lista)
                print("Base de datos:")
                for row in self.c.execute('SELECT * FROM numeros'):
                    print(row[0])
            
            elif op == '0':
                self.conn.close()
                break

ListaCalculadora().menu()
