# if, else, elif

# if, else och elif kan användas för att programmet ska göra olika saker beroende på villkor

# om vi till exempel vill skriva ut olika saker beroende på hur stort ett tal är

tal = int(input("Skriv in ett tal: ")) # tar in ett tal från användaren

if tal < 5: # kollar om talet är mindre än 5
    print("Talet är mindre än 5") #skriver ut detta om talet är mindre än 5

elif tal == 10: # om talet inte är mindre än 5 körs denna. Den kollar om talet är lika med 10
                # vi har två likamed-tecken när vi ska jämföra saker i Python
    print("Talet är 10")

else: # om ingen av de två första stämmer så körs den här
    print("Talet är inte mindre än fem, och talet är inte 10")

# För att markera att något är "inom" if-satsen eller inom elif eller inom else används indenteringar
    # denna rad är exempelvis indenterad jämfört med raden ovan

# jämförelser kan göras exempelfis med dessa:
# <=, <, >, >=, ==, !=

if tal <= 3: # mindre än eller lika med skrivs med <=, och större än eller lika med tvärtom med >=
    print("talet är mindre än eller lika med tre")

if tal != 2: # att kolla om något inte är lika med görs med ! innan =
    print("talet är inte lika med 2")


# and, or, not
# vi kan kolla två saker samtidigt
tal2 = int(input("skriv ett till tal: "))

if tal < 2 and tal2 == 4: # körs bara om båda sakerna stämmer
    print("första talet är mindre än 2 OCH andra talet är lika med 4")

if tal == 9 or tal2 == 10: # körs om någon av sakerna stämmer
    print("första talet är lika med 9 ELLER andra talet är lika med 10")

# vi kan ha flera elif om vi vill

if tal2 == 10:
    print("du vann, grattis!")

elif tal2 == 9 or tal2 == 8:
    print("du vann nästan")

elif tal2 == 7:
    print("du var lite nära att vinna")

elif tal2 > 10:
    print("ditt tal var för högt")

else:
    print("ditt tal var aldeles för lågt")


# nästlade if-satser
# vi kan också ha if-satser i varandra, så kallade nästlade if-satser

if tal < 3:
    tal3 = input("skriv ett till tal: ")
    if tal3 < 3:
        print("du tog dig hela vägen fram")


#########################################################################################################


# while-loop
# kan användas när man vill köra en kod flera gånger tills något stoppar den
tal = 4

while tal < 10: # loopen kommer att köras så länge tal är mindre än 10
    tal += 1 # varje varv i loopen lägger vi på 1 på talet. 
                # Om vi inte gör det kommer talet vara 4 hela tiden och loopen blir oändlig
else:
    print("nu är det slut!") # det här skrivs ut när loopen tar slut
    

# for-loop
# kan användas när man vill köra en kod ett visst antal gånger, eller loopa igenom en sak (till exempel en sträng)

for i in range(1,20,2): # loopar med hjälp av range(), 1 är starttalet, 20 är hur högt den ska gå och 2 är hur stora hopp
    # om vi bara skriver for i in range(5) kommer siffrorna 0, 1, 2, 3, 4 skrivas ut. Den startar automatiskt på 0
    # om man inte skriver något annat. För mer info, googla range() Python
    print(i)

# for x in "apple"

for bokstav in "apple": # vi kan loopa igenom bokstäverna i en sträng
    print(bokstav)


# nästlade for-loopar
# vi kan även ha loopar i loopar, testa själv och se vad som skrivs ut

for i in range(4):
    for j in range(4):
        print(i,j)
