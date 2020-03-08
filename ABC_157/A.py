import sys
input = sys.stdin.readline

n = int(input())

if n % 2 == 0:
    ans = n/2
else:
    ans = n/2 + 0.5

print(int(ans))