#appunti lezione classe 26


                    #esercizio 1
'''
#inseire in input una frase in stringa
#stampare una stringa che equivale a quella con ogno lettera di ogni parola maiuscola
frase = input("Scrivi una frase:\n")
print(frase.title())
'''

                    #esercizio 2
'''
#stampare la frase con la prima e ultima lettera maiuscola
fraselista = []
parole = frase.split()

for parola in parole:
    if len(parola) > 1:
        parola_primaeultima_maiuscola = (parola[0].upper()) + (parola[1:-1].lower()) + (parola[-1].upper())

    else:
        parola_primaeultima_maiuscola = parola.upper()

    fraselista.append(parola_primaeultima_maiuscola)

frasefinale = " ".join(fraselista)
print(frasefinale)
'''



