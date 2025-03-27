'''
6-1. Person: 
Use a dictionary to store information about a person you know. 
Store their first name, last name, age, and the city in which they live. 
You should have keys such as first_name, last_name, age, and city. 
Print each piece of information stored in your dictionary.
'''


adriano = {"nome":"Adriano", "cognome":"Morra", "eta":34, "citta":"Pontecorvo"}                                                                                                      

for ogni_informazione, chesiha in adriano.items():
    if ogni_informazione == "eta":
        print(f"{chesiha} anni")
    else:
        print(chesiha)




