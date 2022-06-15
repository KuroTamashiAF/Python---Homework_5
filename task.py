# 1. Напишите программу, удаляющую из текста все слова содержащие "абв",
# которое регистронезависимо. Используйте знания с последней лекции. Выполните ее в виде функции.
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»
'''
def case_reduction(row):
    row = row.lower()
    return row


def del_element(row):
    list1 = list(filter(lambda x: 'абв' not in x, row.split()))
    return list1


row = 'абггдеж рабав копыто фабв Абкн абрыволк аБволк'
row = case_reduction(row)
total_list = del_element(row)
print(total_list)
'''

# 2. Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её,
# причем чтобы сыграть в нее можно было в одиночку.
'''
board = [i for i in range(1, 10)]
wins_combination = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
                    (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_board():
    print('-'*13)
    for i in range(3):
        print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
    print('-'*13)


def input_from_user(player_input):
    while True:
        value = input("В какую ячейку поставить: " + player_input + " ?")
        if not (value in '123456789'):
            print('Неверный ввод. Повторите')
            continue
        value = int(value)
        if str(board[value-1]) in 'XO':
            print('Эта клетка уже занята')
            continue
        board[value-1] = player_input
        break


def wins_check():
    for each in wins_combination:
        if(board[each[0]-1]) == (board[each[1]-1]) == (board[each[2]-1]):
            return board[each[0]-1]
    else:
        return False


def main():

    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            input_from_user('X')
        else:
            input_from_user('O')
        if counter > 3:
            winner = wins_check()
            if winner:
                draw_board()
                print(winner, 'Победил')
                break
        counter += 1
        if counter > 8:
            draw_board()
            print('Ничья')
            break


main()
'''
# 3. Вот вам текст:«Ну, вышел я, короче, из подъезда. В общем, короче говоря,
# шел я, кажется, в магазин. Ну,эээ, в общем, было лето, кажется. Как бы тепло.
# Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма.
# Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда. Ясен пень, в магазин.
# В общем, лето на дворе, жарко, солнечно, птицы, короче, летают.
# Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем.
# Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно.
# В общем, в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я.
# Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил».

# Отфильтруйте его, чтобы этот текст можно было нормально прочесть.
# Предусмотрите вариант, что мусорные слова могли быть написаны без использования запятых.
