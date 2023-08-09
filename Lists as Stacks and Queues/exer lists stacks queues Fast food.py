from collections import deque

food_quantity = int(input())

order_queue = deque([int(x) for x in input().split()])
max_order = max(order_queue)

for i in range(len(order_queue)):
    order = order_queue.popleft()
    if order <= food_quantity:
        food_quantity -= order
    else:
        order_queue.appendleft(order)
        break
print(max_order)
if len(order_queue) == 0:
    print(f"Orders complete")
else:
    print(f"Orders left:",' '.join([str(order) for order in order_queue]))



