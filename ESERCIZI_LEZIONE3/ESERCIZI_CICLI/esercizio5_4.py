'''
5-4. Alien Colors #2: 
Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain:
    
• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
• Write one version of this program that runs the if block and another that runs the else block.
'''


colorealieno = ("verde", "giallo", "rosso")

print("spara a un alieno:")
alienoabbattuto = input("\n Di che colore era l'alieno?\n")

if alienoabbattuto == colorealieno[0]:
    print("\n +5 punti!\n")
    
else:
    print("\n +10 punti!\n")