def password_check():           
    while input("Password: ") != "swordfish":
        print("Wrong! Try again!")
    print("Okay, come on in")

password_check()

s = "Tenochtitlan"
index = 0 
while index < len(s):
    index += 1 
    print(s[:index])

