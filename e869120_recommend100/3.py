# https://atcoder.jp/contests/abc122/tasks/abc122_b

import sys
input = sys.stdin.readline # 改行コード「\n」を呼んでしまうため、文字数など、注意！！

s = input().replace("\n","")

ans = 0

for i in range(len(s)):
    cnt = 0
    for j in range(i,len(s)):
        # print(len(s),i)
        # print(s[j:])
        # print(s[j])
        if s[j] == 'A' or s[j] == 'C' or s[j] == 'G' or s[j] == 'T':
            cnt += 1
            if cnt > ans:
                ans = cnt
        else:
            # print("AGCT意外です。カウント数：",cnt)
            break

print(ans)