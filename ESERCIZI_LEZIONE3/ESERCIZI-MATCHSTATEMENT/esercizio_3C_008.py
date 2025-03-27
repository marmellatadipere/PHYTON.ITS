'''
Esercizio 3C-8. Scrivere un programma in Python che legga una frase di una riga e mostri una delle seguenti risposte:
- "Si" -> se la frase termina con un punto interrogativo (?) ed il numero dei caratteri è pari;
- "No" -> se la frase termina con un punto interrogativo (?) ed il numero dei caratteri è dispari;
- "Wow!" -> se la frase termina con un punto esclamativo (!)
- "Tu dici" seguito dalla frase inserita racchiusa tra doppi apici in tutti gli altri casi.

Expected Output:

frase: di essere bellissimo
Output: Tu dici "di essere bellissimo"

- - - - - - - - - - - - - - - - - - - - - -

frase: ho vinto!
Output: Wow!
'''



frase = input("\n Inserire una frase o domanda:\n")

match frase:
    
    case frase if frase[-1] == "?":
        if len(frase)%2 == 0:
            print("si")
        else:
            print("no")
            
            
    case frase if frase [-1] == "!":
        print("Wow")
        
        
    case _  :
        print(f'"tu dici" {frase}')