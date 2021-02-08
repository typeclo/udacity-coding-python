def is_substring(substring, string): # Write your code here
    index = 0
    while index < len(string):
        if string[index : index + len(substring)] == substring:
            return True
        index += 1
    return False
# Below are some calls you can use to test it

# This one should return False
print(is_substring('bad', 'abracadabra'))

# This one should return True
print(is_substring('dab', 'abracadabra'))

