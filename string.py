string = "Hello world!"
output = [] # Create empty list
index = 0
while index < len(string):
    output.append(string[index]) # Append current character
    index += 1 # Move on to next character

print(output)