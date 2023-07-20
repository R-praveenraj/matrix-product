def matrixProduct(matrix,b,row,column):
    for i in range(row):
        for j in range(column):
            matrix[i][j]=matrix[i][j]*b
    return matrix

row=int(input())
column=int(input())
b=int(input())
matrix=[]
for i in range(row):
    matrix.append(list(map(int,input().split())))
print(matrixProduct(matrix,b,row,column))
