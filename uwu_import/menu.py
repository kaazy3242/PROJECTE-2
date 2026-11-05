
from uwu_import.exercicisconvertitsafuncions import *

def mostrar_menu():
    print("           MENÚ PRINCIPAL D'EXERCICIS"          )
    print(" 1. Càlcul de l'àrea d'un quadrat")
    print(" 2. Operacions bàsiques amb dos enters")
    print(" 3. Frase amb 3 paraules")
    print(" 4. Casting de Float a Int")
    print(" 5. Comprovar majoria d'edat")
    print(" 6. Trobar el nombre més gran de tres")
    print(" 7. Comprovar si un nombre és positiu o negatiu")
    print(" 8. Mostrar nombres parells de 1 a 200")
    print(" 9. Comprovar si hi ha alguna nota igual a 10")
    print("10. Comprovar si hi ha nombres negatius")
    print(" S. Sortir del programa")
    

def main():
    while True:
        mostrar_menu()
        opcio = input("Tria una opció: ").strip().upper()

        if opcio == "1":
            calcul_area_quadrat()
        elif opcio == "2":
            operacions_basiques()
        elif opcio == "3":
            frase_tres_paraules()
        elif opcio == "4":
            casting_float_a_int()
        elif opcio == "5":
            comprovar_majoria_edat()
        elif opcio == "6":
            trobar_major_de_tres()
        elif opcio == "7":
            comprovar_positiu_negatiu()
        elif opcio == "8":
            mostrar_parells_1_200()
        elif opcio == "9":
            cercar_nota_deu()
        elif opcio == "10":
            cercar_nombres_negatius()
        elif opcio == "S":
            print("\nHas sortit del programa.")
            break
        else:
            print("\n[ERROR] Opció no vàlida. Torna a intentar-ho.\n")

if __name__ == "__main__":
    main()