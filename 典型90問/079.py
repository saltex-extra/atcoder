H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]
cnt = 0

C = [[0] * W for _ in range(H)]
chk = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        C[i][j] = B[i][j] - A[i][j]
        
for i in range(H-1):
    for j in range(W-1):
        x = C[i][j]
        C[i][j] -= x
        C[i+1][j] -= x
        C[i][j+1] -= x
        C[i+1][j+1] -= x
        cnt += abs(x)

if C == chk:
    print('Yes')
    print(cnt)
else:
    print('No')
