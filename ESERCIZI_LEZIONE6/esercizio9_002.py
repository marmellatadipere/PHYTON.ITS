'''
9-2. Three Restaurants: 
Start with your class from Exercise 9-1. 
Create three different instances from the class, and call describe_restaurant() 
for each instance.
'''

class Restaurant:
    def __init__(self, name:str, cuisinetype:str):
        self.name = name
        self.cuisinetype = cuisinetype
    def describe_restaurant(self):
        print(self.name)
        print(self.cuisinetype)
    def open_restaurant(self):
        print("il ristorante e' aperto")
        

ristorante = Restaurant("Pinocchio", "Italiana")
print(ristorante.name)
print(ristorante.cuisinetype)

ristorante2 = Restaurant("Il mulino", "Italiana")
print(ristorante.name)
print(ristorante.cuisinetype)

ristorante3 = Restaurant("Naumachia", "Trappola per turisti")
print(ristorante.name)
print(ristorante.cuisinetype)



ristorante.describe_restaurant()
ristorante.open_restaurant()
ristorante2.describe_restaurant()
ristorante2.open_restaurant()
ristorante3.describe_restaurant()
ristorante3.open_restaurant()
