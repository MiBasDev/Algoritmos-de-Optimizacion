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

def max_station(remaining_stations, covered_states):
    """
    Encuentra la estación que cubre la mayor cantidad de estados no cubiertos.
    """
    best_station = None
    max_uncovered = -1
    
    for station in remaining_stations:
        uncovered = get_uncovered_states(station, remaining_stations, covered_states)
        if uncovered > max_uncovered:
            max_uncovered = uncovered
            best_station = station
    
    return best_station

def best_combination():
    """
    Encuentra la mejor combinación de estaciones para cubrir el mayor número de estados.
    Muestra el progreso en cada iteración e imprime la solución final.
    """
    # Obtenemos el diccionario de estaciones y sus estados
    stations = get_stations()  
    # Lista de estaciones que vamos seleccionando
    selected_stations = []  
    # Conjunto de estados cubiertos
    covered_states = set()  
    # Hacemos una copia para las estaciones disponibles
    remaining_stations = stations.copy()  
    
    count = 1
    with open("doc/resultado_voraz.txt", "w", encoding="utf-8") as file:
        while remaining_stations:
            # Encontramos la estación que cubra la mayor cantidad de estados aún no cubiertos
            best_station = max_station(remaining_stations, covered_states)
            uncovered_states = remaining_stations[best_station] - covered_states
            
            # Si la estación no aporta nuevos estados, terminamos
            if not uncovered_states:
                break
            
            # Agregamos la mejor estación a la solución
            selected_stations.append(best_station)
            covered_states.update(remaining_stations[best_station])
            del remaining_stations[best_station]
            
            # Imprimimos información sobre el progreso
            file.write(f"Iteración {count}:\n")
            file.write(f"- Mejor estación seleccionada: {best_station}\n")
            file.write(f"- Estados cubiertos en esta iteración [{len(uncovered_states)}]: {uncovered_states}\n")
            file.write(f"- Total de estados cubiertos hasta ahora [{len(covered_states)}]: {covered_states}\n")
            file.write(f"- Estaciones restantes [{len(remaining_stations)}]: {list(remaining_stations.keys())}\n\n")
            
            count += 1
        
        # Imprimimos la solución final
        file.write("Solución:\n")
        file.write(f"** Estaciones seleccionadas [{len(selected_stations)}]: {selected_stations} **\n")
        file.write(f"** Total de estados cubiertos [{len(covered_states)}]: {covered_states} **\n")
    
    return selected_stations


if __name__ == "__main__":
    combination = best_combination()
    print(f"Las estaciones que debe elegir Beyoncé son [{len(combination)}]:", combination)

