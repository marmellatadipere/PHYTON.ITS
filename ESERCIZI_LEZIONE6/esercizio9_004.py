'''
9-4. Number Served:
Start with your program from Exercise 9-1. 
Add an attribute called number_served with a default value of 0. 
Create an instance called restaurant from this class. Print the number of customers the restaurant has served, 
and then change this value and print it again. Add a method called set_number_served() that lets you set the number of customers that have been served. 
Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
Call this method with any number you like that could represent how many customers were served in, say, a day of business. '
'''


class Restaurant:
    number_served = 0
    def __init__(self, name: str, cuisinetype: str):
        self.name = name
        self.cuisinetype = cuisinetype
    
    def describe_restaurant(self):
        print(f"Nome del ristorante: {self.name}")
        print(f"Tipo di cucina: {self.cuisinetype}")
    
    def open_restaurant(self):
        print("Il ristorante è aperto!")
    
    def set_number_served(self, number):
        self.number_served += number
    
    def customers_served(self):
        print(f"Il ristorante ha servito {self.number_served} persone.")


ristorante = Restaurant("Pinocchio", "Cucina Italiana")

ristorante.describe_restaurant()
ristorante.open_restaurant()

ristorante.customers_served()

ristorante.set_number_served(50)
ristorante.customers_served()
