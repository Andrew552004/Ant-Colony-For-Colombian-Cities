# Algoritmo de Colonia de Hormigas para el Problema del Viajante (TSP)

## Autores
- Andrés Felipe Vanegas Bogotá
- Sergio Andrés Sanabria Castillo
- Carlos Andrés Sinuco Murcia

## Descripción
Este programa implementa el algoritmo de **Optimización por Colonia de Hormigas (ACO)** para resolver el **Problema del Viajante (TSP)** en un conjunto de ciudades colombianas.

El usuario proporciona el nombre de la ciudad de inicio, y el algoritmo encuentra la mejor ruta para visitar todas las ciudades y regresar al punto de partida. Además, se genera una visualización 3D del recorrido óptimo.

## Requisitos
Para ejecutar este programa, se deben instalar las siguientes bibliotecas de Python:

```bash
pip install numpy matplotlib
```

## Ejecución
1. Ejecuta el programa en un entorno de Python.
2. Ingresa el nombre de la ciudad de inicio cuando se solicite.
3. El programa calculará la mejor ruta y mostrará una visualización 3D del recorrido.

### Parámetros de ACO
El algoritmo usa los siguientes parámetros:
- **n_hormigas**: Número de hormigas en cada iteración.
- **iteraciones**: Cantidad de iteraciones del algoritmo.
- **alpha**: Importancia de las feromonas en la toma de decisiones.
- **beta**: Influencia de la distancia en la toma de decisiones.
- **evaporacion**: Tasa de evaporación de las feromonas.
- **Q**: Cantidad de feromonas depositadas por cada hormiga.

Estos valores se pueden modificar directamente en el código.

## Ciudades Incluidas
El programa trabaja con las siguientes ciudades de Colombia, con sus respectivas coordenadas (latitud, longitud y altitud):

- Bogotá
- Medellín
- Cali
- Barranquilla
- Cartagena
- Cúcuta
- Bucaramanga
- Pereira
- Santa Marta
- Ibagué
- Manizales
- Pasto

## Salida del Programa
Después de la ejecución, el programa imprimirá:
- **Mejor ruta**: Lista ordenada de ciudades en el recorrido óptimo.
- **Longitud de la mejor ruta**: Distancia total del recorrido óptimo.
- **Visualización 3D**: Un gráfico en 3D mostrando la ruta óptima con conexiones entre ciudades.

## Ejemplo de Uso
```bash
Ingrese la ciudad de inicio: Bogotá
Mejor ruta: ['Bogotá', 'Ibagué', 'Pereira', 'Manizales', 'Medellín', 'Cali', ...]
Longitud de la mejor ruta: 1520.5 km
```

