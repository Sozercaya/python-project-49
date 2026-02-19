import math
from random import randint

DESCRIPTION = "Find the greatest common divisor of given numbers."


def generate_round():
    num1 = randint(1, 100)
    num2 = randint(1, 100)

    question = f'{num1} {num2}'
    correct_answer = str(math.gcd(num1, num2))

    return question, correct_answer

