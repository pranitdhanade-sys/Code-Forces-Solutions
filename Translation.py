s = input()
t = input()
a = True
for i in range(len(s)):
    if s[i] != t[-i]:
        a = False
if a:
    print("YES")
else:
    print("NO")
