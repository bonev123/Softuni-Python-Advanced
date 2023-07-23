def even_parameters(f):
    def wrapper(*args):
        error_msg = "Please use only even numbers!"
        for arg in args:
            try:
                if not arg % 2 == 0:
                    return error_msg
            except:
                return error_msg
        return f(*args)
    return wrapper




@even_parameters
def add(a, b):
    return a + b
print(add(2, 4))
print(add("Peter", 1))