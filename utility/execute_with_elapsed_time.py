import time
import math
import warnings
import random

def execute_with_elapsed_time(func, **kwargs):
    start_time = time.time()
    warnings.filterwarnings("ignore")
    random.seed(10)

    func(**kwargs)

    num_sec = int(time.time() - start_time)
    num_hours = math.floor(num_sec / (60 * 60))
    num_sec = num_sec % (60 * 60)
    num_minutes = math.floor(num_sec / 60)
    num_sec = num_sec % 60
    print("Executed in ", num_hours, "hours,", num_minutes, "minutes,", num_sec, "seconds")
