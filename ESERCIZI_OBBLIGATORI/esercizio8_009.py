'''
8-9. Messages: 
Make a list containing a series of short text messages. 
Pass the list to a function called show_messages(), which prints each text message.
'''


lista = ["E", "la", "lazio", "..."]

def show_messages(lista:list) -> list:
        print(" ".join(lista))
        
show_messages(lista)