str_lst = list(map(str,input().strip()))
holes = ['A','B','D','O','P','Q','R']
count = 0
for i in str_lst:
    for j in holes:
        if i == j == 'B':
            count += 2
        elif i == j:
            count += 1
print(count,end="")