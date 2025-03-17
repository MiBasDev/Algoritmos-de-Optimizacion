import random

def get_stations():
    """
    Devuelve un diccionario donde las claves son estaciones (kone, ktwo, etc.)
    y los valores son conjuntos de estados cubiertos por cada estación.
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

def get_uncovered_states(station, remaining_stations, covered_states):
    """
    Devuelve la cantidad de estados no cubiertos por la estación dada.
    """
    return len(remaining_stations[station] - covered_states)

def random_station_selection():
    """
    Encuentra una combinación aleatoria de estaciones para cubrir el mayor número de estados.
    """
    stations = get_stations()
    selected_stations = []
    covered_states = set()
    remaining_stations = stations.copy()

    count = 1
    with open("doc/resultado_aleatorio.txt", "w", encoding="utf-8") as file:
        while remaining_stations:
            # Seleccionamos una estación aleatoria en vez de la mejor
            best_station = random.choice(list(remaining_stations.keys()))
            uncovered_states = remaining_stations[best_station] - covered_states

            # Si la estación no aporta nuevos estados, descartamos
            if not uncovered_states:
                del remaining_stations[best_station]
                continue

            # Agregamos la estación seleccionada
            selected_stations.append(best_station)
            covered_states.update(remaining_stations[best_station])
            del remaining_stations[best_station]

            # Guardamos en el log
            file.write(f"Iteración {count}:\n")
            file.write(f"- Estación seleccionada: {best_station}\n")
            file.write(f"- Estados cubiertos en esta iteración [{len(uncovered_states)}]: {uncovered_states}\n")
            file.write(f"- Total de estados cubiertos [{len(covered_states)}]: {covered_states}\n")
            file.write(f"- Estaciones restantes [{len(remaining_stations)}]: {list(remaining_stations.keys())}\n\n")
            
            count += 1
        
        # Resultado final
        file.write("Solución:\n")
        file.write(f"** Estaciones seleccionadas [{len(selected_stations)}]: {selected_stations} **\n")
        file.write(f"** Total de estados cubiertos [{len(covered_states)}]: {covered_states} **\n")

    return selected_stations

if __name__ == "__main__":
    combination = random_station_selection()
    print(f"Las estaciones que debe elegir Beyoncé son [{len(combination)}]:", combination)
