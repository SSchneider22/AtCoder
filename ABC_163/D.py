n,k = map(int, input().split())

ans = 0
mod = 10**9+7

for i in range(k,n+2):
    ans += int((n*(n+1)/2 - (n-i)*(n-i+1)/2 - (i-1)*i/2 +1))

print(ans%mod)


"""
import sys
input = sys.stdin.readline
from functools import reduce
mod = 10 ** 9 + 7

def cmb(r):
    numerator = reduce(lambda x, y: x * y % mod, [n - r + k + 1 for k in range(r)])
    denominator = reduce(lambda x, y: x * y % mod, [k + 1 for k in range(r)])
    return numerator * pow(denominator, mod - 2, mod) % mod

n, k = map(int, input().replace("\n","").split())

if k-n == 1:
    print(1)
    exit()

print(cmb(n+1))
"""