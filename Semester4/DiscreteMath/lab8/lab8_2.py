def is_valid_move(x, y, n, m, visited):
    return 0 <= x < n and 0 <= y < m and not visited[x][y]

def count_tour_paths(n, m, start_x, start_y):
    visited = [[False] * m for _ in range(n)]
    visited[start_x][start_y] = True
    count = [0]
    closed_count = [0]

    def dfs(x, y, depth):
        if depth == n * m:
            count[0] += 1
            dx = [1, 2, 2, 1, -1, -2, -2, -1]
            dy = [-2, -1, 1, 2, 2, 1, -1, -2]
            for i in range(8):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if new_x == start_x and new_y == start_y:
                    closed_count[0] += 1
                    break
        else:
            dx = [1, 2, 2, 1, -1, -2, -2, -1]
            dy = [-2, -1, 1, 2, 2, 1, -1, -2]
            for i in range(8):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if is_valid_move(new_x, new_y, n, m, visited):
                    visited[new_x][new_y] = True
                    dfs(new_x, new_y, depth + 1)
                    visited[new_x][new_y] = False

    dfs(start_x, start_y, 1)

    return count[0], closed_count[0]


def main():
    while True:
        n = int(input("Enter the number of rows: "))
        m = int(input("Enter the number of columns: "))
        start_x = int(input("Enter the starting row: "))
        start_y = int(input("Enter the starting column: "))
        total_paths, closed_paths = count_tour_paths(n, m, start_x, start_y)
        print("Total paths:", total_paths)
        print("Closed paths:", closed_paths)


if __name__ == "__main__":
    main()
