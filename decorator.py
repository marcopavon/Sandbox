
def hi(func):
    def inner():
        print("hi")
        func()
    return inner

def hello(func):
    def inner():
        print("hello..")
        string = "you said hello"
        func(string)
    return inner

@hi
@hello
def ciao(takeover):
    print(takeover)
    print("ciao...")

ciao()


def multi (*args):
    print(args)
    print(type(args))
    for element in args:
        print(element)


#multi("a","b","c",1,2,3)


# Decorator 1: Adds a prefix to the output
def add_prefix(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{prefix} {result}"
        return wrapper
    return decorator

# Decorator 2: Converts the output to uppercase
def to_uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

# Decorated function
@add_prefix("Hello")
@to_uppercase
def greet(name):
    return f"Hello, {name}!"

# Calling the decorated function
result = greet("Alice")
print(result)

