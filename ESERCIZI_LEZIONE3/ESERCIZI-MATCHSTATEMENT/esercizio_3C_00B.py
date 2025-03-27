
nome_chiave = input("Inserire nome\n")
genere_valore = (input("inserire genere, M o F o Preferisco non rispondere\n")).lower()

match genere_valore:
    case "m":
        print(f"{nome_chiave},UOMO")
    case "f":
        print(f"{nome_chiave},DONNA")
    case _:    
        print("Genere non valido per un documento")