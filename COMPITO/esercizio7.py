#Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n, 
# entrambe contenenti valori interi, calcoli la somma incrociata degli elementi.
#Memorizzare ogni somma incrociata in una nuova lista c e, quindi,
# visualizzare in output le liste a, b, c.

a = []
b = []
c= []



while True:    
    num_a = int(input("inserire un numero per la lista A:\n"))
    a.append(num_a)
    continuare = input("Vuoi inserire un altro numero?\n")
    if continuare == "no":
        break

while len(b) < len(a):
    num_b = int(input("inserire un numero per la lista B\n"))
    b.append(num_b)

prima_cifra_a = 0
ultima_cifra_b = -1

while len(c) < len(a):
    somma_incrociata = a[prima_cifra_a] + b[ultima_cifra_b]
    c.append(somma_incrociata)
    prima_cifra_a += 1
    ultima_cifra_b -= 1

print(a)
print(b)
print(c)
