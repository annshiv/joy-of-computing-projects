import math
c = 50
h = 30
q_values = list(map(int,input().split(',')))
lst = []
for i in q_values:
    q = str(int(round(math.sqrt((2 * c * i)/h))))
    lst.append(q)

print(",".join(lst),end="")