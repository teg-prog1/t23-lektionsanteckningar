# OBS! om ni stöter på något ni inte känner igen får ni googla.
# När det gäller varför det står {} i print är det ett sätt för att skriva ut variabler.
# Googla gärna för att lära er mer om det.


import math

def vektor_längd_kalkylator():
    print("Välkommen till vektorlängd-kalkylatorn!")
    x = float(input("Ange x-koordinaten för vektorn: "))
    y = float(input("Ange y-koordinaten för vektorn: "))
    
    längd = round(math.sqrt(x**2 + y**2),3)
    
    print(f"Längden av vektorn ({x}, {y}) är {längd}")
    input()

def linjens_ekvation_kalkylator():
    print("Välkommen till räta linjer-kalkylatorn!")
    x1 = float(input("Ange x-koordinaten för punkt 1: "))
    y1 = float(input("Ange y-koordinaten för punkt 1: "))
    x2 = float(input("Ange x-koordinaten för punkt 2: "))
    y2 = float(input("Ange y-koordinaten för punkt 2: "))
    
    if x1 == x2:
        print("Linjen är vertikal och har ekvationen: x =", x1)
    else:
        lutning = (y2 - y1) / (x2 - x1)
        m_värde = round(y1 - lutning * x1,3)
        lutning = round(lutning,3)
        print(f"Linjens ekvation är: y = {lutning}x + {m_värde}")
        input()

def meny():
    print("Välkommen till matematikkalkylatorn!")
    print("Välj en av följande operationer:")
    print("1. Vektorer")
    print("2. Räta linjer")
    print("3. Avsluta programmet")
    
    val = int(input("Ange ditt val (1/2/3): "))
    
    if val == 1:
        vektor_längd_kalkylator()
        return True
    elif val == 2:
        linjens_ekvation_kalkylator()
        return True
    elif val == 3:
        print("Programmet avslutas")
        return False
    else:
        print("Ogiltigt val!")
        return True
        
def main():
    kör = True

    while kör:
        kör = meny()


main()


