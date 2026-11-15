import os
import random as rand


def depth_first(matrix: list):

    start_y = rand.randint(1, len(matrix) - 2)
    start_x = rand.randint(1, len(matrix[0]) - 2)

    visited = []

    matrix[start_y][start_x] = 1
    

    current_x = start_x
    current_y = start_y

    # loop that continues until the whole maze is generated
    completed = False
    while completed == False:

        while True:
            # directions = ["u", "d", "l", "r"]
            directions = ["u"]

            choice = rand.choice(directions)
            directions.remove(choice)

            new_y = current_y
            new_x = current_x
            # list used to check all the (relevant) adjacent tiles
            adj_tiles = []

            match choice:
                case "u":
                    # checks that negative indexing or edges aren't being hit
                    if (current_y-2 > 0 and current_y < (len(matrix)-1) and current_x-1 > 0 and current_x+1 < (len(matrix[0])-1)):
                    
                        adj_tiles.append(matrix[current_y - 1][current_x - 1]) # tile to west
                        adj_tiles.append(matrix[current_y - 2][current_x - 1]) # tile to north-west
                        adj_tiles.append(matrix[current_y - 2][current_x]) # tile to north
                        adj_tiles.append(matrix[current_y - 2][current_x + 1]) # tile to north east
                        adj_tiles.append(matrix[current_y - 1][current_x + 1]) # tile to east
                        # moves tile up 1
                        if 1 not in adj_tiles:
                            new_y += 1
                            print("valid move")
                            break
                        else:
                            print("invalid move")
                            break
                    else:
                        print("invalid move")
                        break
                    
                case "d":
                    adj_tiles.append(matrix[current_y - 1][current_x - 1]) # tile to west
                    adj_tiles.append(matrix[current_y - 2][current_x - 1]) # tile to north-west
                    adj_tiles.append(matrix[current_y - 2][current_x]) # tile to north
                    adj_tiles.append(matrix[current_y - 2][current_x + 1]) # tile to north east
                    adj_tiles.append(matrix[current_y - 1][current_x + 1]) # tile to east
                    # moves tile up 1
                    if 1 not in adj_tiles:
                        new_y += 1
                        break
                case "l":
                    pass
                case "r":
                    pass

            break

        matrix[new_y][new_x] = 1
        
        visited.append(matrix[current_y][current_x])

        current_y = new_y
        current_x = new_x
        break

    return matrix


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

    print("----------------- MATRIX ONE ------------------------")
    for r in matrix:
        print(r)
    matrix = depth_first(matrix)
    print("----------------- MATRIX TWO ------------------------")
    for r in matrix:
        print(r)
