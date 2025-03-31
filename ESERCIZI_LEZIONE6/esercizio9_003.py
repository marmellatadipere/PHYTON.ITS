'''
9-3. Users: 
Make a class called User. 
Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. 
Make a method called describe_user() that prints a summary of the user’s information. 
Make another method called greet_user() that prints a personalized greeting to the user. 
Create several instances representing different users, and call both methods for each user.   
'''

class User:
    def __init__(self, first_name: str, last_name: str, age: int, email: str, city: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.city = city
    
    def describe_user(self):
        print(f"Nome: {self.first_name} {self.last_name}")
        print(f"Età: {self.age}")
        print(f"Email: {self.email}")
        print(f"Città: {self.city}")
    
    def greet_user(self):
        print(f"Ciao {self.first_name} {self.last_name}, benvenuto nel nostro sistema!")


user1 = User("Luca", "Rossi", 28, "luca.rossi@email.com", "Roma")

# Chiamata ai metodi per ciascun utente
print("Descrizione Utente 1:")
user1.describe_user()
user1.greet_user()
print()
