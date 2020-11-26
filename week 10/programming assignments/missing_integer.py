n = set(map(int,input().split(" ")))
lst = list(n)
a = [i for i in range(1,lst[-1]+1) if i not in lst]
try:
    print(a[0],end="")
except:
    print(max(lst)+1,end="")