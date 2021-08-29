exception_index = int(input())

all_exception = dir(locals()['__builtins__'])

print(all_exception[exception_index])
