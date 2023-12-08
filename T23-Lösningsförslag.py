# Uppgift 5
word = "glasspinne"
vowels = ("a","o","u","å","e","i","y","ä","ö")

for bokstav in word:
    if bokstav in vowels:
        print("*")
    else:
        print(bokstav)


# Uppgift 6

def perfekt_tal(tal): #Funktion som avgör om ett tal är perfekt
    delare = [] # Lista med tal som talet är delbart med
    for i in range(1,tal):
        if tal % i == 0: # Om talet är delbart med i läggs i i listan
            delare.append(i)
    
    if sum(delare) == tal: # Om summan av delare är lika med talet är det perfekt
        print("Talet är perfekt")
    else:
        print("Talet är inte perfekt")

perfekt_tal(28)