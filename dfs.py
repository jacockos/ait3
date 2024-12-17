
GRID_SIZE = 10
START = (0, 0)
GOAL = (GRID_SIZE - 1, GRID_SIZE - 1)


grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

grid[5][5] = 1
grid[6][5] = 1
grid[7][5] = 1
grid[5][6] = 1
grid[5][7] = 1



def print_grid():
    for row in range(GRID_SIZE):
        line = ""
        for col in range(GRID_SIZE):
            if (row, col) == START:
                line += "S "
            elif (row, col) == GOAL:
                line += "G "
            elif grid[row][col] == 1:
                line += "# "
            else:
                line += ". "
        print(line)
    print()



def dfs(start, goal):
    stack = [start]
    came_from = {start: None}

    while stack:
        current = stack.pop()
        if current == goal:
            break
        for neighbor in get_neighbors(current):
            if neighbor not in came_from and grid[neighbor[1]][neighbor[0]] != 1:
                stack.append(neighbor)
                came_from[neighbor] = current
    return reconstruct_path(came_from, start, goal)



def get_neighbors(pos):
    x, y = pos
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
            neighbors.append((nx, ny))
    return neighbors



def reconstruct_path(came_from, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path



def main():
    print("Počáteční mřížka:")
    print_grid()


    path = dfs(START, GOAL)


    print("Nalezená cesta:")
    if path:
        for (x, y) in path:
            grid[y][x] = 2
        print_grid()
    else:
        print("Cesta nebyla nalezena.")


if __name__ == "__main__":
    main()
