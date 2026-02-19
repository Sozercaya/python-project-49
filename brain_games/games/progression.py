from random import randint

DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def generate_progression(start, step, length):
    return [start + i * step for i in range(length)]


def generate_round():
    # Генерируем случайные параметры прогрессии
    start = randint(1, 20)
    step = randint(2, 5)
    length = randint(5, 10)

    progression = generate_progression(start, step, length)

    # Выбираем случайный индекс для скрытого элемента
    hidden_index = randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    question_parts = []
    for i, num in enumerate(progression):
        if i == hidden_index:
            question_parts.append('..')
        else:
            question_parts.append(str(num))
    
    question = ' '.join(question_parts)
    
    return question, correct_answer