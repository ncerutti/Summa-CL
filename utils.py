import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Time elapsed: {end - start:.2f} seconds")

    return wrapper


def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        func(*args, **kwargs)

    return wrapper
