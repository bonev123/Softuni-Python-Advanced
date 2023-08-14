rows, cols = [int(el) for el in input().split()]

matrix = []
matrix_best = []
max_so_far = None

for _ in range(rows):
    matrix.append([int(el) for el in input().split()])
for row in range(rows-2):
    for col in range(cols-2):
        first_row = matrix[row][col], matrix[row][col+1], matrix[row][col+2]
        second_row = matrix[row+1][col], matrix[row+1][col+1], matrix[row+1][col+2]
        third_row = matrix[row+2][col], matrix[row+2][col+1], matrix[row+2][col+2]
        current_max = sum(first_row) + sum(second_row) + sum(third_row)
        if max_so_far == None or current_max > max_so_far:
            max_so_far = current_max
            matrix_best = [first_row, second_row, third_row]
print(f"Sum = {max_so_far}")
for row in matrix_best:
    print(f" ".join([str(x) for x in row]))


