#Esercizio 6
#Scrivere un programma che acquisisca in input due numeri interi, n1 e n2, 
# e calcoli il prodotto di tutti i numeri compresi tra n1 e n2, inclusi gli estremi.
#Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque il prodotto correttamente.

numero1 = int(input("Spara un numero amico:\n"))
numero2 = int(input("Sparane un altro:\n") )
prodotto = 1

if numero1 > numero2:   
    while numero1 >= numero2:
        prodotto *= numero2 
        numero2 += 1
    else:
        print(f"Il prodotto di tutti i numeri compresi tra i due numeri e' {prodotto}:\n")

elif numero2 > numero1:
    while numero2 >= numero1:
        prodotto *= numero1
        numero1 += 1
    else:
        print(f"Il prodotto dei tuoi numeri e' \n{prodotto}")

elif numero1 == numero2 :
    print("Scrivi due numeri diversi altrimenti che gusto c'e'!")


