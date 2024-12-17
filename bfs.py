
GRID_SIZE = 10
START = (0, 0)
GOAL = (GRID_SIZE - 1, GRID_SIZE - 1)


grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]


grid[5][5] = 1
grid[6][5] = 1
grid[7][5] = 1
grid[5][6] = 1
grid[5][7] = 1
grid[3][4] = 1
grid[3][5] = 1
grid[2][5] = 1
grid[8][3] = 1
grid[8][4] = 1
grid[7][8] = 1
grid[1][2] = 1
grid[2][2] = 1
grid[3][2] = 1
grid[4][2] = 1
grid[4][3] = 1
grid[1][6] = 1
grid[1][7] = 1
grid[4][8] = 1
grid[3][7] = 1
grid[6][8] = 1
grid[7][2] = 1



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
            elif grid[row][col] == 2:
                line += "\033[92m✓\033[0m "
            else:
                line += "\033[92m✓\033[0m "
        print(line)
    print()



def bfs(start, goal):
    queue = [start]
    came_from = {start: None}

    while queue:
        current = queue.pop(0)
        if current == goal:
            break
        for neighbor in get_neighbors(current):
            if neighbor not in came_from and grid[neighbor[1]][neighbor[0]] != 1:
                queue.append(neighbor)
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


    path = bfs(START, GOAL)


    print("Nalezená cesta:")
    if path:
        for (x, y) in path:
            grid[y][x] = 2 
        print_grid()
    else:
        print("Cesta nebyla nalezena.")


if __name__ == "__main__":
    main()
