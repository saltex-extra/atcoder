from collections import Counter

N = int(input())
s = [input() for _ in range(N)]
M = int(input())
t = [input() for _ in range(M)]
c_s = Counter(s)
c_t = Counter(t)
ans = 0

for k in c_s.keys():
    ans = max(ans, c_s[k] - c_t[k])

print(ans)
