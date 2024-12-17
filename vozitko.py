def bfs_min_moves(grid, R, C, F, start_row, start_col, target_row, target_col):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


    queue = [[start_row, start_col, 0, 0]]


    visited = [[[False] * (F + 1) for _ in range(C)] for _ in range(R)]
    visited[start_row][start_col][0] = True

    while queue:
        row, col, steps, dangerous_count = queue.pop(0)


        if row == target_row and col == target_col:
            return steps


        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < R and 0 <= new_col < C:
                new_dangerous_count = dangerous_count + (1 if grid[new_row][new_col] == 1 else 0)


                if new_dangerous_count <= F and not visited[new_row][new_col][new_dangerous_count]:
                    visited[new_row][new_col][new_dangerous_count] = True
                    queue.append([new_row, new_col, steps + 1, new_dangerous_count])

    return -1



def main():
    R, C, F = map(int, input().split())
    start_row, start_col = map(int, input().split())
    target_row, target_col = map(int, input().split())

    grid = []
    for _ in range(R):
        grid.append(list(map(int, input().split())))


    start_row -= 1
    start_col -= 1
    target_row -= 1
    target_col -= 1

    result = bfs_min_moves(grid, R, C, F, start_row, start_col, target_row, target_col)
    print(result)


if __name__ == "__main__":
    main()
