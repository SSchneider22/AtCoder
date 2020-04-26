import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().replace("\n","").split()))
b = list(map(int, input().replace("\n","").split()))
c = list(map(int, input().replace("\n","").split()))

sa = sorted(a)
sb = sorted(b)
sc = sorted(c)

ans = 0
for i in range(len(sa)):
    bleft = 0
    bright = len(sb) - 1
    while bleft <= bright:
        mid = (bleft + bright) // 2 # "//"で、小数点以下切り捨ての割り算になる"
        if sb[mid] == 