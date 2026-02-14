x1, y1, x2, y2 = map(int, input().split())

v_1_2 = [x2 - x1, y2 - y1]
P = [[-1, 1], [1, -1]]

for p in P:
    v_2_3 = [p[0] * v_1_2[1], p[1] * v_1_2[0]]
    x3 = x2 + v_2_3[0]
    y3 = y2 + v_2_3[1]
    x4 = x1 + v_2_3[0]
    y4 = y1 + v_2_3[1]
    v_4_3 = [x3 - x4, y3 - y4]

    area = (x2 - x1) * (y2 + y1) + (x3 - x2) * (y3 + y2) + (x4 - x3) * (y4 + y3) + (x1 - x4) * (y1 + y4)

    if area < 0:
        print(x3, y3, x4, y4)
