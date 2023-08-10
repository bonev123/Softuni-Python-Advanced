word = tuple(input())

unique_chars = set(word)

for char in sorted(unique_chars):
    print(f'{char}: {word.count(char)} time/s')