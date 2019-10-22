n = int(input())
wl = list(map(int,input().split()))

ans = 10000000

for t in range(n-1):
    #print('ループ{}回目',t+1)
    s1 = sum(wl[:t+1])
    #print('s1 = {}',s1)
    s2 = sum(wl[t+1:])
    #print('s2 = {}',s2)
    if abs(s2-s1) < ans:
        ans = abs(s2-s1)

print(str(ans))
