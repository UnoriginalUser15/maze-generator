import os
from random as r


def depth_first(matrix: list):

    start_x = r.randint(1, len(matrix) - 2)
    start_y = r.randint(1, len(matrix[0]) - 2)

    open_visited = []

    matrix[start_x][start_y] = 1
    

    current_x = start_x
    current_y = start_y

    completed = False
    while completed == False:
        while True:
            directions = ["u", "d", "l", "r"]
            
            choice = r.choice(directions)
            directions.remove(choice)

            match choice:
                case "u":
                    
                case "d":
                    pass
                case "l":
                    pass
                case "r":


        
        
        open_visited.append(matrix[current_x][current_y])
        break


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

    depth_first(matrix)
    for r in matrix:
        print(r)
