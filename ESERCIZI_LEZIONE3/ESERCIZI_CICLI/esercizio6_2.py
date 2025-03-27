''' 
6-2. Favorite Numbers: 
Use a dictionary to store people’s favorite numbers. 
Think of five names, and use them as keys in your dictionary. 
Think of a favorite number for each person, and store each as a value in your dictionary. 
Print each person’s name and their favorite number. 
For even more fun, poll a few friends and get some actual data for your program.
'''


numeriamici = {"Adriano": 69, "Daniele": 71, "Leandro" : 99, "Francesco": 77, "Stefano" : 15}

for (nome, numero) in numeriamici.items():
    print(f"Il numero preferito di {nome} è: {numero}")
    
