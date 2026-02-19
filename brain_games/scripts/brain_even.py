import prompt
from random import randint


def main():
    name = welcome_user()
    print('Welcome to the Brain Games!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answer = 0
    while correct_answer <= 3:
        number = randint(1, 20)
        print('Question:' + str(number))
        answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            if answer == 'yes':
                print('Correct!')
                correct_answer += 1
            else:
                print(answer + " is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, " + name + "!")
                break
        elif number % 2 != 0:
            if answer == 'no':
                print('Correct!')
                correct_answer += 1
            else:
                print(answer + " is wrong answer ;(. Correct answer was 'no'.\nLet's try again, " + name + "!")
                break
        if correct_answer == 3:
            print('Congratulations, ' + name + '!')
            break

        




def welcome_user():
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + '!')
    return name

if __name__ == "__main__":
    main()



