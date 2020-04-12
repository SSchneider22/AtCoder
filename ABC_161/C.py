import sys
input = sys.stdin.readline

n, k = map(int, input().split())

ans = n%k

if ans > abs(ans-k):
    ans = abs(ans-k)

print(ans)