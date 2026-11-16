import random
import os
import time

# функция who_goes_first(), которая определяет, кто будет делать первый ход – пользователь или компьютер.
# Функция должна задать соответствующий вопрос пользователю и предложить ввести варианты:
# например, ввести 0, если первым будет ходить пользователь, или 1 – если компьютер. После этого функция должна вернуть игрока,
# который будет ходить первым.

def who_goes_first():
    answer_first_step = 2
    while answer_first_step != '0' and answer_first_step != '1':
        print('Введите 0, если первым будет ходить пользователь, или 1 - если компьютер.')
        answer_first_step = input()
    else:
        return int(answer_first_step)

# функция, которая будет отображать игровое поле в следующем виде:

# ❌⬜⬜
# ❌⭕⬜
# ⬜⬜⭕


def show_field(field):
    print()
    emoji_values = {1: '⬜', 2: '❌', 3: '⭕'}
    for row in field:
        print(''.join(emoji_values[cell] for cell in row))
    print()

# функция ask_for_game() которая печатает случайное приветствие из нескольких вариантов. 
# если пользователь впервые играет, то выводится одно из следующих сообщений:

# 1. Здравствуйте! Не желаете ли сыграть?
# 2. Доброго времени суток! Хотите поиграть?
# 3. Привет! Как насчет игры?

# если пользователь играет повторно, функция задает пользователю один из следующих вопросов:

# 1. Сыграем еще разок?
# 2. Хотите еще сыграть?
# 3. Желаете еще раз?

# пользователь должен ввести ответ да или нет. если пользователь отвечает да, начинаем игру, если нет – программа завершает работу.
# если пользователь введет что-то другое, функция должна вывести сообщение о некорректности ввода и повторить прием ввода.

def ask_for_game(game_number):
    message_dict = {1: 'Здравствуйте! Не желаете ли сыграть?',
                    2: 'Доброго времени суток! Хотите поиграть?',
                    3: 'Привет! Как насчет игры?'
    }
    question_dict = {1: 'Сыграем еще разок?',
                     2: 'Хотите еще сыграть?',
                     3: 'Желаете еще раз?'
    }
    answer_message = ''
    answer_question = ''
    if game_number == 0:
        num_random_message = random.randint(1,3)
        print(message_dict[num_random_message])
        answer_message = ''
        while answer_message.lower() != 'да' and answer_message.lower() != 'нет':
            answer_message = input()
            if answer_message.lower() != 'да' and answer_message.lower() != 'нет':
                print('Введите корректный ответ: да или нет')
    else:
        num_random_question = random.randint(1,3)
        print(question_dict[num_random_question])
        answer_question = ''
        while answer_question.lower() != 'да' and answer_question.lower() != 'нет':
            answer_question = input()
            if answer_question.lower() != 'да' and answer_question.lower() != 'нет':
                print('Введите корректный ответ: да или нет')
    return answer_message.lower() == 'да' or answer_question.lower() == 'да'

# функция get_user_move(), которая через стандартный поток ввода принимает от пользователя номер ряда и столбца.
# если пользователь вводит некорректные данные или клетка занята, функция должна вывести соответствующее сообщение
# и повторить ввод. функция должна продолжать работу до тех пор, пока данные не будут валидными. После этого функция возвращает
# ход пользователя в виде кортежа (<номер ряда>, <номер столбца>).

def get_user_move(field):
    print('Ваш ход')
    print()
    print('Введите номер ряда:')
    row_number = input()
    print('Введите номер столбца:')
    column_number = input()
    while (row_number not in ['1', '2', '3'] or column_number not in ['1', '2', '3']) or field[int(row_number) - 1][int(column_number) - 1] != 1:
        print()
        print('Неккоректные данные.')
        print('Номер ряда может быть в диапазоне от 1 до 3.')
        print('Номер столбца может быть в диапазоне от 1 до 3.')
        print('Клетка должна быть не занята')
        print('Повторите ввод.')
        print()
        print('Введите номер ряда:')
        row_number = input()
        print('Введите номер столбца:')
        column_number = input()
    else:
        user_move = (int(row_number), int(column_number))
        return user_move

# функция get_computer_move(), которая возвращает ход компьютера в виде кортежа (<номер ряда>, <номер столбца>). 
# для простоты реализации пусть компьютер делает ход в случайную из свободных клеток игрового поля.

def get_computer_move(field):
    print()
    print('Ход компьютера')
    row_comp_move = random.randint(1, 3)
    column_comp_move = random.randint(1, 3)
    while field[row_comp_move - 1][column_comp_move - 1] != 1:
        row_comp_move = random.randint(1, 3)
        column_comp_move = random.randint(1, 3)

    computer_move = (row_comp_move, column_comp_move)
    return computer_move

# функция check_result(), которая проверяет текущее состояние игрового поля на наличие исхода – 
# победы крестиков, ноликов или ничьей. Функция должна возвращать результат игры.

def check_result(field):
    if ((field[0][0], field[0][1], field[0][2]) == (2, 2, 2) or 
        (field[1][0], field[1][1], field[1][2]) == (2, 2, 2) or
        (field[2][0], field[2][1], field[2][2]) == (2, 2, 2) or
        (field[0][0], field[1][0], field[2][0]) == (2, 2, 2) or
        (field[0][1], field[1][1], field[2][1]) == (2, 2, 2) or
        (field[0][2], field[1][2], field[2][2]) == (2, 2, 2) or
        (field[0][0], field[1][1], field[2][2]) == (2, 2, 2) or
        (field[0][2], field[1][1], field[2][0]) == (2, 2, 2)):
        return 'Победа крестиков'
    elif ((field[0][0], field[0][1], field[0][2]) == (3, 3, 3) or 
        (field[1][0], field[1][1], field[1][2]) == (3, 3, 3) or
        (field[2][0], field[2][1], field[2][2]) == (3, 3, 3) or
        (field[0][0], field[1][0], field[2][0]) == (3, 3, 3) or
        (field[0][1], field[1][1], field[2][1]) == (3, 3, 3) or
        (field[0][2], field[1][2], field[2][2]) == (3, 3, 3) or
        (field[0][0], field[1][1], field[2][2]) == (3, 3, 3) or
        (field[0][2], field[1][1], field[2][0]) == (3, 3, 3)):
        return 'Победа ноликов'
    elif True not in [True for i in range(3) for j in range(3) if field[i][j] == 1]:
        return 'Ничья' 
    else:
        return 'Игра продолжается'

    
    
# функция play_game(), которая отвечает за одну партию - от пустого поля до победы или ничьей


def play_game(first_player):
    field = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    current_player = first_player
    for i in range(1, 10):
        if current_player == 0:
            time.sleep(1)
            step = get_user_move(field)
            row, column = step
            field[row - 1][column - 1] = 2
            current_player = 1
            show_field(field)
        elif current_player == 1:
            time.sleep(1)
            step = get_computer_move(field)
            row, column = step
            field[row - 1][column - 1] = 3
            current_player = 0
            show_field(field)
        current_result = check_result(field)
        if current_result != 'Игра продолжается':
            print(current_result)
            return   


# главная функция 

def main():
    game_number = 0

    while ask_for_game(game_number):
        first_player = who_goes_first()
        play_game(first_player)
        game_number += 1

    print('Игра окончена')

main()