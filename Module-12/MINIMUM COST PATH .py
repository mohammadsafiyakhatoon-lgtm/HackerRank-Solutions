N, M = map(int, input().split())
grid = []
for i in range(N):
    grid.append(list(map(int, input().split())))
dp = [[0] * N for _ in range(N)]
dp[0][0] = grid[0][0]
for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            continue
        best = 10**18
        if i > 0:
            best = min(best, dp[i - 1][j])
        if j > 0:
            best = min(best, dp[i][j - 1])
        if i > 0 and j > 0:
            best = min(best, dp[i - 1][j - 1])
        dp[i][j] = grid[i][j] + best
print(dp[N-1][N-1])
