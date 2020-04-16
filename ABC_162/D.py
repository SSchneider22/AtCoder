# Pypy3のほうがTLE数少なかった、速そう

import itertools
import sys
input = sys.stdin.readline

n = int(input().replace("\n",""))
s = input().replace("\n","")
orgs = s

ans = 0


for i in range(n):
    for j in range(i+1, n):
        if s[i] != s[j]:
            if ('R' != s[i]) and ('R' != s[j]):
                ans += s[j+1:].count('R')
                if len(s) > j+(j-i):
                    if s[j+(j-i)] == 'R':
                        ans -= 1
            elif ('G' != s[i]) and ('G' != s[j]):
                ans += s[j+1:].count('G')
                if len(s) > j+(j-i):
                    if s[j+(j-i)] == 'G':
                        ans -= 1
            elif ('B' != s[i]) and ('B' != s[j]):
                ans += s[j+1:].count('B')
                if len(s) > j+(j-i):
                    if s[j+(j-i)] == 'B':
                        ans -= 1


"""
for i in range(n):
    for j in range(i+1, n):
        if s[i] != s[j]:
            for k in range(j+1, n):
                if (s[i] != s[k]) and (s[j] != s[k]) and (j-i != k-j):
                    ans += 1
"""

print(ans)