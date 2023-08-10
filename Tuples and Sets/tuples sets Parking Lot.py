n = int(input())
parking = set()

for _ in range(n):
    direction, reg = input().split(', ')
    if direction == 'IN':
        parking.add(reg)
    elif direction == 'OUT':
        parking.remove(reg)

if parking:
    print('\n'.join(parking))
else:
    print('Parking Lot is Empty')