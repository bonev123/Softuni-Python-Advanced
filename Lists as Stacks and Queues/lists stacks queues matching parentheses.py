stri = input()
stack = []

for i in range(len(stri)):
    if stri[i] == '(':
        stack.append(i)
    elif stri[i] == ')':
        start_ind = stack.pop()
        print(stri[start_ind:i + 1])