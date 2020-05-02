from itertools import permutations, combinations,combinations_with_replacement,product
import sys
input = sys.stdin.readline

n, m, q = map(int, input().replace("\n","").split())
a = [[int(j) for j in input().replace("\n","").split()] for i in range(q)]


tmp = [i for i in range(1,m+1)]
chk = list(combinations_with_replacement(tmp, n))
# print(list(chk[0]))

tmpans = 0
ans = 0

for i in range(len(chk)):
    tmpans = 0
    for j in range(q):
        if (chk[i][a[j][1]-1] - chk[i][a[j][0]-1]) == a[j][2]:
            tmpans += a[j][3]
    if tmpans >= ans:
        ans = tmpans

print(ans)
