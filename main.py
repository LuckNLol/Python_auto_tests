import math
import time

def time_calculation():
    return str(math.log(int(time.time())))


seconds = time.time()
# answer = time_calculation()
print(seconds, type(seconds))
a = time_calculation()
b = float(time_calculation())
print(a, type(a))
print(b, type(b))

