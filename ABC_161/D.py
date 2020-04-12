import sys
input = sys.stdin.readline

k = int(input())

lunlist = [1,2,3,4,5,6,7,8,9,10,11,12,21,22,23]
for i in range(24,3234566670):
    chk = str(i)
    count = 0
    for j in range(len(chk)-1):
        # print(i,"　を確認します")
        # print(int(chk[j]))
        # print(int(chk[j+1]))
        if abs(int(chk[j])-int(chk[j+1])) >= 2:
            # print("abs：",abs(int(chk[j])-int(chk[j+1])))
            count += 1
            # print("countしました！")

    if count == 0:
        lunlist.append(i)
        # print(i,"をるんリストに追加！")

print(lunlist)

print(lunlist[k-1])