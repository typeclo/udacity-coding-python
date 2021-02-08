def replace_substring(string, substring, replacement):
    output = []
    index = 0
    while index < len(string):
        if string[index:index+len(substring)] == substring:
            output.append(substring)
            index += len(substring)
        else:
            output.append(string[index])
            index += 1
    return "".join(output)

# Here are some examples you can test it with:
print(replace_substring('Hot SPAM!drop soup, and curry with SPAM!plant.', 'SPAM!', 'egg'))
print(replace_substring("The word 'definately' is definately often misspelled.", 'definately', 'definitely'))