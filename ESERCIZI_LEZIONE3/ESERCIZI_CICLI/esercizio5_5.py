'''
5-5. Alien Colors #3: 

Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed for the appropriate color alien.
'''




colorealieno = ("verde", "giallo", "rosso")
print("spara a un alieno:")
alienoabbattuto = input("\n Di che colore era l'alieno?\n")

if alienoabbattuto in colorealieno:
    
    if alienoabbattuto == colorealieno[0]:
        print("\n +5 punti!\n")
    
    elif alienoabbattuto == colorealieno[1]:
        print("\n +10 punti!\n")
    
    else:
        print("\n +15 punti!\n")
else:
    print("\niIl colore non esiste")

