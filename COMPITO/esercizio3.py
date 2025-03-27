# Acquisisco la stringa dall'utente
frase = input("Inserisci una stringa: ")

# Creo una variabile per partire dalla fine della stringa
indice = len(frase) - 1

# Inizializzo una variabile per la stringa invertita
stringa_invertita = ""

#inizializziamo l'ultima lettera (che diventera la prima in Output)
ultima_lettera = frase[indice]

# Ciclo per attraversare la stringa dalla fine all'inizio
while indice >= 0:
    stringa_invertita += frase[indice]  # Aggiungo il carattere alla nuova stringa
    indice -= 1  # Decremento l'indice per andare al carattere precedente 

# Visualizzo la stringa invertita
print(f"La stringa invertita è: {stringa_invertita}")
