from itertools import permutations, combinations,combinations_with_replacement,product
import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().replace("\n","").split()))
q = list(map(int, input().replace("\n","").split()))

dic = list(permutations(p))
dic.sort()

tp = tuple(p)
tq = tuple(q)

print(abs(dic.index(tp)-dic.index(tq)))