ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110,
140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250]
calendar = {
    "Lunes": [],
    "Martes": [],
    "Miercoles": [],
    "Jueves": [],
    "Viernes": [],
    "Sabado": [],
    "Domingo": [],
}

while len(ventas) > 0:
    for d in calendar:
        if len(ventas):
            calendar[d].append(ventas.pop(0))

best_day = ""
greatest_sale = 0
for i in calendar:
    curr = calendar[i]
    total_of_day = sum(curr)

    if total_of_day > greatest_sale:
        greatest_sale = total_of_day
        best_day = i

print(best_day, greatest_sale)