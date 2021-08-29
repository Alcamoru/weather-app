def morning(func):
    def wrapper(args):
        func(args)
        print(f"Good morning, {args}")
    return wrapper


@morning
def greetings(name):
    print('Hello,', name)
