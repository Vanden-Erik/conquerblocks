"""
Trabajas en colegio y estas encargado de mantener un seguimiento de las notas de los
estudiantes de un clase. En tu base de datos tienes una lista con los nombres de los estudiantes y
para cada estudiante debes guardar sus notas provenientes de deberes, exámenes y proyectos.
También necesitas calcular a nota media de cada estudiante y la nota media de la clase al
completo.
Pista: Para resolver este problema puedes usar una lista anidada donde guardes las notas para
cada estudiante. Entonces puedes usar un bucle para recorrer la lista de listas y calcular la nota
media de cada estudiante. También puedes usar otro bucle para calcular la nota media de toda la
clase. 
"""

avg_notes_for_class = 0
students = {
    "s1": {
        "notes": [10, 10, 9, 9, 10, 9],
        "avg_notes": 0
    },
    "s2": {
        "notes": [10, 10, 9, 8, 10, 9],
        "avg_notes": 0
    },
    "s3": {
        "notes": [8, 6, 7, 9, 6, 7, 7],
        "avg_notes": 0
    },
    "s4": {
        "notes": [5, 1, 5, 3, 6, 2, 6],
        "avg_notes": 0
    },
    "s5": {
        "notes": [4, 2, 3, 5, 5, 3, 4, 2],
        "avg_notes": 0
    },
}

for i in students:
    student=students[i]
    notes=0
    for note in student["notes"]:
       notes+=note
    
    student["avg_notes"] = round(notes / len(student["notes"]))
    print(f"Average notes for {i}: {student["avg_notes"]}")


avg_notes_for_class = round(sum([students[i]["avg_notes"] for i in students]) / len(students))

print(f"\nClass' average notes: {avg_notes_for_class}")