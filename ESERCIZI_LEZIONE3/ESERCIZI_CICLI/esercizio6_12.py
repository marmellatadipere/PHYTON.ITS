'''
6-12. Extensions: 
We’re now working with examples that are complex enough that they can be extended in any number of ways. 
Use one of the example programs from this chapter, and extend it by adding new keys and values, 
changing the context of the program, or improving the formatting of the output.
'''



cane =  {"tipo": "cane", "proprietario": "Andrea", "eta": 3}
maiale =  {"tipo": "maiale", "proprietario": "Adriano" , "eta": 1}
gatto =  {"tipo": "gatto", "proprietario": "Daniele", "eta" : 6}
serpente =  {"tipo": "serpente", "proprietario": "Stefano", "eta" : 2 }
gallina =  {"tipo": "gallina", "proprietario": "Leandro", "eta" : 1 }
 

pets = [cane, maiale, gatto, serpente, gallina] #creo una lista di dizionari con chiave #tipo e valore pproprietario

for animale in pets:
    for key, valore in animale.items():  # prende in considerazione ogni coppia di key:value all'interno di un dizionario (sottoforma di tuple)
        if key == "tipo":
            tipo = valore
        elif key == "proprietario":
            proprietario = valore
        elif key == "eta":
            eta = valore
        

    print(f"Il proprietario del {tipo} di {eta} anno\i è {proprietario}")
    
