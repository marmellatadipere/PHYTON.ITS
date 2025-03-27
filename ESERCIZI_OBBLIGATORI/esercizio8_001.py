'''
8-1. Message: 
Write a function called display_message() that prints one sentence telling 
everyone what you are learning about in this chapter. 
Call the function, and make sure the message displays correctly.
'''


def display_message(lista_argomenti:list) -> str:
    for argomento in lista_argomenti:
        print(f"oggi in classe abbiamo fatto {argomento}")
    
    
display_message(["liste", "classi", "oggetti"])