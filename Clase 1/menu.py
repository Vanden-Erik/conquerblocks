import re

menu = [
	{"name": "Ensalada Mixta"		,"price": 12.0,"cty": 0},
	{"name": "Sopa de Pescado"		,"price": 10.0,"cty": 0},
	{"name": "Dorada al horno"		,"price": 18.0,"cty": 0},
	{"name": "Arroz al curry"		,"price": 14.0,"cty": 0},
	{"name": "Lasagna de carne"		,"price": 15.0,"cty": 0},
	{"name": "Brownie de Chocolate"	,"price": 8.0, "cty": 0},
	{"name": "Helado"				,"price": 6.0, "cty": 0},
	{"name": "Refrescos"			,"price": 5.5, "cty": 0},
	{"name": "Cafe"					,"price": 3.5, "cty": 0},
]

def print_menu():
	for i, item in enumerate(menu):
		print(f"[{i}] {item["name"]}: {item["price"]}")

def query(): # Request user input for every 
	for item in menu:
		item["cty"] = int(input(f"{item["name"]}? #") or 0)

def calculate_total(total=0):
	for i in menu:
		total += i["price"] * i["cty"]
	return total

print_menu()
query()

print(calculate_total())