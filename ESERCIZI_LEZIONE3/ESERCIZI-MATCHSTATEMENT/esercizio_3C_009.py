'''
Esercizio 3C-9. 
Scrivere un programma in Python che permetta all'utente di inserire le coordinate di un punto (x, y) e salvi le coordinate inserite in una tupla. 
Utilizzare il  match statement per determinare la sua posizione del punto inserito nel piano cartesiano:

- Origine → Se il punto è (0,0), stampare: "Il punto si trova nell'origine."
- Asse X → Se y = 0, stampare: "Il punto si trova sull'asse X."
- Asse Y → Se x = 0, stampare: "Il punto si trova sull'asse Y."
- Primo quadrante → Se x > 0 e y > 0, stampare: "Il punto si trova nel primo quadrante."
- Secondo quadrante → Se x < 0 e y > 0, stampare: "Il punto si trova nel secondo quadrante."
- Terzo quadrante → Se x < 0 e y < 0, stampare: "Il punto si trova nel terzo quadrante."
- Quarto quadrante → Se x > 0 e y < 0, stampare: "Il punto si trova nel quarto quadrante."

Expected Output:

Inserisci la coordinata X: 0
Inserisci la coordinata Y: 0
Output: Il punto (0,0) si trova nell'origine.

- - - - - - - - - - - - - - - - - - - - - -

Inserisci la coordinata X: 3
Inserisci la coordinata Y: 5
Output: Il punto (3,5) si trova nel primo quadrante.

- - - - - - - - - - - - - - - - - - - - - - - - -

Inserisci la coordinata X: 4
Inserisci la coordinata Y: 0
Output: Il punto (4,0) si trova sull'asse X.
'''



coordinate = ()
puntoX = input("Inserire X: \n")
puntoY = input("Inserire Y \n")


