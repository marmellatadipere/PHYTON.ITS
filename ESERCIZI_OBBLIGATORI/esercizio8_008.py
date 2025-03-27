'''
8-8. User Albums: 
Start with your program from Exercise 8-7. 
Write a while loop that allows users to enter an album’s artist and title. 
Once you have that information, call make_album() with the user’s input 
and print the dictionary that’s created. Be sure to include a quit value in the while loop.
'''



def make_album(artista, titolo, lunghezza=None) -> None:
    album = {"artist": artista,"titolo": titolo}
    if lunghezza :
       album["canzoni"] = lunghezza
    return album
    
    


album1 = make_album("Tedua", "Orange County")
album2 = make_album("Caparezza", "Exuvia", 19)
album3 = make_album("Ski & Wok", "99")


print(album1)
print(album2)
print(album3)
