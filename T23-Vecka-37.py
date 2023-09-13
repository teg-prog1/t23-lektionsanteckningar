# Skriv ett program som frågar användaren efter ett ord som är 3-6 bokstäver långt. 
# När användaren har skrivit in ordet ska programmet skriva ut varje bokstav i ordet på en egen rad.

# Om användaren skriver in ett ord som är för långt eller för kort ska programmet säga ifrån
# och ge användaren ett nytt försök.

# När ordet är utskrivet ska programmet tala om att det är klart.
# Användaren ska sedan få en till chans att skriva in ett nytt ord.


# ETT STEG I TAGET


while True:
    ordet = input("Skriv in ett ord som är 3-6 bokstäver långt: ")

    if len(ordet) < 3:
        print("ditt ord är för kort")
    elif len(ordet) > 6:
        print("ditt ord är för långt")
    else:
        for bokstav in ordet:
            print(bokstav)
        print("Nu är programmet klart!")
        svar = input("Vill du skriva in ett nytt ord? För ja skriv j, för nej skriv n ")
        
        if svar == "n":
            break
