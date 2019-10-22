p,q,r = map(int,input().split())

A = p+q
B = q+r
C = p+r
mylist = [A,B,C]

print(min(mylist))