from collections import deque
n = int(input())

stations = deque([])

for _ in range(n):
    stations.append(input())

for big_circle in range(n):
    is_enough = True
    petrol_sum = 0
    for small_circle in range(n):
        current_station = stations[small_circle]
        petrol, distance = current_station.split()
        petrol = int(petrol)
        distance = int(distance)
        petrol_sum += petrol - distance
        if petrol_sum < 0:
            stations.append(stations.popleft())
            is_enough = False
            break
    if is_enough:
        print(big_circle)
        break



