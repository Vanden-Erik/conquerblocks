
initial_list = [1,2,3,3,4,5,6,7,7,8,9,10]
dupes = set([i for i in initial_list if initial_list.count(i) > 1])
not_dupes = [i for i in initial_list if not i in dupes]

print(initial_list, dupes, not_dupes)

# 2. Escribe un programa en Python para unir dos listas y ordenarlas en orden ascendente.
list1 = [1,6,3,7,9]
list2 = [2,7,1,0,3,5,3]

list3 = list1+list2
list3.sort()

print(list3)

# 3. Escribe un script que encuentre el segundo número más grande de una lista.
a = [1,2,3,4,5,6,7,8,9,10]
max1 = max2 = float('-inf')

for i in a:
    if i > max1:
        max2 = max1
        max1 = i

print(max2)

# 4. Crea un script que cuente el número de elementos más grandes que un determinado número
# dado por el usuario (supón una lista numérica).
# max1 = int(input("Min: "))
# li1 = [i+1 for i in range(50)]
# li2 = [i for i in li1 if i > max1]

# print(len(li2))

# 5. Crea un script dado un número introducido por el usuario o determinado al inicio del
# programa, realice la suma de aquellos números que sean divisibles por este.
# div = int(input("Number: "))
# print([i for i in range(1, div+1) if div % i == 0])


# 6. Escribe un script que pida un número al usuario y dada una lista encuentre el número más alto
# que es inferior al número introducido o determinado al inicio del programa.

# 7. Crea un script que extraiga los elementos comunes entre dos listas.

# 8. Crea un script que cuente el número de apariciones de un elemento de una lista en dicha lista
# (P.e. en la lista lista=[23, 65, 23] el número de apariciones de 23 es 2)

# 9. Escribe un programa que lea una lista de enteros y cree una nueva lista que contenga solo
# números positivos de la lista original.

# 10. Crea un script que tome una lista de strings y cree una nueva lista que contenga el tamaño de
# los strings de la lista original.

# 11. Crea un programa que dada una lista de strings, devuelva otra lista con los strings en
# mayúscula.