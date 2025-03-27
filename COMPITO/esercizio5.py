

portafogli = int(input("C'hai 'no spiccio?\n"))    #chiedo in input quanti Eurp spicci ha l'utente
numero_barrette_acquistabili = 0                    #creo il counter delle barrette acquistate/acquistabili
buonosconto = 0                                     #creo il counter buoni sconto

while portafogli > 0:                              #imposto il ciclo dell' utente che mette gli spicci nella macchinetta
    numero_barrette_acquistabili += 1              #per ogni euro: aggiorno di 1 la somma delle barrette...
    portafogli -= 1                                #... tolgo uno spiccio dal portafogli
    buonosconto += 1                               # aggiungo un buono sconto

#quando arrivo a sei buoni pasto li scambio per una barretta senza intaccare il portafogli
    if buonosconto == 6:                            
       buonosconto -= 6
       numero_barrette_acquistabili += 1
else: 
    print(f"Ti puoi permettere {numero_barrette_acquistabili} barrette, Golosone")
    print(f"Ti sono avanzati {buonosconto} buoni sconto!")