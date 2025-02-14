password = input("Password: ")

if not "*" in password and not "#" in password:
    print("Password should contain at least 1 of * and # characters")
elif "a" in password or "e" in password or "i" in password or "o" in password or "u" in password:
    print("Logged in")
else: print("No lowercase vowel in password")
