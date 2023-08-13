n = int(input())

matrix = []
position = None

for row in range(n):
    matrix.append(list(input()))
symbol = input()

for row in range(n):
    for col in range(n):
        if matrix[row][col] == symbol:
            position = row, col
            break
    if position:
        print(position)
        break

if not position:
    print(f"{symbol} does not occur in the matrix")

