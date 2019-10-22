n,k = map(int,input().split())
a = list(map(int,input().split()))

ans = 0
for i in range(n):
    total = sum(a[i:])
    for j in range(n):
        sub_total = total - a[n-j-1]
        print(sub_total)
        if sub_total >= k:
            ans  = ans + 1
        else:
            break
    #print(a[i:])
    #print(total)
print(ans)
