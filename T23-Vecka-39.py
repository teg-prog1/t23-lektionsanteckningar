# Funktioner

# Ett block med kod som kan användas på andra ställen i programmet

# En funktion har ett namn och behöver definieras

def hälsning():
    print("Hejsan!")

# För att köra en funktion behöver vi kalla på den. Först definierar vi bara den, sen kan vi använda den.
# Vi kan använda den flera gånger om vi vill.

hälsning()

# En funktion kan ta in en parameter som den kan använda. Det kan vara vilken slags variabel som helst.
def bättre_hälsning(namn):
    print("Hejsan", namn)

användare_namn = "Felicia"
bättre_hälsning(användare_namn)

# Funktioner kan också ta in flera parametrar
def addera_tal(tal1,tal2=3):
    print(tal1+tal2)

addera_tal(2,5)

# Om man skriver in för många eller för få parametrar blir det fel
addera_tal(7)

# Vi kan ha en default också om vi vill, då behövs inte parametern

# Funktionen kan returnera något

def multiplicera_tal(tal1,tal2):
    produkt = tal1 * tal2
    return produkt

print(multiplicera_tal(3,4))
resultat = multiplicera_tal(8,9)
print(resultat)

# Om vi vill spara det som returneras måste vi lägga det i en variabel

# Det går att returnera flera saker från en funktion.

def dividera_kvadrera(tal1,tal2):
    kvot = tal1/tal2
    kvadraten = tal1 ** 2
    return kvot, kvadraten

svar_kvot, svar_kvadrat = dividera_kvadrera(16,4)
print(svar_kvot)
print(svar_kvadrat)