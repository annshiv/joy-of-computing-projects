def mini(n):
    k = str(n)
    r = len(k)
    lst = [int(x) for x in k]
    a = sum(lst)
    v = str(a)
    if len(v)==1:
        print(v)
    else:
        b = int(v)
        mini(b)
n = int(input())
mini(n)