#Scrivere un programma che permetta all'utente di inserire una serie di parole in input, 
# terminando l'inserimento quando viene digitata la parola "fine" (che non deve essere considerata nell'elaborazione).
#Per ogni parola inserita, il programma deve verificare se il primo e l'ultimo carattere 
#sono uguali e visualizzare un messaggio corrispondente.

#imposto il ciclo 
while True:
    parola_inserita = input("inserire una parola\n")

#se l'utente inserisce fine il ciclo chiude
    if parola_inserita == "fine":
        print("!arrivederci signore!")
        break

#controllo se la prima e l'ultima lettera coincidono o meno
    if parola_inserita[0] == parola_inserita[-1]:
        print(parola_inserita[0],parola_inserita[-1], "La parola inserita inizia e termina con la stessa lettera")
  
    else :
        print(parola_inserita[0],parola_inserita[-1], "La parola inserita inizia e termina con lettere diverse")

    
    
