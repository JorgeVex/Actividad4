""" 
Escribir un programa en Python que guarde la temperatura mínima y máxima de los
últimos 5 días. El programa debe recibir la información, almacenarla y mostrar:
● La temperatura media de cada día
● Los días con menor temperatura
● Después de almacenar la información de los 5 días, el programa debe recinir una
temperatura más por teclado y mostrar los días cuya temperatura máxima coincide
con ella. si no existe ningún día se muestra un mensaje de información
"""
class RegistroTemperaturas():
    
    def __init__(self):
        self.temperaturas = []
        
    def registrar_temperaturas(self):
        #Se piden las temperaturas para 5 días
        for dia in range (1, 6):
            temp_min = float(input(f"Introduce la temperatura minima del día {dia}: "))
            temp_max = float(input(f"Introduce la temperatura maxima del día {dia}: "))
            #Guardamos las temperaturas como una tupla
            self.temperaturas.append((temp_min, temp_max))
    
    def calcular_temperatura_media(self):
        #Calculamos y mostramos la temperatura media de cada día
        print("\n Temperaturas medias de cada dia: ")
        for i, (temp_min, temp_max) in enumerate (self.temperaturas):
            media = (temp_min + temp_max) / 2
            print(f"Dia {i + 1}: Temperatura media = {media} °C")
    
    def mostrar_dia_menor_temperatura(self):
        min_temperatura = min(self.temperaturas, key=lambda x: x[0])[0]
        print(f"\n Dias con menor temperatura: ")
        for i, (temp_min, _) in enumerate(self.temperaturas):
            if temp_min == min_temperatura:
                print(f"\n Dia {i+1} con la temperatura minima de: {temp_min} °C")
    
    def buscar_por_temperatura_maxima(self):
        # Pedimos una temperatura extra para buscar coincidencias con la máxima
        temp_extra = float(input("\nIntroduce una temperatura máxima para buscar coincidencias: "))
        coincidencias = []
        
        # Verificamos si la temperatura máxima coincide con la ingresada
        for i, (_, temp_max) in enumerate(self.temperaturas):
            if temp_max == temp_extra:
                coincidencias.append(i + 1)
        
        if coincidencias:
            print(f"Día(s) con una temperatura máxima de {temp_extra}°C: corresponde a los dias: {coincidencias}")
        else:
            print(f"No hay días con una temperatura máxima de {temp_extra}°C.")

#Instanciamos la clase
registro = RegistroTemperaturas()

#Llamamos los métodos en el orden solicitado
registro.registrar_temperaturas()
registro.calcular_temperatura_media()
registro.mostrar_dia_menor_temperatura()
registro.buscar_por_temperatura_maxima()