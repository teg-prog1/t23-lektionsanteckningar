# Listor, tuples, mängder

# Listor
# Kan lagra flera värden i en variabel

frukter = ["äpple","banan","mango","päron"]
tom_lista = []

# Listor är ordnade, det vill säga ordningen spelar roll
# De är indexerade

#print(frukter[1])

# Listor går att förändra värdena på

#frukter[0] = input("säg en annan frukt än äpple: ")

#print(frukter)

# Det kan finnas dubletter i listor

# Det går att spara olika datatyper i en lista

blandad_lista = [1, 3.4, "hej", True]

# Vi kan loopa igenom en lista

#for element in blandad_lista:
    #print(element, end=" ")

#print(blandad_lista)

# Vi kan plocka ut längden på en lista

#print(len(blandad_lista))

# Metoder för listor: https://www.w3schools.com/python/python_lists_methods.asp

# sort(), append(), pop(), remove(), reverse()

test_lista = [4, 5, 1, 2, 8, 3, 5, 6]

test_lista.sort()
#print(test_lista)

test_lista.append(10)
#print(test_lista)

#################################################################################################

# Tuples

elever = ("Natalie", "Leo", "Joshua")

# Som listor, men de går inte att ändra

# Mer minneseffektiva och tidseffektiva

# Bättre att använda om man har värden som inte kommer att ändras

#################################################################################################

# Sets

matvaror = {"mjölk", "tacobröd", "tacokrydda", "paprika", "paprika", "paprika"}
andra_matvaror = {"mjölk", "paprika", "gurka"}

# Ingen ordning, tillåter inte dubletter

print(matvaror)

# Går att lägga till och ta bort element, men inte byta ut eller ändra ett specifikt element

# metoder för sets: https://www.w3schools.com/python/python_sets_methods.asp

# issubset(), intersection(), difference()

svar = andra_matvaror.issubset(matvaror)
print(svar)

