print(f"Debug: system is being debugged")
print(f"-------------------------------")

print(f"Debug: system is being debugged")
print(f"???????????????????????????????")

print(f"Debug: system is being error")
print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


def separate_log():






@separate_log(level, symbol)
def print_log(level, log_m):
    print(f"{level}: {log_m}")

def repeat(func):
    def wrapper(repeat_number):
        func() * repeat_number
    return wrapper(func)

@repeat
def message():
    print("Important message")

message(3)
