import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
s = [input().replace("\n","") for i in range(n)]

Scnt = Counter(s)
print(len(Scnt.values()))