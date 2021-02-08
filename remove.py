def remove_substring(string, substring):
    output =[]
    index = 0
    while index < len(string):
        if string[index:index+len(substring)] == substring:
            index += len(substring)
        else:
            output.append(string[index])
            index += 1
    return "".join(output)



# Here are some strings you can test your function:
#print(remove_substring('SPAM!HelloSPAM! worldSPAM!!', 'SPAM!')) 
#print(remove_substring("Whoever<br> wrote this<br> loves break<br> tags!", "<br>"))
print(remove_substring('I am NOT learning to code.', 'NOT '))