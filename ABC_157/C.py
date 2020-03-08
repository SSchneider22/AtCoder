import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sclist = []
for i in range(m):
    sclist.append(list(map(int, input().split())))

roupcount = 1
for i in range(n):
    roupcount *= 10

for i in range(roupcount):
    stri = str(i)
    mclearcount = 0
    if m == 0:
        print("-1")
        sys.exit()

    if n == 2 and i < 10:
        continue
    elif n == 3 and i < 100:
        continue

    for j in range(m):
        if str(stri[int(sclist[j][0])-1]) == str(sclist[j][1]):
            mclearcount += 1
            if mclearcount == m:
                print(i)
                sys.exit()
        else:
            break
print("-1")


"""
最後２つのテストがエラー他に考えられるケース

１．Nが０のとき
1 1
1 0

２．Mが０のとき
1 0

３．100を答えにしたいとき
3 5
1 1
2 1
3 0
3 0
3 0

3 3
1 1
2 0
3 0



"""