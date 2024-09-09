import numpy as np

# Datos de ejemplo: Temperaturas diarias en 3 ciudades, 7 días de la semana y 4 semanas
# Vamos a usar temperaturas fijas para la demostración.

# Definimos la matriz 3D con temperaturas fijas para las 3 ciudades, 7 días y 4 semanas
# Formato: [ciudad, día de la semana, semana]
temperaturas = np.array([
    # QUITO
    [
        [22, 24, 23, 21],  # Lunes
        [20, 22, 21, 20],  # Martes
        [19, 21, 20, 18],  # Miércoles
        [21, 23, 22, 20],  # Jueves
        [22, 25, 24, 22],  # Viernes
        [24, 26, 25, 23],  # Sábado
        [26, 27, 26, 24]   # Domingo
    ],
    # CUENCA
    [
        [15, 17, 16, 14],  # Lunes
        [14, 16, 15, 13],  # Martes
        [13, 15, 14, 12],  # Miércoles
        [14, 16, 15, 13],  # Jueves
        [15, 17, 16, 14],  # Viernes
        [16, 18, 17, 15],  # Sábado
        [18, 19, 18, 16]   # Domingo
    ],
    # LOJA
    [
        [30, 32, 31, 29],  # Lunes
        [29, 31, 30, 28],  # Martes
        [28, 30, 29, 27],  # Miércoles
        [30, 32, 31, 29],  # Jueves
        [32, 33, 32, 30],  # Viernes
        [33, 34, 33, 31],  # Sábado
        [34, 35, 34, 32]   # Domingo
    ]
])

# Función para calcular el promedio de temperaturas para cada ciudad y semana
def calcular_promedios(matriz):
    num_ciudades, num_dias, num_semanas = matriz.shape
    promedios_semanales = np.zeros((num_ciudades, num_semanas))

    for ciudad in range(num_ciudades):
        for semana in range(num_semanas):
            promedio = np.mean(matriz[ciudad, :, semana])
            promedios_semanales[ciudad, semana] = promedio

    return promedios_semanales

# Calculamos los promedios
promedios = calcular_promedios(temperaturas)

# Mostrar los resultados
ciudades = ["QUITO", "CUENCA", "LOJA"]
semanas = ["Semana 1", "Semana 2", "Semana 3", "Semana 4"]

print("Promedio de temperaturas por ciudad y semana:")
for i, ciudad in enumerate(ciudades):
    print(f"\n{ciudad}:")
    for j, semana in enumerate(semanas):
        print(f"{semana}: {promedios[i, j]:.2f} °C")

# Para visualizar las temperaturas en la matriz
print("\nMatriz de temperaturas (ciudades x días x semanas):")
print(temperaturas)
