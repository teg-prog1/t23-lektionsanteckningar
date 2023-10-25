# Här är ett program som innehåller en del fel
# Vi ska åtgärda dem på följande sätt:
# 1. Se till att programmet går att köra
# 2. Testa funktionerna som ska finnas
# 3. Testa vad som händer om man skriver in konstiga saker och åtgärda det
# 4. Fundera om det är något mer vi kan göra för att öka användarvänligheten

import random

def generate_question(operation): # genererar fråga och svar beroende på om multiplikation eller division ska testas
                                # tar in vilken av multiplikation och division som ska testas som parameter till funktionen
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    if operation == "multiply": # om vi vill testa multiplikation
        question = "What is " + str(num1) + " * " + str(num2) + "? " # skapar en fråga
        answer = num1 * num2 # skapar ett facit till frågan
    elif operation == "divide": # om vi vill testa division
        question = f"What is {num1*num2} / {num1}? " # skapar en fråga
        answer = num2 # facit till frågan
    return question, answer # ger tillbaka frågan och facit till frågan

def main(): # det huvudsakliga programmet
    print("Welcome to the Math Quiz!")
    while True: # loop som kör programmet
        operation = ""
        while operation not in ["multiply","divide","quit"]:
            operation = input("Choose an operation (multiply, divide, both, or quit to exit): ") # användaren får välja vad som ska göras

        if operation == "quit": # om quit så avslutas programmet
            print("Goodbye!")
            break

        num_questions = int(input("How many questions would you like to answer? ")) # får välja hur många frågor
        score = 0

        for i in range(num_questions): # för antalet frågor
            question, answer = generate_question(operation) # genererar fråga och svar med funktionen generate_question
            user_answer = input(question) # frågar frågan som genererades 
            
            user_answer = int(user_answer)

            if user_answer == answer: # om svaret är rätt
                print("Correct!")
                score += 1
            else: # om inte rätt
                print(f"Wrong! The correct answer is {answer}.")

        print("You got",  score, "out of", num_questions, "questions correct.") # skriver ut antal poäng
        if num_questions > 0: # om minst en fråga
            percentage = (score / num_questions) * 100
            print(f"Your score: {percentage} %") # skriver ut hur många procent rätt

main() # kör programmet
