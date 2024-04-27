def count_combinations(m, n):
    dp = [[0] * (m * n + 1) for _ in range(m + 1)]

    for j in range(1, min(n + 1, m * n + 1)):
        dp[1][j] = 1

    for i in range(2, m + 1):
        for j in range(1, m * n + 1):
            for k in range(1, min(n + 1, j)):
                dp[i][j] += dp[i - 1][j - k]

    total_combinations = sum(dp[m][m:(m * n) + 1])

    return total_combinations

def main():
    print("Enter the number of dice:", end=' ')
    m = int(input())

    print("Enter the number of faces on each die:", end=' ')
    n = int(input())

    result = count_combinations(m, n)
    print("Number of combinations:", result)

if __name__ == "__main__":
    while True:
        main()
