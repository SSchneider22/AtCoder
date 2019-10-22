n,x = map(int,input().split())
l = list(map(int,input().split()))
ans = 1
score = 0

for i in range(n):
    score = score + l[i]
    if  score <= x:
        ans = ans + 1

print(ans)