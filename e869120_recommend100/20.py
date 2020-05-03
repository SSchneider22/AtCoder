# https://atcoder.jp/contests/abc077/tasks/arc084_a

from bisect import bisect_left,bisect_right
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
for i in range(n):
    ab = bisect_left(sa,sb[i])
    bc = n - bisect_right(sc,sb[i])

    if ab == 0:
        continue
    ans += ab * bc

print(ans)