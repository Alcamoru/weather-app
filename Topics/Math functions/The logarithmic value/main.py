import math

first_number = int(input())
second_number = int(input())

if second_number <= 1:
    print(round(math.log(first_number)), 2)
else:
    print(round(math.log(first_number, second_number)), 2)
