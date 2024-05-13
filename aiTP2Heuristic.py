class Node:
    def __init__(self, state, parent, action, cost):
        self.state = state  # Current configuration of the robotic arm
        self.parent = parent  # Parent node in the search tree
        self.action = action  # Action taken to reach this state
        self.cost = cost  # Cost of reaching this state

def heuristic(state, goal):
    # Funcion heuristica
    # Esta función debe estimar el costo de alcanzar la meta desde el estado actual.
    # Se deben asignar valores más bajos a los estados más cercanos a la meta
    distance = abs(state[0] - goal[0])  # Heurística de distancia basada en el desplazamiento x
    return distance

def is_valid(state, limits):
    # Comprueba si el estado está dentro de los límites permitidos.
    x, _ = state
    return limits[0] <= x <= limits[1]

def a_star_search(start, goal, limits):
    open_set = []
    closed_set = set()
    start_node = Node(start, None, None, 0)
    open_set.append(start_node)

    while open_set:
        current = min(open_set, key=lambda node: node.cost + heuristic(node.state, goal))
        open_set.remove(current)
        closed_set.add(current.state)

        if current.state == goal:
            path = []
            while current:
                path.append(current.action)
                current = current.parent
            return path[::-1]  # Invierta el camino para obtener la secuencia real de acciones.

        for action in ["left", "right"]:
            new_state = (current.state[0] - 1 if action == "left" else current.state[0] + 1, current.state[1])
            if is_valid(new_state, limits) and new_state not in closed_set:
                new_cost = current.cost + 1  # Suponga un costo constante para cada acción.
                if new_state not in (node.state for node in open_set):
                    new_node = Node(new_state, current, action, new_cost)
                    open_set.append(new_node)
                else:
                    existing_node = next(node for node in open_set if node.state == new_state)
                    if new_cost < existing_node.cost:
                        existing_node.parent = current
                        existing_node.cost = new_cost

    return None  # No se encontró ningún camino

# Example usage
start = (0, 0)  # Posición inicial del brazo robótico (x, y)
goal = (5, 0)  # Posición de objetivo
limits = (-10, 10)  # Límites para el desplazamiento x

path = a_star_search(start, goal, limits)

if path:
    print("Camino encontrado:", path)
else:
    print("No se encontró ningún camino!!!")
