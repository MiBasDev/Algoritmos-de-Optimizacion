import random
import matplotlib.pyplot as plt

def get_stations():
    """
    Devuelve un diccionario donde las claves son estaciones y los valores son 
    conjuntos de estados cubiertos por cada estación.
    """
    stations = {
        'kone': {'ID', 'NV', 'UT'},
        'ktwo': {'WA', 'ID', 'MT'},
        'kthree': {'OR', 'NV', 'CA'},
        'kfour': {'NV', 'UT'},
        'kfive': {'CA', 'AZ'},
        'ksix': {'NM', 'TX', 'OK'},
        'kseven': {'OK', 'KS', 'CO'},
        'keight': {'KS', 'CO', 'NE'},
        'knine': {'NE', 'SD', 'WY'},
        'kten': {'ND', 'IA'},
        'keleven': {'MN', 'MO', 'AR'},
        'ktwelve': {'LA'},
        'kthirteen': {'MO', 'AR'}
    }
    return stations

def evaluate_combination(selected_stations, stations):
    """
    Evalúa cuántos estados cubre una combinación de estaciones.
    """
    covered_states = set()
    for station in selected_stations:
        covered_states.update(stations[station])
    return len(covered_states)

def hill_climbing(iterations=100):
    """
    Algoritmo de búsqueda por ascensión de colinas:
    - Selecciona aleatoriamente 10 estaciones.
    - Evalúa cuántos estados cubren.
    - Reemplaza la combinación si encuentra una mejor.
    - Guarda el número de estados NO cubiertos en cada iteración.
    """
    stations = get_stations()
    station_keys = list(stations.keys())
    total_states = len(set().union(*stations.values()))  # Número total de estados únicos

    best_combination = random.sample(station_keys, 10)
    best_coverage = evaluate_combination(best_combination, stations)
    best_uncovered = total_states - best_coverage  # Estados no cubiertos
    iteration = 0
    
    uncovered_states_list = []  # Lista para la gráfica

    with open("doc/resultado_hill_climbing.txt", "w", encoding="utf-8") as file:
        file.write("Búsqueda de la mejor combinación de estaciones (Ascensión de colinas)\n\n")

        for i in range(iterations):
            new_combination = random.sample(station_keys, 10)
            new_coverage = evaluate_combination(new_combination, stations)
            new_uncovered = total_states - new_coverage

            uncovered_states_list.append(new_uncovered)  # Guardar para la gráfica

            # Si la nueva combinación es mejor, la guardamos
            if new_coverage > best_coverage:
                best_combination = new_combination
                best_coverage = new_coverage
                best_uncovered = new_uncovered
                iteration = i+1
                
                file.write(f"Iteración {i+1}: Mejor combinación encontrada: {best_combination}\n")
                file.write(f"Total de estados cubiertos: {best_coverage}\n\n")

        # Escribimos el resultado final
        file.write("\nSolución óptima encontrada:\n")
        file.write(f"Estaciones seleccionadas: {best_combination}\n")
        file.write(f"Total de estados cubiertos: {best_coverage}\n")
        file.write(f"Estados no cubiertos: {best_uncovered}\n")

    return best_combination, best_coverage, uncovered_states_list, iteration

def plot_results(uncovered_states_list):
    """
    Genera y guarda una gráfica de barras mostrando la cantidad de estados NO cubiertos en cada iteración.
    """
    plt.figure(figsize=(12, 6))
    plt.bar(range(1, len(uncovered_states_list) + 1), uncovered_states_list, color='skyblue', edgecolor='black')
    plt.xlabel("Iteración")
    plt.ylabel("Estados no cubiertos")
    plt.title("Evolución de estados no cubiertos en cada iteración")
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Guardamos la imagen en la carpeta "doc"
    plt.savefig("doc/resultados_hill_climbing.png", dpi=300, bbox_inches="tight")
    print("📊 Gráfico guardado en doc/resultados.png")


if __name__ == "__main__":
    best_stations, coverage, uncovered_states_list, iteration = hill_climbing(100)
    print(f"Mejor combinación de estaciones [{len(best_stations)}] encontrada en la iteración [{iteration}]:", best_stations)
    print(f"Total de estados cubiertos: {coverage}")

    # Generamos y guardamos la gráfica
    plot_results(uncovered_states_list)
