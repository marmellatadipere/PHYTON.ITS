'''Esercizio 3C-2. 
Scrivere un programma in Python che converta un voto di laurea italiano (sistema in 110-emi) nel sistema GPA americano (scala 0-4).
Il programma deve accettare in input un voto di laurea compreso tra 66 e 110, espresso come numero intero e usare un match per determinare il corrispondente GPA americano, secondo questa tabella di conversione:

- 106-110 → 4.0
- 101-105 → 3.7
- 96-100 → 3.3
- 91-95 → 3.0
- 86-90 → 2.7
- 81-85 → 2.3
- 76-80 → 2.0
- 70-75 → 1.7
- 66-69 → 1.0
- Altro caso → "Voto non valido"
'''
da106110 = 4.0
da101105 = 3.7
da96100 = 3.3
da9195 = 3.0
da8690 = 2.7
da8185 = 2.3
da7680 = 2.0
da7075 = 2.0
da6669 = 1.0

voto:int = int(input("inserire un voto tra 66 e 110\n"))


match int(voto):
    case voto if voto >= 66 and voto <= 69:
        print(f"il tuo voto corrisponde a {da6669} ")
    case voto if voto >= 70 and voto <= 75:
        print(f"il tuo voto corrisponde a {da7075} ")
    case voto if voto >= 76 and voto <= 80:
        print(f"il tuo voto corrisponde a {da7680} ")
    case voto if voto >= 81 and voto <= 85:
        print(f"il tuo voto corrisponde a {da8185} ")
    case voto if voto >= 86 and voto <= 90:
        print(f"il tuo voto corrisponde a {da8690} ")
    case voto if voto >= 91 and voto <= 95:
        print(f"il tuo voto corrisponde a {da9195} ")
    case voto if voto >= 96 and voto <= 100:
        print(f"il tuo voto corrisponde a {da96100} ")
    case voto if voto >= 101 and voto <= 105:
        print(f"il tuo voto corrisponde a {da101105} ")
    case voto if voto >= 106 and voto <= 110:
        print(f"il tuo voto corrisponde a {da106110} ")
    case _ :
        print(" Voto non valido")
    








    
    
   
