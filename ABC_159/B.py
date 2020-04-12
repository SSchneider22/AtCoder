import sys
input = sys.stdin.readline

s = input().replace("\n","")

reverse_s = s[::-1]

s1len = int((len(s)/2))

s1 = s[:s1len]
reverse_s1 = s1[::-1]
# print(s1)

s2len = int((len(s)/2) + 1)
s2 = s[s2len:]
reverse_s2 = s2[::-1]
# print(s2)


if (s == reverse_s) and (s1 == reverse_s1) and (s2 == reverse_s2):
    print("Yes")
else:
    print("No")