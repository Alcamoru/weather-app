def sq_sum(*args):
    final_sum = 0
    for number in args:
        number: int
        final_sum += number ** 2
    return final_sum
