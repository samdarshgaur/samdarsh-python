def rotate_mat(mat): 
    L = len(mat[0]) 
    for x in range(L // 2): 
        for y in range(x, L - x - 1): 
            temp = mat[x][y] 
            mat[x][y] = mat[L - 1 - y][x] 
            mat[L - 1 - y][x] = mat[L - 1 - x][L - 1 - y] 
            mat[L - 1 - x][L - 1 - y] = mat[y][L - 1 - x] 
            mat[y][L - 1 - x] = temp 
  
def print_mat(mat): 
    L = len(mat[0]) 
    for x in range(L): 
        print(mat[x]) 
   
mat = [[1, 2, 3], 
     [4,5,6],
     [7,8,9]] 
print("The matrix is : ")
print_mat(mat)
rotate_mat(mat) 
print("The matrix now is : ")
print_mat(mat) 
