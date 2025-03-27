'''
6-10. Favorite Numbers: 
Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
Then print each person’s name along with their favorite numbers.
'''



numeriamici = {
                "Adriano": [69,99,100], 
                "Daniele": [71, 33, 1334], 
                "Leandro" : [99,98], 
                "Francesco": [77, 887], 
                "Stefano" : [16,15]
              }

for (nome, numero) in numeriamici.items():
    print(f"I numeri preferiti di {nome} sono: {(numero)}")
    