n = int(input())

matrix = []

for _ in range(n):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)

col = n - 1
first_dia = 0
second_dia = 0

for index in range(n):
    first_dia += matrix[index][index]
    second_dia += matrix[index][col]
    col -= 1

print(abs(first_dia - second_dia))
