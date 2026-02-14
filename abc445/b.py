N = int(input())
S = [input() for _ in range(N)]
l_max = max([len(s) for s in S])

for s in S:
    ans = '.' * ((l_max - len(s)) // 2) + s +  '.' * ((l_max - len(s)) // 2)
    print(ans)
