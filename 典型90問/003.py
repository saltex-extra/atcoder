from collections import deque

N = int(input())
G = [[] for _ in range(N)]
for i in range(N-1):
    A, B = map(int, input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)

def dfs(s):
    dist = [-1] * N
    dist[s] = 0

    stack = deque([s])
    while stack:
        v = stack.pop()
        for nv in G[v]:
            if dist[nv] == -1:
                stack.append(nv)
                dist[nv] = dist[v] + 1
    
    return dist

dist0 = dfs(0)
mv = max(enumerate(dist0), key=lambda x:x[1])[0]
distmv = dfs(mv)
print(max(distmv) + 1)
