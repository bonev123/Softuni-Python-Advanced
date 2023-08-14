def valid_boundary(row, col):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False

def total_kills(matrix, row, col):
    kills = 0
    rows = [-1, -1, -2, -2, 1, 1, 2, 2]
    cols = [-2, 2, -1, 1, -2, 2, -1, 1]
    for index in range(len(rows)):
        potential_row = row + rows[index]
        potential_col = col + cols[index]
        if valid_boundary(potential_row, potential_col):
            potential_position = matrix[potential_row][potential_col]
            if potential_position == 'K':
                kills += 1
    return kills

removed = 0
n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(input()))
while True:
    killer_position = []
    max_kills = 0
    for row_index in range(n):
        for col_index in range(n):
            if matrix[row_index][col_index] == 'K':
                kills = total_kills(matrix, row_index, col_index)
                if max_kills < kills:
                    max_kills = kills
                    killer_position = [row_index, col_index]
    if killer_position:
        matrix[killer_position[0]][killer_position[1]] = '0'
        removed += 1
    else:
        break
print(removed)