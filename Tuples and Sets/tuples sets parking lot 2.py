n = int(input())

cars = set()

for _ in range(n):
    direction, number = input().split(', ')
    if direction == 'IN':
        cars.add(number)
    else:
        if number in cars:
            cars.remove(number)
if not cars:
    print(f"Parking Lot is Empty")
else:
    [print(car) for car in cars]

