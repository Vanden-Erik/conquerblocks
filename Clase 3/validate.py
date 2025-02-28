#This will be absolutely hideous for a validation process

nombres_usuario = ["juan123", "ana456", "pedro789"]
contraseñas = ["clave_juan", "clave_ana", "clave_pedro"] 

user = input("Username: ")
passwd = input("Password: ")

col = nombres_usuario.index(user) if user in nombres_usuario else -1

if col == -1:
    print(f"{user}, does not exist")
elif passwd == contraseñas[col]:
    print(f"Welcome, {user}!")
else:
    print("Wrong Password")