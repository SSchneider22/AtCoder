a = []
total = 0
n,m = map(int,input().split())
for i in range(m):
    a.append(int(input()))
    if int(a[-1]) - int(a[-2]) == 1:
        print(0)

ans = total % 1000000007
print(ans)