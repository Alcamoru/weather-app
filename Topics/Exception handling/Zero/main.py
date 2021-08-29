n = int(input())
denominator = int(input())

if not denominator:
    print("Division by zero is not supported")
else:
    print(n // denominator)
