import time
from datetime import datetime


def decorator(func):
    def wrapper():
        hour = datetime.now().hour
        if 6 < hour < 14:
            func()  # Call the original function (morning)
        else:
            print("Not Morning!")

    return wrapper  # Ensure the decorator returns the wrapper function


@decorator
def morning():
    print("Good Morning!")


morning()


def decorator(func):
    def wrapper():
        counting_min = datetime.now().minute
        counting_hour = datetime.now().hour
        if 0 < counting_hour < 12:
            func(counting_min, counting_hour, "am")  # Call the original function (morning)
        else:
            func(counting_min, counting_hour, "pm")

    return wrapper  # Ensure the decorator returns the wrapper function


@decorator
def timer(counting_min, counting_hour, ampm):
    print(f"It is {counting_hour}:{counting_min}{ampm} now")


timer()


def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        run_time = end_time - start_time
        print(f"It took {run_time: .4f} to finish run {func.__name__}")
    return wrapper()


@timer
def morning():
    time.sleep(2)
    print("Good Morning!")


morning = timer(morning)
morning()




