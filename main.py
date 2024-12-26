from AStarVisualiser import AStarVisualiser


def main():
    graph = {
        'A': [('B', 2), ('C', 4), ('D', 7), ('E', 3)],
        'B': [('A', 2), ('E', 3), ('F', 5), ('C', 1)],
        'C': [('A', 4), ('B', 1), ('F', 1), ('G', 3), ('D', 2)],
        'D': [('A', 7), ('G', 2), ('H', 6)],
        'E': [('A', 3), ('B', 3), ('I', 4), ('J', 6)],
        'F': [('B', 5), ('C', 1), ('J', 2), ('G', 4)],
        'G': [('C', 3), ('D', 2), ('F', 4), ('K', 4), ('H', 3)],
        'H': [('D', 6), ('G', 3), ('K', 3), ('L', 5)],
        'I': [('E', 4)],
        'J': [('E', 6), ('F', 2), ('I', 2), ('N', 3)],
        'K': [('G', 4), ('H', 3), ('N', 2), ('L', 1)],
        'L': [('H', 5), ('K', 1), ('O', 7), ('P', 4)],
        'M': [('I', 6), ('P', 8), ('N', 5)],
        'N': [('J', 3), ('K', 2), ('M', 5), ('P', 4)],
        'O': [('L', 7), ('P', 3)],
        'P': [('M', 8), ('N', 4), ('O', 3), ('L', 4)]
    }

    # Евристична функция (например Евклидово разстояние)
    heuristic = {
        'A': 10, 'B': 8, 'C': 6, 'D': 7,
        'E': 7, 'F': 5, 'G': 4, 'H': 6,
        'I': 6, 'J': 3, 'K': 2, 'L': 5,
        'M': 6, 'N': 2, 'O': 3, 'P': 0
    }

    start_node = 'C'
    target_node = 'P'
    animation_delay = 1     #секунди

    visualiser = AStarVisualiser()
    path, total_cost = visualiser.visualise_a_star(graph, start_node, target_node, heuristic, animation_delay=animation_delay)

    if path:
        print("Най-кратък път:", " --> ".join(path))
        print(f"Обща дължина на пътя: {total_cost}")
    else:
        print("Няма намерен път до целта.")


if __name__ == "__main__":
    main()
