N, K = map(int, input().split())
MOD = 10 ** 9 + 7

def Power(x, n, m):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return (x * Power(x, n-1, m)) % m
    else:
        a = Power(x, n // 2, m)
        return (a * a) % m

if N == 1:
    ans = K
elif N == 2:
    ans = K * (K - 1)
else:
    ans = K * (K - 1) * Power(K - 2, N - 2, MOD) 

print(ans % MOD)
