''' 
4-2. Animals: 
Think of at least three different animals that have a common characteristic.
Store the names of these animals in a list, and then use a for loop to print out the name of each animal.

• Modify your program to print a statement about each animal, such as A dog would make a great pet.
• Add a line at the end of your program, stating what these animals have in common. 
You could print a sentence, such as Any of these animals would make a great pet!
'''


animali = ("pecora","manzo", "maiale",)

for animale in animali:
    print(f"Il/La {animale} è ottimo/a alla brace.")

caratteristica_comune = "ottimi alla brace"
print(f"La caratteristica comune di {", ".join(animali)} è che sono {caratteristica_comune}.")
