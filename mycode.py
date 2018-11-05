import math

def f(x):
    """Add a new comment"""
    return 5*x*x + 1

def g(x):
    """The greatest function ever"""
    return -x

def h(x):
    return math.sin(x)


if __name__ == "__main__":
    print(g(f(2)))
    print(h(1))
    print("Hello world")
