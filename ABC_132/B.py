import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int,input().split()))

ans = 0

for i in range(len(p)-2):
    if (p[i] < p[i+1] and p[i+1] < p[i+2]) or (p[i+2] < p[i+1] and p[i+1] < p[i]):
        ans = ans + 1
    else:
        continue

print(ans)

"""
for i in range(len(p)-2):
    q = [p[i],p[i+1],p[i+2]]
    q.sort()
    print(q)
    if q[0] < q[1] and q[1] < q[2]:
        ans = ans + 1
    else:
        continue

print(ans)
"""