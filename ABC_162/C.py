# Pypy3だと通った

import math
from functools import reduce
import sys
input = sys.stdin.readline  # 改行コード「\n」を呼んでしまうため、文字数など、注意！！


def gcd(*numbers):
    return reduce(math.gcd, numbers)

# print(gcd(100,20,10))

k = int(input().replace("\n",""))
ans = 0

for a in range(1,k+1):
    for b in range(1,k+1):
        for c in range(1,k+1):
            ans += gcd(a,b,c)

print(ans)


"""

"""