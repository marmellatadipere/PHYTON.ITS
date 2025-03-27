#Scrivere un programma che acquisisca una stringa inserita dall'utente 
# e calcoli il numero totale di spazi presenti nella stringa. 
# Il risultato deve essere visualizzato in output.

#chiedo all' utente di inserire una parola
frase = input("A cosa stai pensando?: \n")

#controllo se e quante volte lo spazio e' nella frase
if " " in frase:
    numero_spazi = frase.count(" ")
    print(f"il numero di spazi nella frase inserita e': {numero_spazi}\n")