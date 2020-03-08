import sys
input = sys.stdin.readline

s = input().rstrip("\n")
q = int(input())

for i in range(q):
    # query = list(map(str, input().split()))
    query = list(input().split())
    if query[0] == "1":
        s = s[::-1]
        continue
    else:
        if query[1] == "1":
            slist = [query[2],s]
            s = ''.join(slist)
            # s = query[2] + s
        else:
            slist = [s,query[2]]
            s = ''.join(slist)
            # s = s + query[2]

    #print("{}回目:{}".format(i+1,s))

print(s)

"""入力例
a
4
2 1 p
['2', '1', 'p']
1
['1']
2 2 c
['2', '2', 'c']
1
['1']
"""