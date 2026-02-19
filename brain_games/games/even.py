import prompt
from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    #Проверяет, является ли число чётным
    return number % 2 == 0


def generate_round():
    number = randint(1, 100)
    question = str(number)
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer

