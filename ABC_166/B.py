import sys
input = sys.stdin.readline
from collections import Counter

#intl = [1,1,1,2,2,2,2,2,2,2,3,3,3,3,4,4,4]
#print(ints[1]) # 3

n, k = map(int, input().replace("\n","").split())

snuke =  [0] * n
# print(snuke)

havelist = []

for i in range(k):
    d = int(input())
    a = list(map(int, input().replace("\n","").split()))

    havelist.extend(a)

have = len(list(set(havelist)))
print(n-have)

"""
お菓子がK種類


"""