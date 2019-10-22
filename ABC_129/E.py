l2 = str(input())
l = int(l2,2) 

total = 0
for i in range(l+1):
    for j in range((l+1)-i):
        if (i+j <= l) and ((i+j) == (i^j)):
            #print('i = {}  ,j = {}  ,i^j={}',bin(i),bin(j),i^j)
            #print('OK!i={},j={}',i,j)
            total += 1

ans = total % 1000000007
print(ans)