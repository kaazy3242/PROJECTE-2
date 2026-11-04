print("EXERCI 2")
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