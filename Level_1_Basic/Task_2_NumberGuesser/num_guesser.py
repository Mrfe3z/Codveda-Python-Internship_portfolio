import random
random_guess = random.randint(1, 100)

attempts = 5
while attempts > 0:
    print('guess a number between 1 and a 100')
    answer = input('>> ')
    try:
        answer = int(answer)
    except ValueError as e:
        print('invalid input, enter a number within th range of 1 and 100')
        continue

    if answer == random_guess and attempts == 5:
        print(f'wow!, got the answer in one try. answer= {random_guess}')
        break

    if answer == random_guess:
        print('correct answer')
        break

    elif answer < random_guess:
        print('please guess higher')
        attempts -= 1
        print(f' attempts left: {attempts}')
        continue

    elif answer > random_guess:
        print('guessed too high, guess lower')
        attempts -= 1
        print(f' attempts left: {attempts}')
        continue

if attempts == 0:
    print(f'no more tries, correct answer was: {random_guess}')
