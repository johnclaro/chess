from timeit import default_timer
from datetime import timedelta, datetime


def timer(function):

    def wrapper(*args, **kwargs):
        start = default_timer()
        output = function(*args, **kwargs)
        end = timedelta(seconds=default_timer() - start)
        print(f'{function.__name__} \t {end}')
        return output

    return wrapper