# Dictionary

ålder = {"Felicia":24,"Frida":22,"Maximiliam":15,"Victor":24}

# Skrivs med {} och har par av nyckel och värde

# Ordnade, går att ändra, tillåter inte dubletter (inte samma nyckel)

# Skriva ut ett värde från en nyckel
värde = ålder["Maximiliam"]
print(värde)

# Kan innehålla olika datatyper
intressen = {"Felicia":["segla","baka","resa"],"Victor":["laga mat","hockey","spela spel"]}

# Metoder för dictionary: https://www.w3schools.com/python/python_dictionaries_methods.asp

ålder["Felicia"]= input("skriv en ålder: ")
print(ålder["Felicia"])