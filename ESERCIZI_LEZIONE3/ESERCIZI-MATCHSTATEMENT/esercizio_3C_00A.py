#ESERCIZIO 3C-00A
#Esercizio 3C-00A. Scrivere un programma in Python che richieda all'utente di inserire un numero intero rappresentante il numero di neonati e utilizzi lo statement match per fornire una risposta appropriata:


numero_neonati = int(input("Quanti sono i neonati?:\n"))

# if numero_neonati.isnumeric() and numero_neonati > 0:
match numero_neonati:
    case 1:
        print("Congratulazioni!")
    case 2:
        print("Wow! Gemelli!")
    case 3:
        print("Wow! Tre!")
    case 4:
        print("Mamma mia Quattro! Wow!")
    case 5:
        "Incredibile! Cinque!"
    case _ :
        print(f"Non ci credo! {numero_neonati} bambini!")





