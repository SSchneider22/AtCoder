# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d

import sys
input = sys.stdin.readline  # 改行コード「\n」を呼んでしまうため、文字数など、注意！！

n = int(input().replace("\n",""))
s = input().replace("\n","")

ans = 0
for i in range(1000):
    i = str(i).zfill(3)
    x = s.find(i[0])
    y = s.find(i[1], x+1)
    z = s.find(i[2], y+1)
    if x != -1 and y != -1 and z != -1:
        ans += 1
print(ans)


"""
anslist = []
ans = 0

for i in range(1000):
    if i < 10:
        chk = '00' + str(i)
    elif i < 100:
        chk = '0' + str(i)
    else:
        chk = str(i)

    for j in range(len(s)):
        if s[j] == chk[0]:
            for k in range(j+1, len(s)):
                if s[k] == chk[1]:
                    for l in range(k+1, len(s)):
                        if s[l] == chk[2]:
                            # print(chk)
                            anslist.append(chk)
            continue
ans = len(set(anslist))
print(ans)
"""