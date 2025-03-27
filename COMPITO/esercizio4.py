#Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi 
# (sia interi che decimali). L'inserimento termina quando viene fornito un numero negativo, 
# che funge da sentinella e non deve essere considerato nei calcoli.
#Il programma deve:
#Calcolare la media dei soli numeri interi inseriti. 
#Utilizzate la funzione is_integer() per verificare se il numero inserito è un intero.
#Determinare e visualizzare il numero più grande e il numero più piccolo 
# tra tutti quelli inseriti (sia interi che decimali).

numeri_totali_interi_inseriti = []              #creo una lista per gli interi
numeri_totali_float_inseriti = []               #creo una lista per i float
numeri_totali_inseriti = []                     #creo una lista per tutti i numeri

sum_numeri_interi = 0                           #creo una variabile counter 

#imposto il ciclo
while True :
    numero_inserito = float(input("Inserisci un numero (negativo per terminare): "))  #chiedo di inserire un numero
    
    if numero_inserito < 0:         #imposto la condizione del numero negativo 
        break   
    
    if numero_inserito.is_integer():    #controllo se e' un numero intero
        sum_numeri_interi += numero_inserito
        numeri_totali_interi_inseriti.append(numero_inserito) #aggiungo al numero di interi totali inseriti
        numeri_totali_inseriti.append(numero_inserito) #aggiungo al totale di numeri inseriti
    
    else:   
        numeri_totali_inseriti.append(numero_inserito) #aggiungo al totale di numeri inseriti


#calcolo la media e la mando a schermo
#media_numeri_interi = len(numeri_totali_interi_inseriti) / sum_numeri_interi
media_numeri_interi = sum_numeri_interi / len(numeri_totali_interi_inseriti)

print(f"La media dei tuoi numeri e': {media_numeri_interi}")

#calcolo il numero piu grande e quello piu piccolo tra tutti quelli inseriti
numero_piu_grande = max(numeri_totali_inseriti)
numero_piu_piccolo = min(numeri_totali_inseriti)

print(f"Il numero più grande è: {numero_piu_grande}")
print(f"Il numero più piccolo è: {numero_piu_piccolo}")


