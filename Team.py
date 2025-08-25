n =  int(input())
temp = 0
res = 0
for i in n:
    for j in i:
        if j == 1:
            temp +=1
    if temp == 2:
        res += 1
    temp = 0
return res



