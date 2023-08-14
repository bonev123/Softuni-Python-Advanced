rows, cols = [int(el) for el in input().split()]

matrix = []
for _ in range(rows):
    matrix.append([])
    for _ in range(cols):
        matrix[-1].append('')

text = input()
text_index = 0
col = 0
for row in range(rows):
    if row % 2 == 0:
        dir = 1
    else:
        dir = -1
    while 0 <= col < cols:
        matrix[row][col] = text[text_index]
        if text_index + 1 == len(text):
            text_index = -1
        text_index += 1
        col += dir
    col -= dir

for i in range(len(matrix)):
    print(''.join(matrix[i]))



