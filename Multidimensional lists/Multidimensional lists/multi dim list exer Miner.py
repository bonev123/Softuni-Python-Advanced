def find_miner(row, col):
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == 's':
                return row, col


# def find_all_coals(matrix, row, col):
#     total_coals = 0
#     for row in range(n):
#         for col in range(n):
#             if matrix[row][col] == 'c':
#                 total_coals += 1
#             return total_coals


n = int(input())
command = input().split()
matrix = []
row = 0
col = 0
total_coals = 0
coals_collected = 0

for _ in range(n):
    matrix.append(input().split())

for row in range(n):
    for col in range(n):
        if matrix[row][col] == 'c':
            total_coals += 1

for comm in command:
    if comm == 'left':
        position = (find_miner(row, col))
        row = position[0]
        col = position[1]
        if col <= 0:
            continue
        if matrix[row][col - 1] == '*':
            matrix[row][col - 1] = 's'
            matrix[row][col] = '*'
        elif matrix[row][col - 1] == 'c':
            coals_collected += 1
            matrix[row][col - 1] = 's'
            matrix[row][col] = '*'
            #if not find_all_coals(matrix, row, col):
            if total_coals <= coals_collected:
                print(f'You collected all coals! ({row}, {col - 1})')
        elif matrix[row][col - 1] == 'e':
            print(f"Game over! ({row}, {col - 1})")
            exit(0)
    elif comm == 'right':
        position = (find_miner(row, col))
        row = position[0]
        col = position[1]
        if col >= n - 1:
            continue
        if matrix[row][col + 1] == '*':
            matrix[row][col + 1] = 's'
            matrix[row][col] = '*'
        elif matrix[row][col + 1] == 'c':
            coals_collected += 1
            matrix[row][col + 1] = 's'
            matrix[row][col] = '*'
            #if not find_all_coals(matrix, row, col):
            if total_coals <= coals_collected:
                print(f'You collected all coals! ({row}, {col + 1})')
        elif matrix[row][col + 1] == 'e':
            print(f"Game over! ({row}, {col + 1})")
            exit(0)

    elif comm == 'up':
        position = (find_miner(row, col))
        row = position[0]
        col = position[1]
        if row <= 0:
            continue
        if matrix[row - 1][col] == '*':
            matrix[row - 1][col] = 's'
            matrix[row][col] = '*'
        elif matrix[row - 1][col] == 'c':
            coals_collected += 1
            matrix[row - 1][col] = 's'
            matrix[row][col] = '*'
            #if not find_all_coals(matrix, row, col):
            if total_coals <= coals_collected:
                print(f'You collected all coals! ({row - 1}, {col})')
        elif matrix[row - 1][col] == 'e':
            print(f"Game over! ({row - 1}, {col})")
            exit(0)
    elif comm == 'down':
        position = (find_miner(row, col))
        row = position[0]
        col = position[1]
        if row >= n - 1:
            continue
        if matrix[row + 1][col] == '*':
            matrix[row + 1][col] = 's'
            matrix[row][col] = '*'
        elif matrix[row + 1][col] == 'c':
            coals_collected += 1
            matrix[row + 1][col] = 's'
            matrix[row][col] = '*'
            #if not find_all_coals(matrix, row, col):
            if total_coals <= coals_collected:
                print(f'You collected all coals! ({row + 1}, {col})')
        elif matrix[row + 1][col] == 'e':
            print(f"Game over! ({row + 1}, {col})")
            exit(0)
if total_coals > coals_collected:
    if command[-1] == 'down':
        print(f"{total_coals - coals_collected} coals left. ({row + 1}, {col})")
    elif command[-1] == 'up':
        print(f"{total_coals - coals_collected} coals left. ({row - 1}, {col})")
    elif command[-1] == 'right':
        print(f"{total_coals - coals_collected} coals left. ({row}, {col + 1})")
    elif command[-1] == 'left':
        print(f"{total_coals - coals_collected} coals left. ({row}, {col - 1})")

















