"""
Authors:
Andrés Felipe Vanegas Bogotá
Sergio Andrés Sanabria Castillo
Carlos Andrés Sinuco Murcia

Description:
This program uses the Ant Colony Optimization (ACO) algorithm to solve the Traveling Salesman Problem (TSP) 
for a set of Colombian cities. The program takes the starting city as input from the user and then calculates 
the optimal route to visit all cities and return to the starting city.
"""

import numpy as np
import matplotlib.pyplot as plt

def calculate_distance(city1, city2):
    """Calculates the Euclidean distance in 3D between two cities, including altitude."""
    return np.linalg.norm(np.array(city1) - np.array(city2))

def initialize_pheromones(n):
    """Initializes the pheromone matrix with default values."""
    return np.ones((n, n))

def choose_next_city(pheromones, distances, current, unvisited, alpha, beta):
    """Chooses the next city based on the transition probability."""
    current_pheromones = pheromones[current, unvisited]
    current_distances = distances[current, unvisited]
    probabilities = (current_pheromones ** alpha) * ((1 / current_distances) ** beta)
    probabilities /= probabilities.sum()
    return np.random.choice(unvisited, p=probabilities)

def update_pheromones(pheromones, paths, lengths, Q, evaporation):
    """Updates the pheromone matrix based on the ants' paths."""
    pheromones *= evaporation
    for path, length in zip(paths, lengths):
        for i in range(len(path) - 1):
            pheromones[path[i], path[i + 1]] += Q / length
        pheromones[path[-1], path[0]] += Q / length  # Close the loop without adding an extra node

def ant_colony(ciudades, start, n_ants, iterations, alpha, beta, evaporation, Q):
    """Implements the Ant Colony Optimization (ACO) algorithm with a chosen starting city."""
    city_list = list(ciudades.keys())
    coordinates = np.array(list(ciudades.values()))
    n = len(city_list)
    pheromones = initialize_pheromones(n)
    distances = np.array([[calculate_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)])
    best_path = None
    best_length = float('inf')
    start_idx = city_list.index(start)
    
    for _ in range(iterations):
        paths = []
        lengths = []
        
        for _ in range(n_ants):
            current = start_idx
            path = [current]
            unvisited = list(range(n))
            unvisited.remove(current)
            length = 0
            
            while unvisited:
                next_city = choose_next_city(pheromones, distances, current, unvisited, alpha, beta)
                length += distances[current, next_city]
                path.append(next_city)
                unvisited.remove(next_city)
                current = next_city
            length += distances[path[-1], start_idx]  # Return to the start correctly
            paths.append(path)
            lengths.append(length)
            
            if length < best_length:
                best_path, best_length = path, length
        
        update_pheromones(pheromones, paths, lengths, Q, evaporation)
    
    return best_path, best_length

def plot_route(ciudades, best_path):
    city_list = list(ciudades.keys())
    coordinates = np.array([ciudades[city_list[i]] for i in best_path] + [ciudades[city_list[best_path[0]]]])  # Close the loop
    abbreviations = {city: city[:3].upper() for city in city_list}
    colors = plt.cm.rainbow(np.linspace(0, 1, len(best_path)))
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    for i in range(len(best_path)):
        ax.plot([coordinates[i, 0], coordinates[i + 1, 0]],  
                [coordinates[i, 1], coordinates[i + 1, 1]],  
                [coordinates[i, 2], coordinates[i + 1, 2]],  
                color=colors[i], marker='o', markersize=6)
        ax.text(coordinates[i, 0], coordinates[i, 1], coordinates[i, 2], 
                f"{abbreviations[city_list[best_path[i]]]}-{i+1}", fontsize=8)

    ax.set_xlabel("Latitude")
    ax.set_ylabel("Longitude")
    ax.set_zlabel("Altitude")
    plt.title("ACO Applied to the Traveling Salesman Problem for Colombian Cities")
    plt.show()


# Colombian cities (normalized)
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

# ACO parameters
start = input("Enter the starting city: ").upper().replace("Á", "A").replace("É", "E").replace("Í", "I").replace("Ó", "O").replace("Ú", "U")
if start not in ciudades:
    print(f"City '{start}' not found. Using BOGOTA as default.")
    start = "BOGOTA"

n_ants = 20
iterations = 30
alpha = 1
beta = 2
evaporation = 0.5
Q = 100

# Run ACO
best_path, best_length = ant_colony(ciudades, start, n_ants, iterations, alpha, beta, evaporation, Q)
best_path_names = [list(ciudades.keys())[i].capitalize() for i in best_path]

# Display results
plot_route(ciudades, best_path)
print("Best route:", best_path_names)
print("Length of the best route:", best_length)