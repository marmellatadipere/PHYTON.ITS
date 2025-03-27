#Un'applicazione interessante dei computer è la rappresentazione grafica di dati.
#Scrivere un programma che acquisisca cinque numeri interi 
# (ognuno compreso tra 1 e 30) e visualizzi in output un grafico a barre testuale con asterischi *.
#Per ogni numero letto, il programma deve stampare una riga contenente tanti asterischi quanti
#il valore del numero stesso.

#chiedo in input 5 valori interi
numero1= int(input("Dammi il numero 1 su 5\n"))
numero2= int(input("Dammi il numero 2 su 5\n"))
numero3= int(input("Dammi il numero 3 su 5\n"))
numero4 = int(input("Dammi il numero 4 su 5\n"))
numero5 = int(input("Dammi il numero 5 su 5\n"))

#inizializzo counter di asterischi che dovro mandare a schermo
asterischi_counter = 0

#stampo la riga numero 1 di 5
if numero1 > 0 and numero1 < 31 :
        print(numero1 * "*")
else:
    print("Riga 1: Numero inserito fuori Range")

#stampo la riga numero 2 di 5
if numero2 > 0 and numero2 < 31 :
        print(numero2 * "*")
else:
    print("Riga 2: Numero inserito fuori Range")

#stampo la riga numero 3 di 5
if numero3 > 0 and numero3 < 31 :
        print(numero3 * "*")
else:
    print("Riga 3: Numero inserito fuori Range")

#stampo la riga numero 4 di 5
if numero4 > 0 and numero4 < 31 :
        print(numero4 * "*")

#stampo la riga numero 5 di 5
if numero5 > 0 and numero5 < 31 :
        print(numero5 * "*")
else:
    print("Riga 5: Numero inserito fuori Range")


