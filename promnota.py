totalgrade = int(input("¿Cuántas notas va a ingresar en su materia? "))
grades = [] #Vector que guarda las notas ingresadas por el usuario

for i in range(totalgrade):
    grade = -1  # Valor inicial inválido
    
    while grade < 0 or grade > 5:
        try:
            grade = float(input(f"Ingrese la nota #{i+1}: "))
            
            if grade < 0 or grade > 5:
                print("La nota debe estar entre 0 y 5.")
        
        except ValueError: #dado el caso que el usuario ingrese un valor no numérico
            print("Por favor, ingrese un número válido.")
            grade = -1  # Se mantiene inválido para que repita el ciclo
    
    grades.append(grade)

print("Sus notas son:", grades)

if len(grades) > 0:
    average = sum(grades) / len(grades) #Len cuenta el número de notas ingresadas
    print("El promedio de sus notas es:", average)
else:
    print("No se ingresaron notas.")