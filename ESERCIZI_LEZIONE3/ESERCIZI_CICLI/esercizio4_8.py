'''
4-8. Cubes: 
A number raised to the third power is called a cube. 
For example, the cube of 2 is written as 2**3 in Python. 
Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), 
and use a for loop to print out the value of each cube.
'''


lista_numeri = list(range(1 , 11 , 1))
cubi = []

for ogni_numero_da1_a10 in lista_numeri:
    il_cubo_del_numero = ogni_numero_da1_a10 ** 3 #al cubo
    cubi.append(il_cubo_del_numero) #funzione lista.append() per aggiungere un alemento alla lista

for cubo_di_ogni_numero_da1_ad in cubi:
    print(cubo_di_ogni_numero_da1_ad)

