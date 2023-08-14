from sys import maxsize

SQUARE_SIZE = 3


def read_current_square(the_matrix, row_idx, col_idx, square_size=SQUARE_SIZE):
    square = []
    for num in range(square_size):
        square.append(the_matrix[row_idx + num][col_idx:col_idx + square_size])
    return square


def calculate_current_square_sum(square):
    total_square_sum = 0
    for current_row in square:
        total_square_sum += sum(current_row)
    return total_square_sum


matrix = []

(rows, cols) = map(int, input().split())

for _ in range(rows):
    matrix.append(list(map(int, input().split())))

max_square_sum = -maxsize
square_with_max_sum = None

for row_index in range(rows - SQUARE_SIZE + 1):
    for col_index in range(cols - SQUARE_SIZE + 1):
        current_square = read_current_square(matrix, row_index, col_index)
        current_square_sum = calculate_current_square_sum(current_square)
        if current_square_sum > max_square_sum:
            max_square_sum = current_square_sum
            square_with_max_sum = current_square

print(f"Sum = {max_square_sum}")
[print(*row, sep=" ") for row in square_with_max_sum]
