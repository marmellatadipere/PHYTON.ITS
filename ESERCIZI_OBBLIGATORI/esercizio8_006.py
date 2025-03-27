'''
8-6. City Names: 
Write a function called city_country() that takes in the name of a city and its country. 
The function should return a string formatted like this: "Santiago, Chile". 
Call your function with at least three city-country pairs, and print the values that are returned.
'''

def city_country(name:str, country:str):
    stringa = (f"{name}, {country}")
    return stringa
    
print(city_country("Roma", "italia"))
print(city_country("Milano", "italia"))
print(city_country("Fiume", 'italia'))