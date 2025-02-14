cars = {
    "RBM S1":{
        "price": 20000,
        "commision": 0.03
    },
    "RBM S+":{
        "price":35000,
        "commision": 0.05
    },
    "RBM Ranger":{
        "price": 60000,
        "commision": 0.07
    }
}

returns = 0
for car in cars:
    cars[car]["sold"] = int(input(f"{car} - units sold: "))
    unit = cars[car]

    returns += unit["sold"] * (unit["price"] * unit["commision"])

print(f"Returns: {returns}EUR")