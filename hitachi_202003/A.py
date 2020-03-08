import sys
input = sys.stdin.readline

s = input()
s = s.replace('\n','')
s = s.replace('hi','')

if len(s)==0:
    print("Yes")
else:
    print("No")

