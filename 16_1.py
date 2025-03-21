import heapq

def print_grid(grid):
    """Print the grid for visualization."""
    print()
    for row in grid:
        print(''.join(row))

def get_grid():
    """Read the input grid and find start (S) and end (E) positions."""
    grid = []
    start, end = None, None

    with open("input/16.txt") as file:
        row_index = 0
        for line in file.readlines():
            row = []
            for column_index, char in enumerate(line.strip()):
                if char == 'S':
                    start = (row_index, column_index)
                elif char == 'E':
                    end = (row_index, column_index)
                row.append(char)
            grid.append(row)
            row_index += 1

    return grid, start, end

def dijkstra(grid, start, end):
    """Use Dijkstra's algorithm to find the best paths and mark tiles part of best paths."""
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # North, East, South, West

    pq = []
    heapq.heappush(pq, (0, start[0], start[1], 1, [start]))  # (score, x, y, direction, path)

    # Visited states to prevent reprocessing with worse scores
    visited = {}

    best_paths = []
    best_score = float('inf')

    while pq:
        score, x, y, direction, path = heapq.heappop(pq)

        # If we reach the end, check if this path is the best path
        if (x, y) == end:
            if score < best_score:
                best_score = score
                best_paths = [path + [(x, y)]]  # Start a new set of best paths
            elif score == best_score:
                best_paths.append(path + [(x, y)])

        # Mark the current state as visited if the score is better or equal
        if (x, y, direction) not in visited or visited[(x, y, direction)] > score:
            visited[(x, y, direction)] = score
        else:
            continue

        # Try moving forward (1 step in the current direction)
        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy
        if grid[ny][nx] != "#":  # If the next tile is not a wall
            heapq.heappush(pq, (score + 1, nx, ny, direction, path + [(nx, ny)]))

        # Try turning (clockwise and counterclockwise)
        for new_dir in [(direction + 1) % 4, (direction - 1) % 4]:
            heapq.heappush(pq, (score + 1000, x, y, new_dir, path))

    # Collect all unique tiles from the best paths
    best_path_tiles = set()
    for path in best_paths:
        best_path_tiles.update(path)

    # Count the unique tiles and mark them on the grid
    for (x, y) in best_path_tiles:
        if grid[y][x] not in ['S', 'E']:  # Don't overwrite start or end
            grid[y][x] = 'O'

    # Print the updated grid with 'O' marking the best path tiles
    print_grid(grid)

    return best_score, len(best_path_tiles)


if __name__ == '__main__':
    grid, start, end = get_grid()
    best_score, best_path_tile_count = dijkstra(grid, start, end)
    print(f"Best Score: {best_score}")
    print(f"Total tiles in best paths: {best_path_tile_count}")