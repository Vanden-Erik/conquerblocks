users = ["Alejandro", "Naomi", "Sergio"]

user_name = input("Username: ").title()
user_name.replace(".","")
user_name.replace("#","")

if user_name in users:
    print(f"Hello, {user_name}! Welcome back!")
else:
    print(f"What are you, {user_name}? A mouse or a horse?")