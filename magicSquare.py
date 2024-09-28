size = int(input("Enter an odd value for the size of the magic square: "))


if size % 2 == 0:
    print("Please enter an odd value.")
else:

    array = [[0 for _ in range(size)] for _ in range(size)]

    p = size // 2  
    q = size - 1   

    for i in range(1, (size * size) + 1):
        
        if p == -1 and q == size:  
            p = 0
            q = size - 2
        else:
            if p == -1:  
                p = size - 1
            if q == size:  
                q = 0

        
        if array[p][q] == 0:
            array[p][q] = i
        else: 
            p = p + 1
            q = q - 2
            array[p][q] = i

  
        p = p - 1
        q = q + 1

    for row in array:
        for element in row:
            print(f"{element:3}", end=" ")
        print()