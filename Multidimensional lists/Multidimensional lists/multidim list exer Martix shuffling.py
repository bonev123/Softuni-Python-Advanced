rows, cols = [int(el) for el in input().split()]
matrix = []
for _ in range(rows):
    matrix.append([el for el in input().split()])

command = input().split()

while not command[0] == 'END':
    if len(command) == 5 and command[0] == 'swap':
        row1 = int(command[1])
        col1 = int(command[2])
        row2 = int(command[3])
        col2 = int(command[4])
        if 0 <= row1 < rows and 0 <= col1 < cols and 0 <= row2 < rows and 0 <= col2 < cols:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            [print(*row, sep=" ") for row in matrix]

        else:
            print(f'Invalid input!')

    else:
        print(f'Invalid input!')
    command = input().split()

