import time

def measure_time(func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    return result, end - start

def fast(): return sum(range(10))
def slow(): time.sleep(0.5); return "done"
def power(x, y): return x ** y

print(measure_time(fast))
print(measure_time(slow))
print(measure_time(power, 2, 10))
