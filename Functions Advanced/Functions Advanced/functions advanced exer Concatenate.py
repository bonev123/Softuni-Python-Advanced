def concatenate(*args):
    for string in args:
        return f''.join(args)

print(concatenate('Soft', 'Uni', 'Is', 'Great', '!'))
