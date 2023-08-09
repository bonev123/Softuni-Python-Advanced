from collections import deque
from datetime import datetime, timedelta

data = input().split(';')
time = datetime.strptime(input(), '%H:%M:%S')

robots = []
products = []
avail_robots = deque([])

for el in data:
    robot_data = el.split('-')
    robot = {}
    robot['name'] = robot_data[0]
    robot['processing_time'] = int(robot_data[1])
    robot['available_at'] = time
    robots.append(robot)
    avail_robots.append(robot)

product = input()
avail_robots = deque(avail_robots)

while not product == 'End':
    products.append(product)
    product = input()
products = deque(products)
time = time + timedelta(seconds=1)

while len(products) > 0:
    current_product = products.popleft()
    if avail_robots:
        current_robot = avail_robots.popleft()
        current_robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
        robot = [el for el in robots if el == current_robot][0]
        print(f"{current_robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    else:
        for r in robots:
            if time >= r['available_at']:
                avail_robots.append(r)
        if not avail_robots:
            products.append(current_product)
        else:
            current_robot = avail_robots.popleft()
            current_robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
            robot = [el for el in robots if el == current_robot][0]
            print(f"{current_robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    time = time + timedelta(seconds=1)



        


