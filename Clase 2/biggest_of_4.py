num1 = input("Insert 4 or more numbers, separated by commas: ")

li = [int(i) for i in num1.split(",")]

print(max(li))