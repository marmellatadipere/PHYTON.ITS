'''
5-7. Favorite Fruit: 
Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit is in your list. 
    If the fruit is in your list, the if block should print a statement, such as You really like Apples!
'''


fruttipreferiti = ["banana", "cachi", "pescionfrui"]
frutto = input("Indovina uno dei miei frutti preferiti:\n")

if frutto in fruttipreferiti:
    print(f"\n{frutto.title()} e' tra i miei frutti preferiti")
else:
    print(f"\n{frutto.title()} non e' tra i miei frutti preferiti")



