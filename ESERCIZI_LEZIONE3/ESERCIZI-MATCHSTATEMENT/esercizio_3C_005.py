'''Esercizio 3C-5. 
Scrivere un programma che memorizzi il nome, il ruolo e l'età di un utente in un dizionario.
Il nome, il ruolo e l'età devono essere inseriti in input dall'utente stesso. 
Il programma deve determinare il livello di accesso ai servizi in base 
    al ruolo e all'età dell'utente secondo questo schema:

- Admin → "Accesso completo a tutte le funzionalità."
- Moderatore → "Può gestire i contenuti ma non modificare le impostazioni."
- Utente adulto (età ≥ 18) → "Accesso standard a tutti i servizi."
- Utente minorenne (età < 18) → "Accesso limitato! Alcune funzionalità sono bloccate."
- Ospite → "Accesso ristretto! Solo visualizzazione dei contenuti."
- Ruolo non riconosciuto → "Attenzione! Ruolo non riconsciuto! Accesso Negato!"'''


# creo le variabili per il dirozionario
nome = input("\nCome ti chiami?\n").title()
eta = int((input("\nQuanti anni hai\n")))
ruolo = input("\nChe ruolo hai?\n").lower()

# creo in dizionario
utente = {"nome": nome, "ruolo": ruolo, "eta": eta}

#faccio il match per ogni ruolo
match utente:
           
    case utente if ruolo == "admin":
        print(f"\n{nome}, in qualita di {ruolo} hai accesso completo a tutte le funzionalita")
        
        
    case utente if ruolo == "moderatore":
        print(f"\n{nome}, in qualita di {ruolo} puoi gestire i contenuti ma non modificare le impostazioni.") 
        
    case utente if ruolo == "user": #nel caso un cui l'utente si un user allora controllo anche se e' maggiorenne o meno
        if int(eta) >= 18:
            print(f"\n{nome}, in qualita di {ruolo.title()} adulto, hai accesso standard a tutte le informazioni.")
        else:
            print(f"\n{nome}, in qualita di {ruolo.title()} minorenne, hai accesso limitato a alcune informazioni")
        
    case utente if ruolo == "ospite":
        print(f"\n{nome}, in qualita di {ruolo} hia accesso ristretto alla sola visualizzazione dei contenuti")    
        
        
    case _ :
        print(f"{ruolo.title()} e' un ruolo non riconosciuto!")
        

