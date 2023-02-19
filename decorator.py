
def hello(func):
    def inner():
        print("hello..")
        string = "you said hello"
        func(string)
    return inner


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


multi("a","b","c",1,2,3)

