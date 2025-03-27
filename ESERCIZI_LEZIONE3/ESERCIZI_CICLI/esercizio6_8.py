'''
6-8. Pets: 
Make several dictionaries, where each dictionary represents a different pet. 
In each dictionary, include the kind of animal and the owner’s name. 
Store these dictionaries in a list called pets. 
Next, loop through your list and as you do, print everything you know about each pet. 
'''


cane =  {"tipo": "cane", "proprietario": "Andrea" }
maiale =  {"tipo": "maiale", "proprietario": "Adriano" }
gatto =  {"tipo": "gatto", "proprietario": "Daniele" }
serpente =  {"tipo": "serpente", "proprietario": "Stefano" }
gallina =  {"tipo": "gallina", "proprietario": "Leandro" }


pets = [cane, maiale, gatto, serpente, gallina] #creo una lista di dizionari con chiave #tipo e valore pproprietario

for animale in pets:
    for key, valore in animale.items():  # prende in considerazione ogni coppia di key:value all'interno di un dizionario (sottoforma di tuple)
        if key == "tipo":
            tipo = valore
        elif key == "proprietario":
            proprietario = valore


    
    print(f"Il proprietario del {tipo} è {proprietario}")
    

'''for animale in pets:
    for key, valore in animale.items():  # prende in considerazione ogni coppia di key:value all'interno di un dizionario (sottoforma di tuple)
'''

        