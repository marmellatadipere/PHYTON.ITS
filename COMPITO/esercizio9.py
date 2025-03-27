
#creo una lista dei valori per cui devo approssimare
lista_obiettivi = [3.14, 3.141, 3.1415, 3.14159]

# Variabili iniziali 
segno = -1
somma_termini = 1
approssimazione = float(input("Quale e il valore minimo accettabile di tollerabilita? (inserire numero maggiore di 0)")) # valore accettabile di approssimazione

# Loop per ogni obiettivo nella lista 
for obiettivo in lista_obiettivi:
    pigreco = 0
    denominatore = 1
    segno = 1  # Iniziamo con 4/1, quindi il segno è positivo
    somma_termini = 1 # Iniziamo con 4/1 quindi inizializziamo a 1 (primo termine)

# Calcoliamo la somma della serie finché non raggiungiamo l'obiettivo, per ogni obiattivo
    while abs(pigreco - obiettivo) > approssimazione: #utilizzo il modulo per non interrompere il loop al primo giro
        pigreco += segno * (4 / denominatore)  # Aggiungi il termine alla somma partendo da 4/1
        denominatore += 2  # Aumenta il denominatore di 2
        segno *= -1  # Alterna il segno (+, -, +, ...)
        somma_termini += 1  # Conta il numero di termini 


# Output per ogni obiettivo
    print(f"Per approssimare {obiettivo}, ci sono voluti {somma_termini} termini. Valore di pi: {pigreco}")

