def multiplyMatrix(m1, m2):

    if(len(m1[0]) != len(m2)):
        print("The given matrices can't be multiplied.")
    
    else:
        rows_in_result = len(m1)
        columns_in_result = len(m2[0])

        result_matrix = []#Initialising the product of the matrices as an empty list.

        #Setting the product matrix as a null matrix of appropriate order.
        for i in range(rows_in_result):
            result_matrix.append([0]*columns_in_result)

        #Multiplying the matrices
        for s in range(len(m1)):
            for k in range(len(m2[0])):

                column = [m2[i][k] for i in range(len(m2))]

                result_element = 0
                for p in range(len(column)):
                    result_element += column[p]*m1[s][p]

                result_matrix[s][k] = result_element


        # Printing the product matrix in a more readable format.
        for row in result_matrix:
            print(row)


matirx1 = [[1,2,3], [4,5,6], [7,8,9]]
matrix2 = [[1,0,0], [0,1,0], [0,0,1]]
multiplyMatrix(matirx1, matrix2)