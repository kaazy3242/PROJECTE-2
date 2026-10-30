print("EXERCI 2")
num1 = int(input("Introdueix el primer nombre enter: "))
num2 = int(input("Introdueix el segon nombre enter: "))

print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicació: {num1 * num2}")
if num2 != 0:
    print(f"Divisió: {num1 / num2}\n")
else:
    print("Divisió: No es pot dividir per zero\n")