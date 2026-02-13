import sys
sys.setrecursionlimit(10**6)
        
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

visited = [False] * N
K = 0

def dfs(p):
    visited[p] = True
    for x in graph[p]:
        if visited[x] == False:
            dfs(x)

for i in range(N):
    if visited[i]:
        continue
    dfs(i)
    K += 1

ans = M - (N - K)

print(ans)
