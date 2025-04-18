numeros = [1,2,3,4,5,6,7,8,9,10]
pares = [i for i in numeros if not i % 2][::-1]
potencias = [i**2 for i in numeros]

loop_sum = 0
for i in numeros:
    loop_sum += i

normal_sum = sum(numeros)


print(f"""
numeros: {numeros}
pares: {pares}
potencias: {potencias}
minmax: {min(numeros), max(numeros)}
sums: {loop_sum, normal_sum}
indexes: {numeros.index(8), pares.index(8)}
""")