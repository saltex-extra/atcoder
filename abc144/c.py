N = int(input())
ans = N - 1

for i in range(2, int(N ** 0.5) + 1):
    if N % i == 0:
        a = i
        b = N // i
        ans = min(ans, a + b - 2)

print(ans)
