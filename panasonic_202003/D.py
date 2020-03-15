import sys
from itertools import permutations, combinations,combinations_with_replacement
input = sys.stdin.readline

n = int(input())
al=[chr(ord('a') + i) for i in range(n)]

checklist = list(combinations_with_replacement(al,n))

print(checklist[0])