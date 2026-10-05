V,N = map(int,input().split())
coins = list(map(int,input().split()))
dp = [V+1]*(V+1)
dp[0] = 0
for i in range(1,V+1):
    for coin in coins:
        if coin <=i:
            dp[i] = min(dp[i], dp[i - coin] + 1)
if dp[V] == V + 1:
    print(-1)
else:
    print(dp[V])
