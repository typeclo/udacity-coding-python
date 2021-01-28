def starts_with(s1, s2):
    if s1[0] == s2[0]:
        return True
    else:
        return False
    # Add your function definition here

# A call like this should return True:
print(starts_with("banana", "bread"))

# And one like this should return False:
print(starts_with("zebonkey", "kiwi"))

def starts_with(long, short):
    for position in range (len(short)):
        if long[position] != short[position]:
            return False
        else:
            return True
        # Write your function definition here.

# A call like this should return True:
print(starts_with("apple", "app"))

# And one like this should return False:
print(starts_with("manatee", "mango"))

def starts_with (long, short):
    if long[0:len(short)] == short:
        return True
    else:
        return False# Write your function definition here.

# A call like this should return True:
print(starts_with("apple", "app"))

# And one like this should return False:
print(starts_with("manatee", "mango"))

def starts_with(long, short):
    return long[0:len(short)] == short

print(starts_with("apple", "app"))

# And one like this should return False:
print(starts_with("manatee", "mango"))
