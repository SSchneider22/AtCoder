import sys
input = sys.stdin.readline

A = [0] * 4

s = input()
for i in range(4):
    A[i] = s[i]

A_uni = list(set(A))

if len(A_uni) == 2:
    print('Yes')
else:
    print('No')


