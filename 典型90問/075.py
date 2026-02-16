N = int(input())
cnt = 0
ans = 0

i = 2
while i * i <= N:
    while N % i == 0:
        cnt += 1
        N //= i
    i += 1

cnt += 1 if N != 1 else 0

if cnt > 1:
    i = 1
    while cnt // (2 ** i) != 1:
        i += 1

    ans = i if cnt % (2 ** i) == 0 else i + 1
else:
    ans = 0
    
print(ans)
