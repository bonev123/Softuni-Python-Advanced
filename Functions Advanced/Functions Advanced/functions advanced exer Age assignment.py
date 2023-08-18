def age_assignment(*args, **kwargs):
    dictio = {name: 0 for name in args}

    for letter,age in kwargs.items():
        for name in dictio:
            if name.startswith(letter):
                dictio[name] = age
    return dictio


print(age_assignment('Peter', 'George', G=26, P=19))