n = input()
lst = []
for j in range(97,123):
  lst.append(chr(j))
x=0
while(x<=25):
  new=n.replace(".",lst[x])
  if new==new[::-1]:
    print(new,end='')
    break
  new=n
  x+=1
else:
  print('-1',end='')