## Kommentarer

# Skrivs med # innan. Bra att kommentera sitt program så att man kommer ihåg vad man har gjort.
# Högst upp i varje fil skriver ni ert namn, vad filen är till för och senast ni ändrade den

# Felicia Rosenberg -  Genomgång vecka 35. Ändrad 30/8-2023.

# Hello world
# Traditionellt första program
print("Hello, World!") #print används för att skriva ut någonting

# Variabler
namn = "Felicia"

# Vad kan jag döpa min variabel till?
#   siffror, bokstäver, understreck
#   understreck eller stor bokstav
#   något namn som är beskrivande
#   case sensitive
#   vissa ord är "förbjudna"

lillasyster_namn = "Frida"
lillasysterNamn = "Frida"
Lillasyster_namn = "Julia" #Vanligare att skriva variabler med små bokstäver

# Python förstår själv vilken typ variabeln har, man behöver oftast inte definiera det själv.


# Datatyper

#   String
väder = "halvklart till mulet, vad trevligt!\nHur mår du idag? :)" # en string är text, skrivs med "" runt
#print(väder)

#   Int (heltal)
ålder_barn = 7
ålder_vuxen = 32

summa_ålder = ålder_barn + ålder_vuxen
#print(summa_ålder)


#   Float (decimaltal, kom ihåg att använda . istället för ,)
poäng = 8.9
massa = 7.0

#   Boolean (är antingen sann eller falsk)
lämnat_in = True
ätit_middag = False


# Input
svar_ålder = int(input("Hur gammal är du?")) #inputen blir automatiskt en string, 
                                             # om det ska vara t.ex. en int behöver vi "casta" den till int, det vill säga ändra explicit.
ökad_ålder = svar_ålder + 23

# två olika sätt att lägga till 23 till ett heltal
svar_ålder = svar_ålder + 23
svar_ålder += 23

# 
print("Du kommer vara " + str(ökad_ålder)) # om vi har + måste vi göra om ökad_ålder till en string
print("Du kommer vara", svar_ålder) # vi kan också skriva , mellan två saker att printa, då läggs ett mellanslag automatiskt till


# Ta reda på en typ för en variabel
print(type(svar_ålder))


# Räkneoperationer

#   +, -, *, /, //, %

print(89+2) # vi kan addera både heltal och decimaltal

print(3-56) # vi kan subtrahera med både heltal och decimaltal

print(2*1.5) # vi kan multiplicera med både heltal och decimaltal

print(24/9) # vi kan dividera som vanligt med / Då blir det ett decimaltal om det inte går jämnt ut.

print(24//9) # vi kan göra heltalsdivision, då struntar programmet i decimaler. OBS: programmet avrundar inte

print(24%9) # vi kan få ut resten vid en division. T.ex. blir 10%3 1 eftersom 3 får plats 3 gånger i 10, och det blir 1 över.

# Importera random


# Yatzy slå tärning


