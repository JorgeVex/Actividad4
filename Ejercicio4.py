""" 
Crea un programa en Python que permita adivinar un número. La aplicación genera un
número aleatorio del 1 al 100. A continuación, va pidiendo números y va respondiendo si
el número a adivinar es mayor o menor que el introducido, así como el número de intentos
que quedan, se contarán con 10 intentos para adivinar el número). El programa termina
cuando se acierta el número y debe indicar en que intento fue acertado, si se llega al límite
de intentos, el programa debe mostrar que se había generado.
"""

import random

class AdivinaElNumero:
    
    def __init__(self):
        self.numero_a_adivinar = random.randint(1, 100)
        self.intentos_restantes = 10
        self.intento_actual = 0
    
    def jugar(self):
        print("¡Bienvenido al juego de adivinar el número!")
        print("Tienes 10 intentos para adivinar un número entre 1 y 100.\n")

        while self.intentos_restantes > 0:
            try:
                intento = int(input("Introduce un número: "))
                self.intento_actual += 1
                self.intentos_restantes -= 1

                if intento == self.numero_a_adivinar:
                    print(f"¡Felicidades! Adivinaste el número: '{self.numero_a_adivinar}' en el intento #{self.intento_actual}.\n")
                    break
                elif intento < self.numero_a_adivinar:
                    print(f"El número es mayor que {intento}. Intentos restantes: {self.intentos_restantes}")
                else:
                    print(f"El número es menor que {intento}. Intentos restantes: {self.intentos_restantes}")
            
            except ValueError:
                print("Por favor, introduce un número válido.")

        if self.intentos_restantes == 0:
            print(f"\nTe has quedado sin intentos. El número que debías adivinar era: {self.numero_a_adivinar}")

# Crear una instancia del juego
juego = AdivinaElNumero()

# Iniciar el juego
juego.jugar()
