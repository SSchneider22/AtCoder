import sys
from math import factorial
input = sys.stdin.readline

n, m = map(int, input().split())

if n == 1 and m == 1:
    print(0)
    exit()

# 偶数＆偶数
if n > 2:
    ans1 = factorial(n) / factorial(2) / factorial(n - 2)
elif n == 2:
    ans1 = 1
elif n <= 1:
    ans1 = 0

# 奇数 & 奇数
if m > 2:
    ans2 = factorial(m) / factorial(2) / factorial(m - 2)
elif m == 2:
    ans2 = 1
elif m <= 1:
    ans2 = 0

print(int(ans1 + ans2))