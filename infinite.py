def no_repeating():
    words = []
    while True:
        word = input("Tell me a word: ")
        if word in words:
            print("You told me that word already!")
            break
        words.append(word)
    return words

print(no_repeating())

def find_512():
    for x in range(100):
        for y in range(100):
            if x * y == 512:
    return f"{x} * {y} == 512" #break   # does not do what we want!

print(find_512())