'''
4-10. Slices:
 Using one of the programs you wrote in this chapter add several lines to the end of the program that do the following:
    
• Print the message The first three items in the list are:. 
Then use a slice to print the first three items from that program’s list.

• Print the message Three items from the middle of the list are:. 
Then use a slice to print three items from the middle of the list.

• Print the message The last three items in the list are:. 
Then use a slice to print the last three items in the list.
'''



lista_numeri = list(range(1 , 7 , 1)) #riprendo esercizio 4.8
cubi = []

for ogni_numero_da1_a10 in lista_numeri:
    il_cubo_del_numero = ogni_numero_da1_a10 ** 3 #al cubo
    cubi.append(il_cubo_del_numero)

for cubo_di_ogni_numero_da1_ad in cubi:
    print(cubo_di_ogni_numero_da1_ad)


# utilizzo la funzione slice(DA , A-NON INCLUSO!-)
primi_tre_numeri = slice(0 , 3) #L'ULTIMO NUMERO NON E'  INLUSOOOOO!!!!
print(f"The first three items in the list are: {cubi[primi_tre_numeri]}")


ultimi_tre_numeri = slice(-1, -4, -1) #COME PER LA FUNZIONE RANGE PARTE DA -1 
                                      # E ARRIVA A 4 !!NON INCLUSO!! SCALANDO DI -1
print(f"The last three items in the list are: {cubi[ultimi_tre_numeri]}")


numero_centrale:int = len(cubi) // 2  #cerco il numero centrale utilizzando la floor division cosi da avere un intero come riultato
start:int = numero_centrale - 1       
end:int = numero_centrale + 2  #piu due perche l ultimo numero dello slice non è incluso

tre_numeri_centro:int = slice(start,end)
print(f"The three items in the middle of the list are: {cubi[tre_numeri_centro]}")


