squared = 0 #global variable

def demo_f(x):
    squared = x * x  #local variable
    return squared

squared = demo_f(2)

print(squared)