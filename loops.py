def count_character(string, target):
    index = 0
    total = 0
    while index < len(string):
        if string[index] == target:
            total += 1
        index += 1
    return total  
print(count_character("bonobo", "o"))

index = 0
s = "Mind the gap!"
while index < len(s) and s[index] != " ":
    index += 1
print(s[:index])
    