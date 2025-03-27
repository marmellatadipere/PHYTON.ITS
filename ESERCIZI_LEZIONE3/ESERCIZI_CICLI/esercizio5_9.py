'''
5-9. No Users: 
Add an if test to hello_admin.py to make sure the list of users is not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message is printed.
'''


users = ["admin", "alessio", "manuel", "carlo", "samuele", "piero"]

if len(users) == 0:
    print("\nDobbiamo trovare qualche utente!")
else:
    for accesso in users:
        if accesso == "admin":
            print("Benvenuto admin vuoi vedere uno status report?")
        else:
            print(f"benvenuto {accesso.title()}")
    