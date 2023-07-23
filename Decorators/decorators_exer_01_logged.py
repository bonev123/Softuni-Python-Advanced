def logged(f):
    def wrapper(*args):
        result = f(*args)
        return f"you called {f.__name__}{args}\nit returned {result}"
    return wrapper


@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))