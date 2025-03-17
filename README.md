# Algoritmos de Optimización

Este repositorio contiene dos enfoques distintos para **seleccionar un conjunto óptimo de estaciones** que cubran la mayor cantidad de estados en EE.UU., que tendrá que utilizar **Beyoncé** para promocionar su disco:

1. **Algoritmo voraz (greedy)** → Selecciona siempre la mejor opción disponible.  
2. **Algoritmo aleatorio** → Selecciona estaciones al azar, explorando diferentes posibilidades.

Ambos enfoques se comparan para evaluar su rendimiento y eficiencia. 📊  

---

## Índice
1. [Instalación](#instalación)
2. [Uso](#uso)
   - [Algoritmo Voraz](#ejecutar-algoritmo-voraz)
   - [Algoritmo Aleatorio](#ejecutar-algoritmo-aleatorio)
3. [Explicación del Algoritmo](#explicación-del-algoritmo)
   - [Qué hace el programa](#qué-hace-el-programa)
   - [Algoritmo Voraz](#algoritmo-voraz-greedy)
   - [Algoritmo Aleatorio](#algoritmo-aleatorio)

---

## Instalación
Para obtener este repositorio desde **GitHub**, usa el siguiente comando en la terminal:

```bash
cd Algoritmos_Optimizacion
```

Ahora, navega dentro de la carpeta del proyecto:

```bash
cd Algoritmos_Optimizacion
```

---

## Uso
### Ejecutar Algoritmo Voraz
Para lanzar el algoritmo voraz (greedy), ejecuta el siguiente comando:

```bash
python greedy_algorithm.py
```
El resultado se guardará en **doc/resultado_voraz.txt**.


### Ejecutar Algoritmo Aleatorio
Para lanzar el algoritmo aleatorio, ejecuta:

```bash
python random_algorithm.py
```

El resultado se guardará en **doc/resultado_aleatorio.txt**.

---

## Explicación del Algoritmo
### Qué hace el programa
Este programa **selecciona estaciones** de una lista predefinida para cubrir la mayor cantidad de estados posibles. Se utilizan dos enfoques:

1. **Enfoque Voraz (Greedy):** Siempre elige la estación que cubre más estados no cubiertos.
2. **Enfoque Aleatorio:** Elige estaciones al azar para ver si llega a una solución diferente.

---

### Algoritmo Voraz (Greedy)
**Lógica:**
1. Se inicializa un conjunto vacío de **estaciones seleccionadas**.
2. Se busca la estación que cubra la mayor cantidad de **estados no cubiertos**.
3. Se añade esa estación y se actualiza la lista de estados cubiertos.
4. Se repite hasta cubrir todos los estados.

```py
def max_station(remaining_stations, covered_states):
    """
    Encuentra la estación que cubre la mayor cantidad de estados no cubiertos.
    """
    best_station = None
    max_uncovered = -1
    
    for station in remaining_stations:
        uncovered = len(remaining_stations[station] - covered_states)
        if uncovered > max_uncovered:
            max_uncovered = uncovered
            best_station = station
    
    return best_station
```

---

### Algoritmo Aleatorio
**Lógica:**
1. Se inicializa un conjunto vacío de **estaciones seleccionadas**.
2. En cada iteración, se elige **una estación aleatoria** en lugar de la mejor opción.
3. Se añade esa estación y se actualiza la lista de estados cubiertos.
4. Se repite hasta cubrir todos los estados.

```py
import random

def random_station_selection():
    """
    Encuentra una combinación aleatoria de estaciones para cubrir el mayor número de estados.
    """
    stations = get_stations()
    selected_stations = []
    covered_states = set()
    remaining_stations = stations.copy()

    while remaining_stations:
        best_station = random.choice(list(remaining_stations.keys()))
        uncovered_states = remaining_stations[best_station] - covered_states
        
        if not uncovered_states:
            del remaining_stations[best_station]
            continue
        
        selected_stations.append(best_station)
        covered_states.update(remaining_stations[best_station])
        del remaining_stations[best_station]
    
    return selected_stations
```