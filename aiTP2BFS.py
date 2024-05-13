class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state  # Estado actual del brazo robótico
        self.parent = parent  # Nodo principal en el árbol de búsqueda
        self.action = action  # Acción tomada para llegar a este estado (izquierda/derecha)
        self.cost = cost  # Costo total para llegar a este estado.

def uniform_search(initial_state, goal_state):
    """
    Realiza una búsqueda uniforme utilizando BFS para el problema del brazo robótico.

    Args:
        initial_state: El estado inicial del brazo robótico.
        goal_state: El estado objetivo deseado del brazo robótico.

    Devuelve:
        Una lista de acciones que representan la ruta de la solución, o Ninguna si no se encuentra ninguna solución.
    """

    if initial_state == goal_state:
        return []  # Solución hallada en el estado inicial.

    frontier = [Node(initial_state)]
    explored = set()

    while frontier:
        node = frontier.pop(0)  # FIFO (BFS)
        explored.add(node.state)

        # Generar nodos secundarios para movimientos hacia la izquierda y hacia la derecha.
        for action in ['left', 'right']:
            new_state = perform_action(node.state, action)

            if new_state is None:
                continue  # Acción no válida (por ejemplo, el brazo ya está en el borde)

            if new_state in explored:
                continue  # Estado ya explorado

            child = Node(new_state, parent=node, action=action, cost=node.cost + 1)
            frontier.append(child)

            if new_state == goal_state:
                # Solución encontrada, retroceda para obtener el camino.
                path = []
                while child:
                    path.append(child.action)
                    child = child.parent
                return path[::-1]  # Invertir para el orden correcto (objetivo para comenzar)

    return None  # No se encuentra solucion

def perform_action(state, action):
    """
    Simula el movimiento del brazo robótico en función de la acción dada.
    Args:
        state: El estado actual del brazo robótico.
        action: La acción a realizar ('izquierda' o 'derecha').

    Devuelve:
        El nuevo estado del brazo robótico después de la acción, o Ninguno si no es válido.
    """

    # considerando límites, limitaciones, etc.
    if action == 'left':
        # Actualizar el estado para reflejar el movimiento hacia la izquierda (dentro del rango válido)
        new_state = (state[0] - 1, state[1])  # Ajuste según la representación de su estado
    elif action == 'right':
        # Actualizar el estado para reflejar el movimiento hacia la derecha (dentro del rango válido)
        new_state = (state[0] + 1, state[1])  # Ajuste según la representación de su estado
    else:
        return None  # Acción inválida

    # Compruebe si el nuevo estado es válido (por ejemplo, al alcance de la mano)
    if is_valid_state(new_state):
        return new_state
    else:
        return None  # Estado no válido (por ejemplo, brazo fuera de rango)

def is_valid_state(state):
    """
    Comprueba si el estado dado es válido para el problema del brazo robótico.

    Args:
        state: El estado a comprobar.

    Devuelve:
        Verdadero si el estado es válido; Falso en caso contrario.
    """
    return 0 <= state[0] <= 10 and -10 <= state[1] <= 0     # Límites para el desplazamiento x

# reemplazar con la representación de estado real y lógica de validación)
initial_state = (0, 0)  # Posición inicial (x, y)
goal_state = (3, 0)  # Posición de meta deseada (x, y)

solution = uniform_search(initial_state, goal_state)

if solution:
    print("Solución encontrada:")
    for action in solution:
        print(action, end=" -> ")
    print("Solucionado")
