print("EXERCI 3")
te_negatiu = False

for i in range(1, 11):
    num = float(input(f"Introdueix el nombre {i} de 10: "))
    if num < 0:
        te_negatiu = True

if te_negatiu:
    print("Hi havia almenys un nombre negatiu\n")
else:
    print("No hi ha cap nombre negatiu\n")