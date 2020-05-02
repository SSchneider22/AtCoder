import sys
input = sys.stdin.readline

x = int(input())
ans = 100

for i in range(1,10000000000):
    ans += int(ans/100)
    if ans >= x:
        print(i)
        break
