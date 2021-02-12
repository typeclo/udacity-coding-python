import time

print("Your grandpa told you that he hid some treasures in the forest nearby.")
time.sleep(2)
print("Today, you decided you are going to look for that treasure.")
time.sleep(2)
print("First, you want to bring tools you need to  find and dig the treasure.")
time.sleep(2)
print("In the storage you found  two bags full of tools.")
time.sleep(2)

    while True:
        response = input("Which bag will you bring? black bag or blue bag?\n").lower()
        if "black" in response:
            print("Great, Black bag, just what you need!")
            time.sleep(2)
            break
        elif "blue" in response:
            print("Well, okay, not sure what's inside. Blue bag it is.!")
            time.sleep(2)
            break
        else:
            print(" Great idea")
            time.sleep(2)
    
    print("Time to go ")
    time.sleep(2)

    print("You are walking towards the forest and you noticed two entrance.")   
    while True: # We want to loop until they enter a valid response.
        option = input("Which entrance will you choose, left or right?.\n").lower()
        if 'left' in option:
            print("Too bad you choose Left,I don't think you'll make it, I guess you must give up. Goodbye!")
            time.sleep(2)
            break # Note that this will only break out of the inner loop.
        elif 'right' in option:
            print("Very good you choose Right, I'm happy you choose this way, good to go.")
            time.sleep(2)
            break # Again, this only breaks out of the inner loop.
        else:
            print("Sorry, I don't understand.")
            time.sleep(2)
    if 'left' in option: 
        break # We need this last break statement to exit the outer loop.