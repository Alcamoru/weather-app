user_input = input()
all_words = user_input.lower().split()

count = dict()

for i in all_words:
    if i in count.keys():
        count[i] += 1
    else:
        count[i] = 1

for obj in count.items():
    print(f"{obj[0]} {obj[1]}")
