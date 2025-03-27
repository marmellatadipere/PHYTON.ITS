#Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall’utente.
#Il programma deve:
#acquisire una sequenza di numeri interi, terminando l’inserimento quando l’utente digita 0 (che non deve essere considerato nei calcoli);
#calcolare e visualizzare la somma di tutti i numeri pari inseriti;
#calcolare e visualizzare la media di tutti i numeri dispari inseriti;
#determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista);
#se più numeri hanno la stessa frequenza massima, visualizzarli tutti.

#mi creo le variabili
lista_numeri_inseriti = []

    # per  i pari
somma_pari = 0
totale_pari = 0
    # per i dispari
somma_dispari = 0
totale_dispari = 0

frequenzanumeri = {}  #dizionario { NUMERO INSERITO : NUMERO DI VOLTE INSERITO}

#chiedo di inserire numeri
while True:
    numero_inserito = int(input("Inserisci un numero (0 per terminare): "))  #chiedo di inserire un numero
    
    if numero_inserito == 0:         #imposto la condizione del numero negativo che termina il programma
        break   

    if numero_inserito % 2 == 0:        #controllo se il numerp inserito sia divisibile per 2 (pari)
        somma_pari += numero_inserito    #se e' pari aggiorno la somme dei numeri pari
        lista_numeri_inseriti.append(numero_inserito)   #aggiungo il numero al totale dei numeri
        totale_pari += numero_inserito

    else:
        lista_numeri_inseriti.append(numero_inserito)  #aggiungo il numero al totale dei numeri
        somma_dispari += numero_inserito       #aggiorno la somma dei dispari
        totale_dispari += 1           #aggiorno in numero di dispari inseriti (per la media)
       

for numero_inserito in lista_numeri_inseriti:        #per ogni numero inserito...

    if numero_inserito in frequenzanumeri:      #...controllo che il numero sia gia stato inserito (quindi che abbia una frequenza ALMENO 1)
        frequenzanumeri[numero_inserito] += 1           # se e' gia presente aggiorno la frequnza di +1
    else:           
        frequenzanumeri[numero_inserito] = 1    # altrimenti creo una nuova frequenza (=1) del numero inserito diverso da 0



coppia_numero_frequenza = frequenzanumeri.items() #creo una lista di tuple (numero, frequenza)

frequenza_massima = max(frequenzanumeri.values()) #trovo il numero della frequenza massima della lista di tuple

for numero_inserito, frequenza in coppia_numero_frequenza :
    if frequenza == frequenza_massima :
        print(f"Numero più frequente: {numero_inserito} ({frequenza} volte)")
        
#mando a schermo la SOMMA dei numeri pari
if totale_pari > 0:
    print(f"Somma dei numeri pari: {somma_pari}")
else:
    print("Non sono stati inseriti numeri pari")

#mando a schermo la MEDIA dei numeri DISPARI
if totale_dispari > 0: 
    print(f"Media dei numeri dispari: {somma_dispari / totale_dispari}")
else: 
    print("Non sono stati inseriti numeri dispari")
