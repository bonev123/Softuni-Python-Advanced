from collections import deque

cups = deque([int(el) for el in input().split()])
bottles = deque([int(el) for el in input().split()])

wasted = 0

while cups and bottles:
    cup = cups.popleft()
    bottle = bottles.pop()
    if bottle >= cup:
        wasted += bottle - cup
    else:
        cups.appendleft(cup - bottle)
if not cups:
    reversed_bottles = reversed(bottles)
    print(f"Bottles: {' '.join(map(str, reversed_bottles))}")
else:
    print(f"Cups: {' '.join(map(str, cups))}")

print(f"Wasted litters of water: {wasted}")





