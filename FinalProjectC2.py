"""
Autores: 
Andrés Felipe VanegasBogotá
Sergio Andrés Sanabria Castillo
Carlos Andrés Sinuco Murcia

Descripción:
Este programa utiliza el algoritmo Ant Colony Optimization (ACO) para resolver el problema del viajante (TSP) 
para un conjunto de ciudades colombianas, el programa recibe del usuario el nombre de la ciudad inicial y luego calcula 
la mejor ruta para visitar todas las ciudades y regresar a la ciudad de inicio.
"""

import numpy as np
import matplotlib.pyplot as plt

def calcular_distancia(ciudad1, ciudad2):
    """Calcula la distancia euclidiana en 3D entre dos ciudades, incluyendo la altitud."""
    return np.linalg.norm(np.array(ciudad1) - np.array(ciudad2))

def inicializar_feromonas(n):
    """Inicializa la matriz de feromonas con valores predeterminados."""
    return np.ones((n, n))

def elegir_siguiente_ciudad(feromonas, distancias, actual, no_visitadas, alpha, beta):
    """Elige la siguiente ciudad basada en la probabilidad de transición."""
    feromonas_actual = feromonas[actual, no_visitadas]
    distancias_actual = distancias[actual, no_visitadas]
    probabilidades = (feromonas_actual ** alpha) * ((1 / distancias_actual) ** beta)
    probabilidades /= probabilidades.sum()
    return np.random.choice(no_visitadas, p=probabilidades)

def actualizar_feromonas(feromonas, caminos, longitudes, Q, evaporacion):
    """Actualiza la matriz de feromonas con base en los recorridos de las hormigas."""
    feromonas *= evaporacion
    for camino, longitud in zip(caminos, longitudes):
        for i in range(len(camino) - 1):
            feromonas[camino[i], camino[i + 1]] += Q / longitud
        feromonas[camino[-1], camino[0]] += Q / longitud  # Cierre del circuito sin añadir nodo extra

def colonia_de_hormigas(ciudades, inicio, n_hormigas, iteraciones, alpha, beta, evaporacion, Q):
    """Implementa el algoritmo de colonia de hormigas (ACO) con ciudad de inicio elegida."""
    lista_ciudades = list(ciudades.keys())
    coordenadas = np.array(list(ciudades.values()))
    n = len(lista_ciudades)
    feromonas = inicializar_feromonas(n)
    distancias = np.array([[calcular_distancia(coordenadas[i], coordenadas[j]) for j in range(n)] for i in range(n)])
    mejor_camino = None
    mejor_longitud = float('inf')
    inicio_idx = lista_ciudades.index(inicio)
    
    for _ in range(iteraciones):
        caminos = []
        longitudes = []
        
        for _ in range(n_hormigas):
            actual = inicio_idx
            camino = [actual]
            no_visitadas = list(range(n))
            no_visitadas.remove(actual)
            longitud = 0
            
            while no_visitadas:
                siguiente = elegir_siguiente_ciudad(feromonas, distancias, actual, no_visitadas, alpha, beta)
                longitud += distancias[actual, siguiente]
                camino.append(siguiente)
                no_visitadas.remove(siguiente)
                actual = siguiente
            longitud += distancias[camino[-1], inicio_idx]  # Volver al inicio correctamente
            caminos.append(camino)
            longitudes.append(longitud)
            
            if longitud < mejor_longitud:
                mejor_camino, mejor_longitud = camino, longitud
        
        actualizar_feromonas(feromonas, caminos, longitudes, Q, evaporacion)
    
    return mejor_camino, mejor_longitud

def graficar_recorrido(ciudades, mejor_camino):
    lista_ciudades = list(ciudades.keys())
    coordenadas = np.array([ciudades[lista_ciudades[i]] for i in mejor_camino] + [ciudades[lista_ciudades[mejor_camino[0]]]])  # Cierre del circuito
    siglas = {ciudad: ciudad[:3].upper() for ciudad in lista_ciudades}
    colores = plt.cm.rainbow(np.linspace(0, 1, len(mejor_camino)))
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    for i in range(len(mejor_camino)):
        ax.plot([coordenadas[i, 0], coordenadas[i + 1, 0]],  
                [coordenadas[i, 1], coordenadas[i + 1, 1]],  
                [coordenadas[i, 2], coordenadas[i + 1, 2]],  
                color=colores[i], marker='o', markersize=6)
        ax.text(coordenadas[i, 0], coordenadas[i, 1], coordenadas[i, 2], 
                f"{siglas[lista_ciudades[mejor_camino[i]]]}-{i+1}", fontsize=8)

    ax.set_xlabel("Latitud")
    ax.set_ylabel("Longitud")
    ax.set_zlabel("Altitud")
    plt.title("ACO aplicado al problema del vendedor viajero en ciudades Colombianas")
    plt.show()


# Ciudades de Colombia (normalizadas)
ciudades = {
    "BOGOTA": (4.6097, -74.0817, 2640), 
    "MEDELLIN": (6.2518, -75.5636, 1495), 
    "CALI": (3.4372, -76.5225, 1018),
    "BARRANQUILLA": (10.9639, -74.7964, 18), 
    "CARTAGENA": (10.391, -75.4794, 2), 
    "CUCUTA": (7.8939, -72.5078, 320),
    "BUCARAMANGA": (7.1254, -73.1198, 959), 
    "PEREIRA": (4.8133, -75.6961, 1411), 
    "SANTA MARTA": (11.2408, -74.199, 15),
    "IBAGUE": (4.4389, -75.2322, 1285), 
    "MANIZALES": (5.0689, -75.5174, 2160), 
    "PASTO": (1.2136, -77.2811, 2527)
}

# Parámetros de ACO
inicio = input("Ingrese la ciudad de inicio: ").upper().replace("Á", "A").replace("É", "E").replace("Í", "I").replace("Ó", "O").replace("Ú", "U")
if inicio not in ciudades:
    print(f"Ciudad '{inicio}' no encontrada. Se usará BOGOTA por defecto.")
    inicio = "BOGOTA"

n_hormigas = 20
iteraciones = 30
alpha = 1
beta = 2
evaporacion = 0.5
Q = 100

# Ejecutar ACO
mejor_camino, mejor_longitud = colonia_de_hormigas(ciudades, inicio, n_hormigas, iteraciones, alpha, beta, evaporacion, Q)
mejor_camino_nombres = [list(ciudades.keys())[i].capitalize() for i in mejor_camino]

# Mostrar resultados
graficar_recorrido(ciudades, mejor_camino)
print("Mejor ruta:", mejor_camino_nombres)
print("Longitud de la mejor ruta:", mejor_longitud)

