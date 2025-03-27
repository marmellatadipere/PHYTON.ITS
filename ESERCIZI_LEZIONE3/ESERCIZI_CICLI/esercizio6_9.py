''' 
6-9. Favorite Places: 
Make a dictionary called favorite_places. 
Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 
To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. 
Loop through the dictionary, and print each person’s name and their favorite places.
'''


postipreferiti = {
                "Adriano" : ["Thailandia", "Brasile", "Cuba"],
                "Mirko" : ["Giappone", "Cina", "Messico"],
                "Maurizietto" : ["Centroni", "Flaminio", "Piazza della Libertà"]
                 }
            
                      
for ogniamico, suoipostipreferiti in postipreferiti.items():
    print(f"I posti preferiti di {ogniamico} sono: {(" ".join(suoipostipreferiti))}")
    
    