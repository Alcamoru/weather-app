def price_string(func):
    def wrapper(arg):
        return "£" + str(func(arg))

    return wrapper


@price_string
def new_price(arg_test):
    arg_test = arg_test - (10 / 100 * arg_test)
    return arg_test
