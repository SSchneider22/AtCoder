import sys
import copy
input = sys.stdin.readline

round=lambda x:(x*2+1)//2

n = int(input())
d = list(map(int,input().split()))

ans = 0
testd = []

for i in range(max(d)):
    testd = copy.copy(d)
    testd.append(i)
    testd.sort()
    index_num = [n for n, v in enumerate(testd) if v == i]
    ix_max = max(index_num)
    ix_min = min(index_num)
    #print(i,ix_max,ix_min,round(len(testd)/2)-1)
    #if ix_max == round(len(testd)/2)-1 or ix_min == round(len(testd)/2)-1:
    if ix_min == round(len(testd)/2)-1:
        #print(testd)
        #print(i,ix_max,ix_min,round(len(testd)/2)-1,len(testd)/2)
        ans = ans + 1

print(ans)