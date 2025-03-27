'''Esercizio 3C-6. 
Scrivere un codice python che consenta all'utente di inserire il nome di un animale ed un habitat. 
Quando il codice dell'esercizo 3C-4 classifica l'animale inserito in una delle categorie tra 
    mammiferi, rettili, uccelli o pesci, oltre a mostrare un messaggio a schermo,
    deve salvare tale categoria in una variabile animal_type. 
    Se l'animale inserito non è classificabile in una delle quattro categorie proposte, 
    il valore di animal_type sarà ' "unknown".

Inserire, poi, in un dizionario il nome dell'animale, la categoria a cui esso appartiene (animal_type) e l'habitat.

Verificare con un match statement se l'animale e la categoria a cui esso appartiene possano vivere nell'habitat inserito; dunque, verificare:
- se l'animale può vivere nell'habitat specificato, stampare un messaggio appropriato.
- se l'habitat non è compatibile con l'habitat specificato, stampare un avviso.
- Se l'animale o l'habitat non sono riconosciuti, stampare un messaggio di errore.


NOTA.
Il codice deve produrre un risultato sensato, ovvero che l'animale inserito possa effettivamente vivere nell'habitat specificato.
Tenere in considerazione il fatto che alcuni animali tra quelli specificati possono vivere in più di un habitat, 
mentre altri solo in uno.

Suggeirmento: può essere utile per coprire tutti i possibili casi implementare istruzioni match annidate.
'''


mammiferi = ["cane","gatto","cavallo","elefante","leone", "balena", "delfino"]
rettili = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli = ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
pesci = ["squalo", "trota", "salmone", "carpa"]
habitat = ["acqua", "aria", "terra"]

animale = input("\n Inserire un animale: ")
habitat_inserito = input("\n Inserire un habitat: ")
tuttiAnimali = [mammiferi, rettili, uccelli, pesci]


if animale != "stop":
    
    match animale:
        case animale if animale in mammiferi:
            animal_type = "mammiferi"
            print(f"\n{animale} appartiene alla categoria dei mammiferi")
        case animale if animale in rettili:
            animal_type = "rettili"
            print(f"\n{animale} appartiene alla categoria dei rettili")
        case animale if animale in uccelli:
            animal_type = "uccelli"
            print(f"\n{animale} appartiene alla categoria degli uccelli")
        case animale if animale in pesci:
            animal_type = "pesci"
            print(f"\n{animale} appartiene alla categoria dei pesci")
        case _ :
            print("\nAnimale non classificabile")
            animal_type = "unknown"
            
            
    #animali = [mammiferi, rettili, uccelli, pesci]
    animal_info = {"nome": animale, "tipo":animal_type, "habitat": habitat_inserito}
    
    
    
    match habitat_inserito:
        
        case "acqua":
                match animal_info:
                        
                    case {"nome": nome } if nome in {"serpente",
                                                "tartaruga", "coccodrillo", "cigno",
                                                "anatra", "squalo", "trota",
                                                "salmone", "carpa"}:
                             print(f"{animale} può vivere in {habitat_inserito}")
                    case _:
                             print(f"{animale} non può vivere in {habitat_inserito}")
                   
                                       
        case "terra":
                match animal_info:
                 
                    case {"nome": nome } if nome in [
                                                "cane", "gatto", "cavallo",
                                                "elefante", "leone", "serpente",
                                                "lucertola","tartaruga", "coccodrillo", 
                                                "cigno", "anatra", "gallina", 
                                                "tacchino"
                                             
                                                ]:                                                                               
                             print(f"{animale} può vivere in {habitat_inserito}")
                    
                    
                    case _ :
                             print(f"{animale} non può vivere in {habitat_inserito}")
        
                                                                                                                            
        case "aria":
                match animal_info:
                    
                    case {"nome": nome } if nome in [
                                                    "aquila", "pappagallo", "gufo",
                                                    "falco", "anatra", "cigno",
                                                                                                                                            
                                                  ]:
                              print(f"{animale} può vivere in {habitat_inserito}")
                              
                              
                    case _ :
                              print(f"{animale} non può vivere in {habitat_inserito}")
                              
                              
        case _ :
            print("Habitat non riconosciuto")
            
    
            
            

            
            
                
        


