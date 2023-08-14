rows, cols = [int(el) for el in input().split()]
def read_matrix():
    matrix = []
    for _ in range(rows):
        matrix.append(input().split())
    return matrix

def check_elements(row, col, matr):
    current_el = matr[row][col]
    next_el_same_row = matr[row][col+1]
    el_below = matr[row+1][col]
    el_below_next = matr[row+1][col+1]
    if current_el == next_el_same_row and current_el == el_below and current_el == el_below_next:
        return True
    return False

matrix = read_matrix()
counter = 0

for row_ind in range(rows-1):
    for col_ind in range(cols-1):
        if check_elements(row_ind, col_ind, matrix):
            counter += 1
print(counter)