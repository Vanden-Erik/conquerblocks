"""
Aplicar el cifrado ROT13 a un texto se reduce a examinar sus caracteres alfabéticos y sustituirlos
por la letra que está 13 posiciones por delante en el alfabeto, volviendo al principio si es necesario
y conservando las mayúsculas y minúsculas: a se convierte en n, B se convierte en O, y así hasta
la Z, que se convierte en M. Solo quedan afectadas las 26 letras principales que aparecen en el
alfabeto latino; los números, símbolos, espacios y otros caracteres se dejan igual. 
"""

string = input("String to encode: ")

def rot13(target):
    temp_ls = []
    
    for c in target:
        start=ord("A") if c.isupper() else ord("a")
        end=start+25
        if not start <= ord(c) <= end:
            temp_ls.append(ord(c))
            continue

        if c == " ":
            temp_ls.append(ord(" "))
            continue

        convert= ord(c) + 13

        if convert > end:
            convert -= 26

        temp_ls.append(convert)
        
    return "".join(chr(i) for i in temp_ls)


run1 = rot13(string)

run2 = rot13("Hello")

print(run1, run2)