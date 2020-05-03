import sys
input = sys.stdin.readline

n, m = map(int, input().replace("\n","").split())
h = list(map(int, input().replace("\n","").split()))

chklist= [1] * n

# road = []
for i in range(m):
    # road.append(list(map(int, input().replace("\n","").split())))
    a, b = map(int, input().replace("\n","").split())

    if h[a-1] < h[b-1]:
        chklist[a-1] = 0
        if chklist[b-1] != 0:
            chklist[b-1] = 1

    elif h[a-1] > h[b-1]:
        chklist[b-1] = 0
        if chklist[a-1] != 0:
            chklist[a-1] = 1

    elif h[a-1] == h[b-1]:
        chklist[a-1] = 0
        chklist[b-1] = 0

print(chklist.count(1))