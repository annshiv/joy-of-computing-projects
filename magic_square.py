def magic_square(n):
    square = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        square.append(l)
    
    for i in range(n):
      for j in range(n):
        print(square[i][j],end=" ")
      print()

    m = (n*((n**2)+1))/2
    
    row = int(n/2)
    col = n-1

    count = 1
    num = n*n


    while count <= num:
        if count == 1:
            return square[row][col] + 1
            count += 1
    print(square)

magic_square(3)