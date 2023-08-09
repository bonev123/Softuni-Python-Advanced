box = []
for clothing in input().split():
    box.append(int(clothing))
rack_capacity = int(input())

current_rack_weight = 0
racks_used = 1


for i in range(len(box)):
    current_clothing = box.pop()
    if current_clothing + current_rack_weight > rack_capacity:
        racks_used += 1
        current_rack_weight = 0
    current_rack_weight += current_clothing
print(racks_used)


