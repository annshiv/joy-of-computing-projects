n,m = input().split()
matrix = []
n = int(n)
m = int(m)
for i in range(n):
    lst = list(map(str,input().split(" ")))
    matrix.append(lst)

i = 0
alphanumeric = ['!','@','#','$','%','&']
word = ""
for i in range(m):
    for j in range(n):
        if matrix[j][i] in alphanumeric:
            continue
        else:
            word += matrix[j][i]

print(word,end=" ")