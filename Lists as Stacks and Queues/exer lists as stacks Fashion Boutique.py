clothes = list(map(int, input().split()))
capacity = int(input())

counter = 1
current_capacity = capacity
while len(clothes) > 0:
    current_clothes = clothes.pop()
    if current_clothes <= current_capacity:
        current_capacity -= current_clothes
    else:
        counter += 1
        current_capacity = capacity
        current_capacity -= current_clothes
print(counter)



