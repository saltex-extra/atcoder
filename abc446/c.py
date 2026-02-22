T = int(input())

for _ in range(T):
    N, D = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    j = 0

    for i in range(N):
        while B[i] > 0:
            if A[j] >= B[i]:
                A[j] -= B[i]
                B[i] = 0
                break
            else:
                B[i] -= A[j]
                A[j] = 0
                j += 1
        if i - D >= 0:
            A[i - D] = 0
    
    print(sum(A))
