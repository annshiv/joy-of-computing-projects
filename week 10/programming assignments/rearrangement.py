n = list(map(int,input().split(" ")))
n.sort()
a = [x for x in range(0,max(n)+1)]
lst = [i for i in range(0,max(n)+1) if i not in n]
for i in lst:
    a[i] = -1
print(*a,end="")