# README: Ant Colony Optimization for the Traveling Salesman Problem (TSP)

## Description
This program implements the **Ant Colony Optimization (ACO)** algorithm to solve the **Traveling Salesman Problem (TSP)** for a set of Colombian cities. The TSP is a classic optimization problem where the goal is to find the shortest possible route that visits each city exactly once and returns to the starting city. The program takes a starting city as input from the user and computes the optimal route using ACO.

The program also visualizes the best route in a 3D plot, showing the latitude, longitude, and altitude of the cities.

---

## Features
- **Ant Colony Optimization (ACO):** A metaheuristic algorithm inspired by the behavior of ants searching for food.
- **3D Distance Calculation:** Computes Euclidean distances between cities, including altitude.
- **Interactive Input:** The user can specify the starting city.
- **Visualization:** Displays the best route in a 3D plot using `matplotlib`.
- **Customizable Parameters:** Allows tuning of ACO parameters such as the number of ants, iterations, and pheromone evaporation rate.

---

## Requirements
To run this program, you need the following Python libraries:
- `numpy`
- `matplotlib`

You can install the required libraries using pip:
```bash
pip install numpy matplotlib
```

---

## How to Use
1. **Run the Program:**
   Execute the Python script in your terminal or IDE:
   ```bash
   python aco_tsp.py
   ```

2. **Enter the Starting City:**
   When prompted, enter the name of the starting city (e.g., `Bogota`, `Medellin`, `Cali`). The program will automatically handle case sensitivity and special characters.

3. **View the Results:**
   - The program will display the **best route** and its **total length** in the console.
   - A 3D plot will open, showing the route connecting the cities.

---

## Code Structure
- **`calculate_distance(city1, city2)`:** Computes the Euclidean distance between two cities in 3D space.
- **`initialize_pheromones(n)`:** Initializes the pheromone matrix with default values.
- **`choose_next_city(pheromones, distances, current, unvisited, alpha, beta)`:** Selects the next city based on pheromone levels and distances.
- **`update_pheromones(pheromones, paths, lengths, Q, evaporation)`:** Updates the pheromone matrix based on the ants' paths.
- **`ant_colony(ciudades, start, n_ants, iterations, alpha, beta, evaporation, Q)`:** Implements the ACO algorithm to find the best route.
- **`plot_route(ciudades, best_path)`:** Visualizes the best route in a 3D plot.

---

## Parameters
The ACO algorithm can be customized using the following parameters:
- **`n_ants`:** Number of ants (default: `20`).
- **`iterations`:** Number of iterations (default: `30`).
- **`alpha`:** Controls the influence of pheromones (default: `1`).
- **`beta`:** Controls the influence of distances (default: `2`).
- **`evaporation`:** Pheromone evaporation rate (default: `0.5`).
- **`Q`:** Pheromone deposit factor (default: `100`).

---

## Example Output
### Console Output:
```
Enter the starting city: Medellin
Best route: ['Medellin', 'Manizales', 'Pereira', 'Ibague', 'Bogota', 'Bucaramanga', 'Cucuta', 'Santa Marta', 'Barranquilla', 'Cartagena', 'Cali', 'Pasto']
Length of the best route: 1234.56
```

### 3D Plot:
- A 3D graph showing the route connecting the cities, with latitude, longitude, and altitude axes.

---

## Dataset
The program uses a predefined dataset of Colombian cities with their coordinates (latitude, longitude, and altitude). The cities included are:
- Bogota
- Medellin
- Cali
- Barranquilla
- Cartagena
- Cucuta
- Bucaramanga
- Pereira
- Santa Marta
- Ibague
- Manizales
- Pasto

---

## Authors
- Andrés Felipe Vanegas Bogotá
- Sergio Andrés Sanabria Castillo
- Carlos Andrés Sinuco Murcia

---

## License
This project is open-source and available under the MIT License. Feel free to modify and distribute it as needed.

---

## Acknowledgments
- The ACO algorithm is inspired by the behavior of real ants and their ability to find optimal paths.
- The dataset of Colombian cities is normalized for demonstration purposes.

---

For any questions or suggestions, please contact the authors. Enjoy optimizing routes with ACO! 🐜🌍
