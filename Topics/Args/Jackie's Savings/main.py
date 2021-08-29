def final_deposit_amount(*interest, amount=1000):
    for i, _ in enumerate(interest):
        amount *= (1 + interest[i] / 100)

    return round(amount, 2)
