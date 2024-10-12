""" 
Escribir un programa en Python que declare una lista y la vaya llenando de números hasta
que introduzcamos un número negativo. Entonces se debe imprimir el vector (sólo los
valores introducidos).
"""


class Ejercicio1():
    
    def __init__(self):
        
        #inicializamos una lista vacía que almacenará los numero ingresados
        self.lista_numeros = []
    
    def escribirNumeros(self):
        
        # Continuamos solicitando números al usuario hasta que se ingrese un número negativo.
        while True:
            numero = int(input(f"Ingresa cualquier numero, si deseas terminar la ejecución agrega un valor negativo: "))
            
            if numero < 0: #El bucle se detiene cuando se agrega un valor menor a 0
                break
            
            # Agregamos el número a la lista y mostramos los valores introducidos.            
            self.lista_numeros.append(numero)
            print(f"Los numeros introducidos fueron {self.lista_numeros}")

# Creamos una instancia de la clase y llamamos al método que solicita los números.
ejercio1 = Ejercicio1()

ejercio1.escribirNumeros()
    