import sys
import math
import decimal
input = sys.stdin.readline

a, b, c = map(int, input().split())

if a + 2*(math.sqrt(a)*math.sqrt(b)) + b < c:
    print("Yes")
else:
    print("No")


"""
if a >= b:
    if (a-b) < (math.sqrt(a)*math.sqrt(c) - math.sqrt(b)*math.sqrt(c)):
        print("Yes")
    else:
        print("No")
else :
    if (b-a) < (math.sqrt(b)*math.sqrt(c) - math.sqrt(a)*math.sqrt(c)):
        print("Yes")
    else:
        print("No")
"""


"""
if (decimal.Decimal(math.sqrt(a)) + decimal.Decimal(math.sqrt(b))) < decimal.Decimal(math.sqrt(c)):
    print("Yes")
else:
    print("No")
"""