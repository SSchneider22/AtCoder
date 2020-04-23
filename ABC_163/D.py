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
