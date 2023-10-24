# Här är ett program som innehåller en del fel
# Vi ska åtgärda dem på följande sätt:
# 1. Se till att programmet går att köra
# 2. Testa funktionerna som ska finnas
# 3. Testa vad som händer om man skriver in konstiga saker och åtgärda det
# 4. Fundera om det är något mer vi kan göra för att öka användarvänligheten

def generate_question(operation): 
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    if operation == "multiply":
        question = "What is " + num1 + " * " + num2 + "? "
        answer = num1 * num2
    else:
        question = "What is " + num1*num2 + "/" + num1 + "? "
        answer = num2
    return question, answer

def main():
    print("Welcome to the Math Quiz!")
    while True:
        operation = input("Choose an operation (multiply, divide, both, or quit to exit): ")

        if operation == "quit":
            print("Goodbye!")
            break

        num_questions = int(input("How many questions would you like to answer? "))
        score = 0

        for _ in range(num_questions):
            question, answer = generate_question(operation)
            user_answer = input(question)
            
            user_answer = int(user_answer)

            if user_answer == answer:
                print("Correct!")
                score += 1
            else:
                print("Wrong! The correct answer is " + answer + ".")

        print("You got " + score + "out of " + num_questions + " questions correct.")
        if num_questions > 0:
            percentage = (score / num_questions) * 100
            print("Your score: " + percentage + "%")

main()
