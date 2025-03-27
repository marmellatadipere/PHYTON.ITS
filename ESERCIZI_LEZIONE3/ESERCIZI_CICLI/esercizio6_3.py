''' 
6-3. Glossary: 
A Python dictionary can be used to model an actual dictionary. 
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous chapters. 
    Use these words as the keys in your glossary, and store their meanings as values.
• Print each word and its meaning as neatly formatted output. 
    You might print the word followed by a colon and then its meaning, 
    or print the word on one line and then print its meaning indented on a second line. 
    Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
'''


glossary = {
            "print": "stampare a schermo", 
            "glossary" : "dizionario", 
            "break" : "pausa", 
            "directory": "percorso", 
            "byte" : "insieme di 8 bit"
            }
            
for parola, significato in glossary.items():
    print(f"{parola}: \n{significato}\n")