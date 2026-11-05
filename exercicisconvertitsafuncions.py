
def calcul_area_quadrat():
    print("\n--- Exercici 1: Àrea d'un quadrat ---")
    costat = float(input("Introdueix la mida del costat del quadrat: "))
    area = costat ** 2
    print(f"L'àrea del quadrat és: {area}\n")

def operacions_basiques():
    print("\n--- Exercici 2: Operacions bàsiques ---")
    num1 = int(input("Introdueix el primer nombre enter: "))
    num2 = int(input("Introdueix el segon nombre enter: "))
    print(f"Suma: {num1 + num2}")
    print(f"Resta: {num1 - num2}")
    print(f"Multiplicació: {num1 * num2}")
    if num2 != 0:
        print(f"Divisió: {num1 / num2}\n")
    else:
        print("Divisió: No es pot dividir per zero\n")

def frase_tres_paraules():
    print("\n--- Exercici 3: Frase amb 3 paraules ---")
    p1 = input("Introdueix la primera paraula: ")
    p2 = input("Introdueix la segona paraula: ")
    p3 = input("Introdueix la tercera paraula: ")
    print(f"Frase resultant: {p1} {p2} {p3}\n")

def casting_float_a_int():
    print("\n--- Exercici 4: Casting de Float a Int ---")
    f1 = float(input("Introdueix el primer nombre decimal: "))
    f2 = float(input("Introdueix el segon nombre decimal: "))
    suma_float = f1 + f2
    resultat_int = int(suma_float)
    print(f"Suma decimal (float): {suma_float}")
    print(f"Suma convertida a enter (int): {resultat_int}\n")

def comprovar_majoria_edat():
    print("\n--- Exercici 5: Majoria d'edat ---")
    edat = int(input("Introdueix la teva edat: "))
    if edat >= 18:
        print("Ets major d'edat\n")
    else:
        print("Ets menor d'edat\n")

def trobar_major_de_tres():
    print("\n--- Exercici 6: El nombre més gran de tres ---")
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

def comprovar_positiu_negatiu():
    print("\n--- Exercici 7: Positiu o Negatiu ---")
    num = float(input("Introdueix un nombre: "))
    if num >= 0:
        print("El nombre és positiu\n")
    else:
        print("El nombre és negatiu\n")
def mostrar_parells_1_200():
    print("\n--- Exercici 8: Nombres parells de 1 a 200 ---")
    for i in range(2, 201, 2):
        print(i, end=" ")
    print("\n")

def cercar_nota_deu():
    print("\n--- Exercici 9: Cerca d'un 10 en la seqüència ---")
    te_deu = False
    nota = float(input("Introdueix una nota (0-10) o -1 per acabar: "))
    while nota != -1:
        if nota == 10:
            te_deu = True
        nota = float(input("Introdueix una nota (0-10) o -1 per acabar: "))
    
    if te_deu:
        print("Hi ha hagut alguna nota que té un 10\n")
    else:
        print("No hi ha cap 10\n")

def cercar_nombres_negatius():
    print("\n--- Exercici 10: Cerca de negatius en 10 nombres ---")
    te_negatiu = False
    for i in range(1, 11):
        num = float(input(f"Introdueix el nombre {i} de 10: "))
        if num < 0:
            te_negatiu = True
            
    if te_negatiu:
        print("Hi havia almenys un nombre negatiu\n")
    else:
        print("No hi ha cap nombre negatiu\n")


