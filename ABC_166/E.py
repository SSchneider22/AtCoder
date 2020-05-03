from itertools import permutations, combinations,combinations_with_replacement,product
import sys
input = sys.stdin.readline

n = int(input())
memberlist = [i for i in range(1,n+1)]
lengthlist = list(map(int, input().replace("\n","").split()))

combilist = list(combinations(memberlist, 2))

ans = 0
for i in range(len(combilist)):
    """
    print(list(combilist[i]))
    print(abs(list(combilist[i])[0] - list(combilist[i])[1]))
    print(lengthlist[list(combilist[i])[0]-1] + lengthlist[list(combilist[i])[1]-1])
    print("----------")
    """
    if abs(list(combilist[i])[0] - list(combilist[i])[1]) == (lengthlist[list(combilist[i])[0]-1] + lengthlist[list(combilist[i])[1]-1]):
        ans += 1

print(ans)


"""
探索すべきは、
"""