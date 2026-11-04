print("EXERCI 2")
num1 = float(input("Introdueix el primer nombre: "))
num2 = float(input("Introdueix el segon nombre: "))
num3 = float(input("Introdueix el tercer nombre: "))

if num1 >= num2 and num1 >= num3:
    major = num1
elif num2 >= num3:
    major = num2
else:
    major = num3

print(f"El nombre més gran és: {major}\n")