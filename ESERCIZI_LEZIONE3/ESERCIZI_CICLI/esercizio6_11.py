'''
6-11. Cities: 
Make a dictionary called cities. 
Use the names of three cities as keys in your dictionary. 
Create a dictionary of information about each city 
and include the country that the city is in, its approximate population, and one fact about that city. 
The keys for each city’s dictionary should be something like country, population, and fact. 
Print the name of each city and all of the information you have stored about it.
'''                 


citta = {
        "Rocca di Papa" : {"nazione" : "Italia", "popolazione" : 15.000,"info" :"Cittàdina di taglialegna"},
        "Pontecorvo" : {"nazione" : "Senegal", "popolazione" : 10.000, "info" : "Concentrazione di allevamenti suini"},
        "amsterdam" : {"nazione": "Olanda", "popolazione" : 920000,"info" : "Good drugs"}
        }

for cittapresente, informazioni in citta.items():
    print(f"Città | {cittapresente}\n")
    print(f"Nazione | {informazioni["nazione"]}")
    print(f"Popolazione | {informazioni["popolazione"]}")
    print(f"Curiosità | {informazioni["info"]}")
        