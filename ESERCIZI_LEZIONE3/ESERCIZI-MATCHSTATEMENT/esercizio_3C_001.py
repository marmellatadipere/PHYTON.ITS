'''Esercizio 3C-1. 
Scrivere un programma in Python che utilizzi un match statement per classificare un voto scolastico in base alla scala italiana.
Il programma deve accettare in input un voto numerico intero da 1 a 10 e stampare la valutazione corrispondente:

- 10 → "Eccellente"
- 8-9 → "Molto buono"
- 6-7 → "Sufficiente"
- 4-5 → "Insufficiente"
- 1-3 → "Gravemente insufficiente"
- Altro caso → "Voto non valido"
'''

voto = (input("inserire un voto:\n"))

match voto:
        case int(voto) if voto >=1 and voto <=3:
                print("Gravemente insufficiente")
        case 4|5:
                print("Insufficiente")
        case 6|7:
                print("Sufficiente")
        case 8|9:
                print("Molto buono")
        case 10 :
                print("Eccellente") 
        case int(voto) if voto > 10 :
                print("Voto non valido")
        case _ :
                print("inserite un numero")
                


        