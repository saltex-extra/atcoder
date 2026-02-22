N, M = map(int, input().split())
selected = set()

for _ in range(N):
    L = int(input())
    X = list(map(int, input().split()))

    for x in X:
        if x not in selected:
            selected.add(x)
            print(x)
            break
    else:
        print(0)
