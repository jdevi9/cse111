#global variables used
POSITIVE = 1
NEGATIVE = -1

def main():
    #information on survey
    print(f"This program is an implementation of the Rosenberg Self-Esteem Scale."
    "This program will show you ten statements that you could possibly \napply to yourself. "
    "Please rate how much you agree with each of the statements by responding with one "
    "of these four letters: ")
    print()
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")
    
    #Survey Questions
    points = 0
    points += getAnswer("1. I feel that I am a person of worth, at least on an equal plane with others.", POSITIVE)
    points += getAnswer("2. I feel that I have a number of good qualities.", POSITIVE)
    points += getAnswer("3. All in all, I am inclined to feel that I am a failure.", NEGATIVE)
    points += getAnswer("4. I am able to do things as well as most other people.", POSITIVE)
    points += getAnswer("5. I feel I do not have much to be proud of.", NEGATIVE)
    points += getAnswer("6. I take a positive attitude toward myself.", POSITIVE)
    points += getAnswer("7. On the whole, I am satisfied with myself.", POSITIVE)
    points += getAnswer("8. I wish I could have more respect for myself.", NEGATIVE)
    points += getAnswer("9. I certainly feel useless at times.", NEGATIVE)
    points += getAnswer("10. At times I think I am no good at all.", NEGATIVE)

    print(f"Your Score is {points}.")
    print("A score below 15 may indicate problematic low self-esteem.")

#formula prints the question, gets input and calculates the score to return for each
def getAnswer(question, positive_or_negative):
    
    #prints the question added in main()
    print(question)
    userInput = input("Enter D, d, a, or A: ")
    if userInput == "D":
        score = 0
    elif userInput == "d":
        score = 1
    elif userInput == "a":
        score = 2
    elif userInput == "A":
        score = 3

    if positive_or_negative == NEGATIVE:
        score = 3 - score
    return score

#execute program   
main()