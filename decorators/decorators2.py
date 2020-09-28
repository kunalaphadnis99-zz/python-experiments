from time import time


def performance_tracker(fn):
    def wrapper(*args, **kwargs):
        print(f'PERFORMANCE TRACKER :: Executing function: {fn.__name__}')
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f'PERFORMANCE TRACKER :: Executed function: {fn.__name__} in secs: {(end_time - start_time)}')
        return result

    return wrapper
