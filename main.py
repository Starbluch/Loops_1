def Chessboard():
    cell = int(input("Enter the number of the cell: "))

    if cell < 1 or cell > 6:
        print("Cell number must be between 1 and 6.")
        return


    for value in range(6):
        for value2 in range(6):
            if value < 3:
                if value2 % 2 == 0:
                    print(cell * "*", end="")
                else:
                    print(cell * "_", end="")
            else:
                if value2 % 2 == 0:
                    print(cell * "_", end="")
                else:
                    print(cell * "*", end="")
        print()
        # if (cell >= 3):
        #     print("\n")
        # else:
        #     pass

Chessboard()
