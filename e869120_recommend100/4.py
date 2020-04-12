# https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_c

import numpy as np
import sys
input = sys.stdin.readline  # 改行コード「\n」を呼んでしまうため、文字数など、注意！！

n, m = map(int, input().replace("\n","").split())
plist = [[int(j) for j in input().replace("\n","").split()] for i in range(n)]

ans = 0

for i in range(m):
    for j in range(i+1,m):
        anslist = []
        for k in range(n):
            anslist.append(max(plist[k][i], plist[k][j]))
            if ans < sum(anslist):
                ans = sum(anslist)

print(ans)

"""
nplist = np.array(plist)

sumlist = np.sum(nplist, axis=0)
print(sumlist)
"""
