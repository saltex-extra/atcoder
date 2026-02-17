N = int(input())
S = input()
ans = N * (N - 1) // 2
l = 0
r = 0
cnt = 0

for i in range(N - 1):
    if S[i] == S[i+1]:
        r += 1
    else:
        ans -= (r - l + 1) * (r - l) // 2
        l = i + 1
        r = i + 1
        cnt += 1
    if i == N - 2 and cnt > 0 and l < r:
        ans -= (r - l + 1) * (r - l) // 2

if cnt == 0:
    ans = 0

print(ans)
