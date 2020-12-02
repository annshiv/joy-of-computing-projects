m,n = input().split(",")
lst = [str(x) for x in range(int(m),int(n)+1)]
result = []
for i in lst:
    j = 0
    for k in range(4):
        if (int(i[k])%2 == 0):
            j += 1
        if(j==4):
            result.append(i)
print(",".join(result),end="")