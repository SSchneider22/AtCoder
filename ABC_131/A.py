s = input()

for i in range(len(s)):
    if i == 0:
        continue
    if int(s[i]) - int(s[i-1]) == 0:
        print('Bad')
        exit()
print('Good')