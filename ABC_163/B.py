import sys
input = sys.stdin.readline

n, m = map(int, input().replace("\n","").split())
a = list(map(int, input().replace("\n","").split()))

syukudai = sum(a)
if syukudai > n:
    print(-1)
else:
    print(n-syukudai)