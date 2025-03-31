'''
9-5. Login Attempts: 
Add an attribute called login_attempts to your User class from Exercise 9-3. 
Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
Make an instance of the User class and call increment_login_attempts() several times. 
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
Print login_attempts again to make sure it was reset to 0.
'''


class User:
    def __init__(self, first_name: str, last_name: str, age: int, email: str, city: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.city = city
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"Nome: {self.first_name} {self.last_name}")
        print(f"Età: {self.age}")
        print(f"Email: {self.email}")
        print(f"Città: {self.city}")
    
    def greet_user(self):
        print(f"Ciao {self.first_name} {self.last_name}, benvenuto nel nostro sistema!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Andrea", "Ferrario", 27, "andrea@ggmail.com", "Rocca di Papa")

user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
