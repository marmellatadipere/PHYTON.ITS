'''
4-6. Odd Numbers: 
Use the third argument of the range() function to make a list of the 
odd numbers from 1 to 20.
Use a for loop to print each number.
'''


lista_dispari = list(range(1 , 20 , 2 ))   #creo la lista dei numeri dispari 
                                           # logica:  1 ([0]) + 2 ([2]) + 2 ([2]) + . . . FINO a 20 
                                           #                                !!!! NON INCLUSO !!!!

#stampo i numeri della lista dispari utilizzando ciclo for
for number in lista_dispari:
    print(number)