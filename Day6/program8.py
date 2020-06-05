def Print(R,C,array):
    x=0
    y=0
    while(x < R and y < R):
        for i in range(y,C):
            print(array[x][i], end = " ")
    
        x += 1
        for i in range(x,R):
            print(array[i][C-1], end = " ")

        C -=1 
        if (x < R):
            for i in range(C-1,(y-1),-1):
                print(array[R-1][i], end = " ")
            
            R -= 1
            for i in range(R-1 , x-1 , -1):
                print(array[i][y] , end = " ")
            
            y += 1


arr = [ [1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]]
print("The array is : ",arr)
rows = 3
columns = 6
print("\n The array in spiral form is : ")
Print(rows,columns,arr)
