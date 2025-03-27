'''
5-10. Checking Usernames: 
Do the following to create a program that simulates how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)
'''


#creo le varie liste richieste
user_registrati = ["marmellatAdipere", "adriano12" , "danielinho2202", "frakiller01", "juan","MARCH99"]
user_registrati_minuscoli = [] #stessa lista ma sensibile alle lettere maiuscole
nuovi_user = ["MARMELLATADIPERE", "frakiller01", "march99", "carletto", "multimarket"]
nuovi_user_minuscoli = [] #stessa lista la sensibile alle lettere maiuscole

# ciclo che trasforma ogni elemento in minuscolo e lo inserisce nella lista dei nomi utenti ma in minuscolo
for user in user_registrati:
    user_registrati_minuscoli.append(user.lower())
for nuovouser in nuovi_user:
    nuovi_user_minuscoli.append(nuovouser.lower())

# ciclo che verifica che ogni nuovo nome utente in trasformato in minuscolo non sia uguale a nessun nome utente gia registrato trasformato in minuscoolo
for nuovouser in nuovi_user_minuscoli:
    if nuovouser.lower() in user_registrati_minuscoli:
        print(f"{nuovouser} non disponibile")
    else: 
        print(f"{nuovouser} disponibile")

        

