#ESERCIZI LEZIONE 2


name = "Andrea"
print("Hello" + " " + name + ", would you like to learn some Python today?")
# 

name = "Andrea"
print(name.lower())
print(name.upper())
print(name.title())
#

name = "Boban"                      #NON SO COME MANTENERE LE VIRGOLETTE
quote = (
        "se uomo ama donna più di birra gelata davanti a tv "                       
        "con finale champions forse vero amore, ma non vero uomo"
        )
print(name + " " + "once said:" + " " + quote)
#

famous_person = "Boban"
message = name + " " + "once said:" + " " + "se uomo ama donna più di birra gelata davanti a tv con finale champions forse vero amore, ma non vero uomo)"
print(message)
#

names = ["Andrea", "Leandro", "Arturo"]
for name in names:
    print(name)
#

for name in names:
    print(f"{name}, ricordati che mi devi ancora 20$")
#

transportations = ["moto", "autobus", "automobile"]
for mode in transportations:
    print("I usually move by" + " " + mode)
#

guestList = ["Totti", "Leandro", "Cesare Cesaroni"]
for guest in guestList:
    print(f"{guest}, Would you join me in a dinner?")
#

noguest = "Leandro"
print(f"{noguest} can't make the dinner.\n")
#

guestList.remove(noguest)
guestList.append("Darione")


#
new_guests = ["Marco Togni", "Dario Fo", "Dario Argento"]

for guest in guestList:
    print(f"dear {guest} I just found a bigger table")

guestList.insert(0, "Claudio Lotito")
guestList.insert(2, "Massimo Ranieri")
guestList.append("Assan Diop")

for guest in guestList:
    print(f"dear {guest} Would you join me in a dinner?")
#

for guest in guestList:
    print(f"dear {guest} I can invite only 2 of you")

while len(guestList) > 2:
    nomore = guestList.pop(0)
    print(f"Sorry, {nomore}, I can invite you to dinner no more.")

for guest in guestList:
    print(f"Dear {guest} you are still invited to the dinner")

del guestList[:]
print(guestList)
#

places = ["Colombia", "Olanda", "Thailandia", "Pakistan", "Nepal"]
print(places)
print(sorted(places))
??????