#最大公約数
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

#最小公倍数
def lcm(a,b):
    return a*b//gcd(a,b)

a,b,c,d = map(int,input().split())

bandc = b // c 
bandd = b // d
bandcd = b // lcm(c,d)

aandc = a // c 
aandd = a // d
aandcd = a // lcm(c,d)

totalb = b - bandc - bandd + bandcd
totala = a - aandc - aandd + aandcd
#print(totalb)
#print(totala)
if (a % c != 0) and (a % d != 0):
    ans = totalb - totala + 1
else:
    ans = totalb - totala

print(ans)

"""
val = c*d
total = b - a + 1
for i in range(a,b+1):
    if i % c == 0:
        count = count - 1
    elif i % d == 0:
        count = count - 1
    elif i % val == 0:
        count = count + 1
print(count)
"""