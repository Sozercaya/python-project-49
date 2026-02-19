from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    num1 = randint(1, 50)
    num2 = randint(1, 50)
    operations = ['+', '-', '*']
    operation = choice(operations)

    question = f'{num1} {operation} {num2}'

    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    elif operation == '*':
        correct_answer = num1 * num2
    
    return question, str(correct_answer)