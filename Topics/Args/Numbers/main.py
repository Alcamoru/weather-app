# put your python code here
def multiply(*args):
    if len(args) == 1:
        return args[0]
    product = 1
    for i in args:
        product *= i
    return product
