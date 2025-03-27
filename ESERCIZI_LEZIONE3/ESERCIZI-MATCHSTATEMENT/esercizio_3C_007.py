'''Esercizio 3C-7. 
Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".

NOTA.
Le percentuali devono essere mostrate in output obbligatoriamente con 2 cifre decimali.
Usare il match statement.

Expected Output:

Per ciascun lancio della moneta inserisci "t" o "T" se e' uscito "testa" mentre inserisci "c" o "C" se e' uscito "croce".

'''


lanci = []


while len(lanci) < 8:
    lancio = input('Per ciascun lancio della moneta inserisci "t" o "T" se e uscito "testa" mentre inserisci "c" o "C" se e uscito "croce" ')
    
    match lancio:
        case "t":
            lanci.append(lancio.lower())
            print(f"Lancio {len(lanci)}: t")
        case "c":
            lanci.append(lancio.lower())
            print(f"Lancio {len(lanci)}: c")
        case _ :
            print("O testa o croce!")
            
    
volte_testa = lanci.count("t")
volte_croce = lanci.count("c")

percentuale_testa =  volte_testa * 100 / 8


print(f'Totale "testa": {volte_testa}\nPercentuale "testa": {percentuale_testa:.2f}%')
print(f'Totale "croce": {volte_croce}\nPercentuale "croce": {100-percentuale_testa}')  #print(f"{numero:.2f}")

