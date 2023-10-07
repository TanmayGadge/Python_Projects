matrix1 = [[1,2,3], [4,5,6], [7,8,9]]
matrix2 = [[1,0,0], [2,0,0], [3,0,0]]

def squareMatrixAdd(matrix1, matrix2):
    rows1 = len(matrix1)#Number of rows in matrix 1
    columns1 = len(matrix1[0])#Number of columns in matrix 1

    sum = [[0,0,0], [0,0,0], [0,0,0]]
    
    for i in range(rows1):
        for j in range(columns1):
            (sum[i])[j] = (matrix1[i])[j] + (matrix2[i])[j]

    return sum,


# print(squareMatrixAdd(matrix1, matrix2))


def matrixAdd(matrix1, matrix2):

    rows_in_matrix1 = len(matrix1)
    rows_in_matrix2 = len(matrix2)
    columns_in_matrix1 = len(matrix1[0])
    columns_in_matrix2 = len(matrix2[0])

    sum = []
    for _ in range(rows_in_matrix1):
        sum.append([0]*columns_in_matrix1)

    if(rows_in_matrix1 == rows_in_matrix2 and columns_in_matrix1 == columns_in_matrix2):
        for i in range(rows_in_matrix1):
            for j in range(columns_in_matrix1):
                (sum[i])[j] = (matrix1[i])[j] + (matrix2[i])[j]

    else:
        sum = "Only matrices of same order can be added."

    
    return sum

m1 = [[1,2,3], [1,0,0]]
m2 = [[1,2,3], [2,1,1]]
print(matrixAdd(m1, m2))   