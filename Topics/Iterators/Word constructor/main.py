a = input()
b = input()

zipped_gen = zip(a, b)

word = ""

for i in zipped_gen:
    for j in i:
        word += j

print(word)
