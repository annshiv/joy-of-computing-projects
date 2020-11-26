i = str(input())
posi = int(i.count('0'))
neg = int(i.count('1'))

if posi == 1 or neg == 1:
    print("YES",end="")
else:
    print("NO",end="")