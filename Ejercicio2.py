""" 
Escribir un programa en Python que declare tres listas 'lista1', 'lista2' y 'lista3' de cinco
enteros cada uno, pida valores para 'lista1' y 'lista2' y calcule lista3=lista1+lista2.
"""

class Ejercicio2():
    
    def __init__(self):
        self.lista1 = []
        self.lista2 = []
        self.lista3 = []
        
    def ingresar_valores_listas(self):
        
        intentos = 5
        
        while True:
            
            for i in range(intentos):
                valor = int(input(f"Ingresa los valores para la PRIMER lista: "))
                self.lista1.append(valor)
                print(f"Valores agregados para la lista 1: {self.lista1}")
            break
        
        while True:
            
            for i in range(intentos):
                valor = int(input(f"Agrega los valores para la SEGUNDA lista: "))
                self.lista2.append(valor)
                print(f"Valores agregados para la lista 2: {self.lista2}")
            break

        #Sumamos las listas y mostramos la lista3
        
        self.lista3 = self.lista1 + self.lista2
        print(f"Lista 3 (Lista1 + Lista2): {self.lista3} listas concatenadas")
        
ejercicio2 = Ejercicio2()
ejercicio2.ingresar_valores_listas()
        