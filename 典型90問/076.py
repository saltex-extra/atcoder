N = int(input())
A = list(map(int, input().split()))

sumA = sum(A)
prefix_sum = [0] * (N + 2)
ans = 'No'

if sumA % 10 == 0:
    for i in range(N + 1):
        prefix_sum[i + 1] = A[i % N] + prefix_sum[i]
    
    prefix_sum = set(prefix_sum)

    for x in prefix_sum:
        if (x + sumA // 10) % sumA in prefix_sum:
            ans = 'Yes'
            break

print(ans)
