'''
9-1. Restaurant: 
Make a class called Restaurant. 
The __init__() method for Restaurant should store two attributes: 
    a restaurant_name and a cuisine_type. 
Make a method called describe_restaurant() that prints these two pieces of information, 
and a method called open_restaurant() that prints a message indicating that the restaurant is open. 
Make an instance called restaurant from your class. 
Print the two attributes individually, and then call both methods.
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


ristorante.describe_restaurant()
ristorante.open_restaurant()