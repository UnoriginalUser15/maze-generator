import os



def gen_matrix(width: int, height: int):
    """
    Generates a list that contains lists of 0s.\n
    width --> defines how large list of 0s is\n
    height --> defines how many lists of 0s are in the matrix
    """
    matrix = []
    # populates the matrix with lists of 0 based on defined w & h
    for i in range(height):
        matrix.append([0] * width)

    return matrix


if __name__ == "__main__":
    width = int(input("w: "))
    height = int(input("h: "))
    
    matrix = gen_matrix(width, height)

    matrix[2][3] = 1

    for r in matrix:
        print(r)