L, R = map(int, input().split())
ans = 0
MOD = 10 ** 9 + 7

x = L
while x <= R:
    digits = len(str(x))
    if 10 ** digits - 1 < R:
        ans += (((x + (10 ** digits - 1)) * (10 ** digits - x) // 2) * digits) % MOD
        x = 10 ** digits
    else:
        ans += (((x + R) * (R - x + 1) // 2) * digits) % MOD
        break

ans %= MOD

print(ans)
