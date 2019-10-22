n,l = map(int,input().split())

alist = []
testlist = []
for i in range(n):
    if i == 0:
        alist.append(l)
        testlist.append(abs(l))
    else:
        alist.append(l+i)
        testlist.append(abs(l+i))
k = testlist.index(min(testlist))
alist.pop(k)
print(sum(alist))

"""
リスト作って、全体を絶対値出して、昇順ソートし、一番最初のものを除く
"""