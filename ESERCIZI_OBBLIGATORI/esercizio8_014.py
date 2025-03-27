'''
8-14. Cars: 
Write a function that stores information about a car in a dictionary. 
The function should always receive a manufacturer and a model name. 
It should then accept an arbitrary number of keyword arguments. 
Call the function with the required information and two other name-value pairs, 
such as a color or an optional feature. 
Your function should work for a call like this one: 
car = make_car('subaru', 'outback', color='blue', tow_package=True) 
Print the dictionary that’s returned to make sure all the information was stored correctly. 
'''


def macchina(marca: str, modello: str, **altreinfo) -> dict:
   
    car = {"marca": marca, "modello": modello}
    
    for ogni, info in altreinfo.items():
        car[ogni] = info
    
    return car


prova = macchina("Ferrari", "Andrea", colore="rosso", anno=2021, targa="GX877FF")
print(prova)
