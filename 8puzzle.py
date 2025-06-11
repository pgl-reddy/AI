import heapq
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
def manhattan_distance(state):
    distance = 0
    for r in range(3):
        for c in range(3):
            value = state[r][c]
            if value != 0:  # Don't calculate for the empty tile
                goal_r, goal_c = divmod(value - 1, 3)
                distance += abs(r - goal_r) + abs(c - goal_c)
    return distance
def a_star(start_state):
    pq = []
    visited = set()
    initial_state = tuple(tuple(row) for row in start_state)
    heapq.heappush(pq, (0 + manhattan_distance(start_state), 0, initial_state, []))  # (f, g, state, path)
    while pq:
        f, g, state, path = heapq.heappop(pq)
        if state == tuple(tuple(row) for row in goal_state):
            return path
        visited.add(state)
        empty_pos = None
        for r in range(3):
            for c in range(3):
                if state[r][c] == 0:
                    empty_pos = (r, c)
                    break
            if empty_pos:
                break
        r, c = empty_pos  # Unpack row and column
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_state = [list(row) for row in state]
                new_state[r][c], new_state[nr][nc] = new_state[nr][nc], new_state[r][c]
                new_state_tuple = tuple(tuple(row) for row in new_state)
                
                if new_state_tuple not in visited:
                    new_g = g + 1
                    f_new = new_g + manhattan_distance(new_state)
                    heapq.heappush(pq, (f_new, new_g, new_state_tuple, path + [new_state_tuple]))
    
    return None  # If no solution is found
def print_state(state):
    for row in state:
        print(row,end=' ')
    print()
start_state = [[7, 2, 4],
               [5, 0, 6],
               [8, 3, 1]]
solution = a_star(start_state)
if solution:
    print("Solution path:")
    for step in solution:
        print_state(step)
else:
    print("No solution found.")
