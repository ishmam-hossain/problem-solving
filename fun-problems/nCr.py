def nCr(n, r):
    if n == r:
        return 1
    if r == 1:
        return n

    if dp[n][r] == -1:
        dp[n][r] = nCr(n, r-1) + nCr(n-1, r-1)

    return dp[n][r]


dp = [[-1]*50]*50
print(nCr(45, 40))
