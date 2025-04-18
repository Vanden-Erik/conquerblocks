#### Arrays 1D - P1 ###
# 1. Crea un array_1 lleno ceros con una longitud de 8 elementos.
import numpy as np
from functools import reduce

array_1 = np.zeros(8)

# print(array_1)


# 2. Haz que todos los elementos de este array sean igual a 2
array_1[:] = 2

# print(array_1)

# 3. Crea un array_2 que contenga todos los números pares del 1 al 10.
array_2 = np.array(range(2,11,2))
# print(array_2)

# 4. Suma todos los elementos del array_2 usando un bucle y después usando un método de numpy. Compara los resultados
arr_2_loop_sum = 0
for i in array_2:
    arr_2_loop_sum += i

arr_2_np_sum = np.sum(array_2)

# print(arr_2_loop_sum, arr_2_np_sum)

# 5. Revierte array_2 y guárdalo en una variable independiente.
array_2_rev = array_2[::-1]

# print(array_2_rev)

# 6. Encuentra los elementos comunes entre array_1 y array_2 y entre array_2 y array_2_revertido (Pista: Investiga el uso de intersect1d() de numpy)
intersection = reduce(np.intersect1d, (array_1, array_2, array_2_rev))
# print(intersection)

# 7. Crea un arrays lleno de 1s con una longitud dada por el usuario
# ones = np.ones(int(input("Length of 1's:")))
# print(ones)


### Arrays 1D - P2 ###
# 1. Crea un array con 15 números enteros aleatorios entre 1 y 100
rng = np.random.randint(0,100,15)
print(rng)

# 2. Multiplica todos los elementos del array usando un bucle y después usando un método de numpy. Compara los resultados
# loop_multiply = 1
# for i in rng:
#     loop_multiply *= i
# print(loop_multiply)
# ---[Overflow]---

np_multiply = np.prod(rng)
# print(np_multiply)
# 3. Crea otro array con 15 números decimales aleatorios entre 0 y 1
rng2 = np.random.random(15)

print(rng2)

# 4. Suma los elementos de ambos arrays elementos por elemento. Resuélvelo usando un operador y después con una función de numpy (Pista: busca en google que función de numpy hace esto)
op_sum, func_sum = rng+rng2, np.add(rng, rng2)

# print(op_sum)
# print(func_sum)

# 5. Ahora réstalos. Resuélvelo usando un operador y después con una función de numpy (Pista: busca en google que función de numpy hace esto)
op_sub, func_sub = rng-rng2, np.subtract(rng, rng2)

# print(op_sub, func_sub)

# 6. Haz lo mismo con la multiplicación elemento por elemento. Usa un operador y después con una función de numpy (Pista: busca en google que función de numpy hace esto)
op_mult, np_mult = rng*rng2, np.multiply(rng, rng2)

# print(op_mult)
# print(np_mult)

# 7. Encuentra el valor más alto del primer array que has creado.
max = np.max(rng)
print(max)

# 8. Calcula la media (mean), la mediana (median) y al deviación estandar (standard
# deviation) de los arrays (Nota: No nos importa el significado matemático de estos
# valores, lo importante es que encuentres que función de numpy necesitas. Puedes
# hacer la búsqueda en castellano o en inglés, aunque en inglés muchas veces suele
# haber más resultados).

std, med, mean = np.std(rng), np.median(rng), np.mean(rng)

print(std)
print(mean)
print(med)