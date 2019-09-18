def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print("{}".format(matrix[i][j]), end="")
                if j != len(matrix[i]) - 1:
                    print(" ", end="")
            print()
