# 1st Exercise

# stars = int(input("How many stars in the middle? "))

# for i in range(1, stars+1, 1):
#     print("*"*i)

# for i in range(stars-1,0,-1):
#     print("*"*i)

# 2nd Exercise
# password = "contraseña"
# guess = ""

# print("Insert password: ")
# while not guess == password:
#     guess = input()
#     if not guess == password:
#         print("Wrong Password")
#     else print("Welcome")

# 3rd Exercise
# for i in [i for i in input("Word: ")][::-1]:
#     print(i)

# 4th
phrase = input("Phrase? ")
letter = input("Letter? ")

print(len([i for i in phrase if i == letter]))