def count_substring(string, target):
    total = 0
    index = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            total += 1
            index += len(target)   # <- This is the key line
        else:
            index += 1
    return total

print(count_substring('AAAA', 'AA'))

def locate_first(string, sub):
    index = 0
    while index < len(string):
        if string[index : index + len(sub)] == sub:
            return index
        else:
            index += 1
    return -1

# Here are a couple function calls to test with.

# This one should return 1
# print(locate_first('cookbook', 'ook'))

# This one should return -1
print(locate_first('all your bass are belong to us', 'base'))
-1

def locate_all(string, sub):
    index = 0
    matches =[]
    while index < len(string):
        if string[index : index + len(sub)] == sub:
            matches.apend(index)
            index = len(sub)
        else:
            index += 1
    return matches

# Here are a couple function calls to test with.

# This one should return 1
# print(locate_first('cookbook', 'ook'))

# This one should return -1
print(locate_all('all your bass are belong to us', 'base'))
-1
