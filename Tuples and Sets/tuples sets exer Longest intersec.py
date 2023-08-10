n = int(input())

longest = None

for _ in range(n):
    first_line, second_line = input().split('-')

    first_line = first_line.split(',')
    second_line = second_line.split(',')

    first_line = (int(first_line[0]), int(first_line[1]))
    second_line = (int(second_line[0]), int(second_line[1]))

    near_point = max(first_line[0], second_line[0])
    far_point = min(second_line[1], first_line[1])
    current_intersec = far_point - near_point + 1
    if longest == None or current_intersec > len(longest):
        longest = list(range(near_point, far_point + 1))
print(f"Longest intersection is {longest} with length {len(longest)}")