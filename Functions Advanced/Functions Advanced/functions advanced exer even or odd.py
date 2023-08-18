def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return not num % 2 == 0

def even_odd(*args):
    command = args[-1]
    nums = args[:-1]
    if command == 'even':
        return list(filter(is_even, nums))
    elif command == 'odd':
        return list(filter(is_odd, nums))
print(even_odd(1, 2, 3, 4, 5, 6, 'even'))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'odd'))