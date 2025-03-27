'''
4-11.My Pizzas, Your Pizzas: 
Start with your program from Exercise 4-1. 
Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. 
Print the message My favorite pizzas are:, and then use a for loop to print the first list. 
Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
Make sure each new pizza is stored in the appropriate list.
'''


pizze_preferite = [
                "Margherita", 
                "Diavola", 
                "Viustel e Patatine",
                ]
pizze_amici = [
                "Margherita", 
                "Diavola", 
                "Viustel e Patatine", 
                "Maionese e porcini"]


pizze_preferite.append("Pummarola")
pizze_amici.append("SalsicciaFriarielli")

if pizze_preferite != pizze_amici:
    print("\nSono due liste differenti")
    
pizze_preferite_parole = ", ".join(pizze_preferite).lower() 
pizze_amici_parole = ", ".join(pizze_amici).lower()


print(f"Le mie pizze preferite sono: {pizze_preferite_parole}")
print(f"Le pizze preferite dei miei amici sono: {pizze_amici_parole}")
    

