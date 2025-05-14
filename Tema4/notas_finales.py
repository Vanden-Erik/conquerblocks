"""
    ---[Final Grade Calc]---
    Scope: Each student has 4 factors that influence their grade
    - 2 Tests, 30% each
    - 1 Final, 30%
    - Class participation: 10%

    In Numpy:
    Each grade gets a row for a total of 4 rows
    Each student gets a column.

    
"""
import numpy as np

print("""
Name each student or leave empty to finish step
""")

# Receive students. I decide to overengineer this and make it an infinite input
students = np.array(["Sophia", "Milianne", "Thomas"])

# while True:
#     uInput = input(f"Name student {students.size + 1}: ")

#     if uInput:
#         students = np.append(students, uInput.title())
#     else:
#         break


# Create the grades table dynamically, based on amount of students and grades and populate randomly

grade_names = np.array(["T1", "T2", "F", "P"])
grades = np.random.randint(10, size=(students.size, grade_names.size))

test1 = grades[:,0]*0.3
test2 = grades[:,1]*0.3
final = grades[:,2]*0.3
participation = grades[:,3]*0.1

totals = np.ceil(test1+test2+final+participation).astype(np.int64)

for i, n in enumerate(students):
    print(f"""
    ---[{n}]---
    Test 1 (30%)        > {grades[i,0]}
    Test 2 (30%)        > {grades[i,1]}
    Final (30%)         > {grades[i,2]}
    Participation (10%) > {grades[i,3]}
    
    ---[Total: {totals[i]}]---
    """)
    
