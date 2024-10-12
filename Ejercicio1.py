""" 
Escribir un programa en Python que declare una lista y la vaya llenando de números hasta
que introduzcamos un número negativo. Entonces se debe imprimir el vector (sólo los
valores introducidos).
"""


class Ejercicio1():
    
    def __init__(self):
        self.lista_numeros = []
    
    def escribirNumeros(self):
        
        while True:
            numero = int(input(f"Ingresa cualquier numero, si deseas terminar la ejecución agrega un valor negativo: "))
            
            if numero < 0:
                break
            
            self.lista_numeros.append(numero)
            print(f"Los numeros introducidos fueron {self.lista_numeros}")

ejercio1 = Ejercicio1()

ejercio1.escribirNumeros()
    