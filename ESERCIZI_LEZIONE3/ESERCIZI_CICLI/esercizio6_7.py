'''
6-7. People: 
Start with the program you wrote for Exercise 6-1. 
Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
Loop through your list of people. As you loop through the list, print everything you know about each person.
'''


adriano = {"nome":"Adriano", "cognome":"Morra", "eta":34, "citta":"Pontecorvo"}                                                                                                          
  
matteo = {"nome":"Matteo", "cognome":"Fabbri", "eta":23, "citta":"Pontenona"}                                                                                                     
     
daniele = {"nome":"Daniele", "cognome":"Gallo", "eta":19, "citta":"Rodi"}
                                                                                                  


people = [adriano, matteo, daniele]

for persona in people:
    print(" \n")
    for ogni_informazione, chesiha in persona.items():
        if ogni_informazione == "eta":
            print(f"{chesiha} anni")
        else:
            print(f"{chesiha}")
        
    