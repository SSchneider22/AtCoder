# https://atcoder.jp/contests/abc106/tasks/abc106_b

import sys
input = sys.stdin.readline # 改行コード「\n」を呼んでしまうため、文字数など、注意！！

n = int(input())
ans = 0

for i in range(1, n+1,2):
    cnt = 0
    for j in range(1,i+1):
        # print(i,j)
        if i % j == 0:
            cnt += 1
        if cnt == 8:
            ans += 1
            break
    # print(cnt)

print(ans)