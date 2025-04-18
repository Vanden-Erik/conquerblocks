gender = input("Gender (F or M): ")
name = str(input("Name: "))

if gender == "F":
    if "E" <= name[0] <= "M":
        print(f"{name} | Group A")
    else:
        print(f"{name} | Group B")
else: 
    if "A" <= name[0] <= "H" or "R" <= name[0] <= "Z":
        print(f"{name} | Group A")
    else:
        print(f"{name} | Group B")
