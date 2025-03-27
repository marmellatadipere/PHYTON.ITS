'''
13. User Profile:  
Build a profile of yourself by calling build_profile(), 
using your first and last names and three other key-value pairs that describe you. 
All the values must be passed to the function as parameters. 
The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"'
'''

def build_profile(nome:str, cognome:str, altezza:int, peso:int, segnozodiacale: str) :
    return(print(f"{nome} {cognome}, altezza: {altezza}cm, peso:{peso} kg, segnozodiacale:{segnozodiacale}"))
    
build_profile("andrea", "ferrario", "181", "85", "aquario")