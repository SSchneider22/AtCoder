# https://atcoder.jp/contests/abc145/tasks/abc145_c

from itertools import permutations, combinations,combinations_with_replacement,product
import sys
input = sys.stdin.readline
import math

n = int(input())
town = []
for i in range(n):
    town.append(list(map(int, input().replace("\n","").split())))
townnum = [i for i in range(n)]

chklist = list(permutations(townnum))

sumval = 0.0
for i in range(len(chklist)):
    for j in range(n-1):
        sumval += math.sqrt(((town[chklist[i][j]][0] - town[chklist[i][j+1]][0])**2) + ((town[chklist[i][j]][1] - town[chklist[i][j+1]][1])**2))

print(sumval/len(chklist))