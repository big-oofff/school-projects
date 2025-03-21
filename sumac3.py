from collections import deque


def move_X(state):
    #("A", "B", "C", "D", "E")
    #return (C B D A E)
    state = list(state)
    state[0], state[2], state[3] = state[2], state[3], state[0]
    return tuple(state)

def move_Y(state):
    #("A", "B", "C", "D", "E")
    #return (A D C E B)
    state = list(state)
    state[1], state[3], state[4] = state[3], state[4], state[1]
    return tuple(state)


def find_solution(start, target):
    queue = deque([(start, [])])  
    visited = set() 
    while queue:
        current_state, moves = queue.popleft()
        if current_state == target:
            return moves
        if current_state not in visited:
            visited.add(current_state)
            queue.append((move_X(current_state), moves + ["X"]))
            queue.append((move_Y(current_state), moves + ["Y"]))

    return None 


start_config = ("A", "B", "C", "D", "E")  
target_config = ("D", "A", "C", "B", "E")  


solution = find_solution(start_config, target_config)


if solution:
    print("Sequence of moves to reach the target:", solution)
else:
    print("No solution found.")
