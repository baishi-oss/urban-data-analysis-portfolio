import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_ms = (time.perf_counter() - start) * 1000
        print(f"function {func.__name__} runs in {elapsed_ms:.2f}ms")
        return result

    return wrapper

@timer
def calculate(a, b):
    time.sleep(0.5)
    return a + b


if __name__ == "__main__":
    print(calculate(5, 10))
    print(calculate.__name__)
