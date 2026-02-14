N = int(input())
A = list(map(int, input().split()))
ans = [-1] * N

for i in range(N):
    position = i
    visited = {i}

    while ans[i] == -1:
        if A[position] - 1 == position:
            for v in visited:
                ans[v] = position + 1
        elif A[position] - 1 in visited:
            ans[i] = A[(10 ** 100) % len(visited)]
        else:
            position = A[position] - 1
            visited.add(position)

print(*ans)
