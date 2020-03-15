import sys
input = sys.stdin.readline

h, w = map(int, input().split())

if (h==1)or(w==1):
    print(1)
    exit()

allmas = h*w

if allmas % 2 == 1:
    print(int((allmas/2) + 0.5))
else:
    print(int(allmas/2))