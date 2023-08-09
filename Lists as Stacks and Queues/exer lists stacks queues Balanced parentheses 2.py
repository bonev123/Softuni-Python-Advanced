expression = input()

stack = []

for par in expression:
    if par == '{' or par == '[' or par == '(':
        stack.append(par)
