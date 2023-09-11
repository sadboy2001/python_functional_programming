from datetime import datetime
from time import sleep


def time_logger(f):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = f(*args, **kwargs)
        print(f"Function '{f.__name__}' execution time is {(datetime.now() - start).seconds} sec.")
        return result

    return wrapper


@time_logger
def func_add(x: int, y: int):
    return x + y


@time_logger
def complex_calc(x: int, y: int):
    sleep(2)
    return x + y


print(func_add(2, 4))
print(complex_calc(2, 4))