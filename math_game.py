import random as rand
from threading import Timer
from sys import exit

def rules():
    return '''
1. You will be asked 10 math questions.
2. Each question will have two random numbers between 0 and 100.
3. You have 30 seconds to answer all 10 questions.
4. Try to answer as many questions correctly as you can within the time limit.
5. Your final score will be shown at the end of the game.
'''

def find_answer(first_int, second_int, operator):
    match operator:
        case '+':
            return first_int + second_int
        case '-':
            return first_int - second_int
        case '/':
            return first_int / second_int
        case 'x':
            return first_int * second_int
        case '^':
            return first_int ** second_int

def play():
    '''
    Starts the game
    '''
    print(rules())
    input('Type anything to start now!! ')
    
    score = [0]  # use a list so timer can access updated score
    number_of_questions = 10
    operators = ['+','-','/','x','^']

    # Timer function
    def time_up():
        print(f"\nTime's up! Your score is: {score[0]}/10")
        exit()

    # Start the 30-second timer
    t = Timer(57, time_up)
    t.start()

    while number_of_questions:
        first_int = rand.randint(0,50)
        second_int = rand.randint(1,5)  # avoid division by zero
        operator = rand.choice(operators)

        # Skip division if it won't be whole
        if operator == '/' and first_int % second_int != 0:
            continue

        number_of_questions -= 1
        result = find_answer(first_int, second_int, operator)

        try:
            answer = float(input(f"{first_int} {operator} {second_int}: "))
        except ValueError:
            print("Invalid input, counted as wrong!")
            continue

        if result == answer:
            score[0] += 1

    # Cancel timer if player finishes early
    t.cancel()
    print(f"\nYou finished early! Your score is: {score[0]}/10")

if __name__ == "__play__":
    play()

