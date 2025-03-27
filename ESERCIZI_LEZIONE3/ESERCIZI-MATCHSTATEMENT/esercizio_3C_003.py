'''Esercizio 3C-3. 
Creare in Python una lista vuota chiamata 'oggetti'. 
Con un ciclo, riempire questa lista con tre oggetti diversi.
Scrivere, poi, un programma che utilizzi un match statement per classificare gli oggetti presenti nella lista:
- ["penna", "matita", "quaderno"] → "Materiale scolastico"
- ["pane", "latte", "uova"] → "Prodotti alimentari"
- ["sedia", "tavolo", "armadio"] → "Mobili"
- ["telefono", "computer", "tablet"] → "Dispositivi elettronici"
- Qualsiasi altra lista → "Categoria sconosciuta"

Expected Output:

['casa', 'hotel', 'b&b']
Categoria sconosciuta

--------------------------

['penna', 'matita', 'quaderno']
Materiale scolastico
'''


oggetti = set({}) #per trasformare una lista in una set


while len(oggetti) < 3:
    parola=str(input("inserisci oggetto: "))
    oggetti.add(parola)


match oggetti:
    case oggetti if oggetti=={"penna","matita","quaderno"}:
        print ("Materiale scolastico")
    case oggetti if oggetti=={"pane","latte","uova"}:
        print ("Prodotti alimentari")
    case oggetti if oggetti=={"sedia","tavolo","armadio"}:
        print ("Mobili")
    case oggetti if oggetti=={"telefono","computer","tablet"}:
        print ("Dispositivi elettronici")
    case _:
        print ("categoria sconosciuta")
        
        