N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = [A[i] - A[i+1] for i in range(N-1)] + [0]

ans = sum(abs(b) for b in B)

for _ in range(Q):
    L, R, V = map(int, input().split())
    ans_b = abs(B[L-2]) + abs(B[R-1])

    if L != 1:
        B[L-2] -= V
    if R != N:
        B[R-1] += V
    
    ans_a = abs(B[L-2]) + abs(B[R-1])
    ans += ans_a - ans_b

    print(ans)
