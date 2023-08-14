n = int(input())

matrix = []
prim_dia = 0
second_dia = 0
col = n-1
for _ in range(n):
    nums = [int(el) for el in input().split()]
    matrix.append(nums)
for row in range(n):
    prim_dia += matrix[row][row]
    second_dia += matrix[row][col]
    col -= 1

diff = abs(prim_dia - second_dia)
print(diff)


