# Actividad 4 - Fundamentos en Ciencia de Datos

Este proyecto está compuesto por 4 ejercicios desarrollados en Python, utilizando el paradigma de Programación Orientada a Objetos (POO). A continuación se describe la estructura del proyecto y la funcionalidad de cada uno de los ejercicios. Cabe destacar que el **Ejercicio 5** no fue realizado por recomendación del profesor.

## Grupo conformado por los estudiantes:
*Yuleidy Cruz Valbuena* **ID Banner: 100171731**
*Jorge Hernán Velasco Gómez* **ID Banner: 100184860**

## Estructura del Proyecto

El proyecto contiene los siguientes archivos:

- **Ejercicio1.py**: Programa para almacenar números en una lista hasta que se introduzca un número negativo.
- **Ejercicio2.py**: Programa que realiza la suma de dos listas de 5 números enteros cada una.
- **Ejercicio3.py**: Programa que almacena y analiza temperaturas mínimas y máximas de los últimos 5 días.
- **Ejercicio4.py**: Juego en el que el usuario debe adivinar un número generado aleatoriamente del 1 al 100 con un límite de 10 intentos.
- **README.md**: Archivo explicativo de la estructura del proyecto.

## Paradigma Utilizado

Este proyecto implementa el paradigma de Programación Orientada a Objetos (POO), donde los ejercicios se estructuran a partir de clases. Cada clase encapsula atributos y métodos que gestionan la lógica de cada ejercicio.

### Ejercicio 1: Declarar una lista hasta ingresar un número negativo

- **Clase:** `Ejercicio1`
- **Métodos:**
  - `__init__`: Inicializa una lista vacía llamada `lista_numeros`.
  - `escribirNumeros`: Permite al usuario ingresar números enteros hasta que se ingrese un número negativo. Los números son almacenados en la lista y se muestran en pantalla.
  
El uso del método `__init__` es fundamental para la inicialización de la lista donde se guardarán los números. Esto permite que la lista esté disponible para el método que se encargará de manejar los datos.

### Ejercicio 2: Suma de dos listas

- **Clase:** `Ejercicio2`
- **Métodos:**
  - `__init__`: Inicializa tres listas: `lista1`, `lista2`, y `lista3` para almacenar los valores ingresados por el usuario y el resultado de la suma.
  - `ingresar_valores_listas`: Permite al usuario ingresar valores para las dos listas, luego realiza la suma de ambas y almacena el resultado en `lista3`.

El método `__init__` en este caso es importante para inicializar las tres listas, lo cual permite que se mantenga la separación entre las listas originales y la lista resultante.

### Ejercicio 3: Registro y análisis de temperaturas

- **Clase:** `RegistroTemperaturas`
- **Métodos:**
  - `__init__`: Inicializa una lista vacía `temperaturas` para almacenar las temperaturas mínimas y máximas de los últimos 5 días.
  - `registrar_temperaturas`: Solicita al usuario ingresar las temperaturas mínimas y máximas de 5 días y las almacena en una lista de tuplas.
  - `calcular_temperatura_media`: Calcula y muestra la temperatura media de cada día.
  - `mostrar_dia_menor_temperatura`: Muestra el día con la temperatura mínima más baja.
  - `buscar_por_temperatura_maxima`: Permite al usuario buscar los días cuya temperatura máxima coincide con un valor ingresado.

Aquí, el método `__init__` se utiliza para inicializar la lista que almacenará las tuplas de temperaturas, facilitando la gestión de datos para los métodos posteriores.

### Ejercicio 4: Adivina el número

- **Clase:** `AdivinaElNumero`
- **Métodos:**
  - `__init__`: Genera un número aleatorio del 1 al 100, inicializa los intentos restantes a 10 e inicializa un contador de intentos actuales.
  - `jugar`: Solicita al usuario que adivine el número generado, proporcionando pistas si el número es mayor o menor que el ingresado, e informa si el usuario acierta o se queda sin intentos.

El método `__init__` aquí es clave para la configuración del juego, ya que establece el número a adivinar y controla la cantidad de intentos.

## Nota sobre el Ejercicio 5

Por recomendación del profesor, el **Ejercicio 5** no fue realizado como parte de esta actividad.

---

Este proyecto ha sido desarrollado como parte del curso de **Fundamentos en Ciencia de Datos** y emplea POO para organizar la funcionalidad de los ejercicios en clases y métodos, facilitando la lectura y reutilización del código.
