import gen_one
import gen_two
import chast_test
import serial_test
import poker_test
import corr_test
import interval_test
import model_exp
import model_par
import model_weib
import zelin
import broks
import model_gamma
def opros():
    print(':^_^:*_*' * 10)
    menu_return = input('Выберите вариант:\n (1) Вернуться в меню\n (2) Завершить программу\n Введите вариант(номер): ')
    if menu_return == '1':
        main_menu()
    elif menu_return == '2':
        print("Пока!" * 15)
    else:
        print('Вы ввели не корректный запрос!')
        opros()

def main_menu(x = None):
    print('Добро пожаловать! Данный софт предназначен для генерации псевдослучайных чисел.')
    if (x == None):
        z = input('Выберите один из вариантов представленных ниже: \n (1) Запустить генератор псевдослучайных чисел.\n (2) Вызвать список эмпирических тестов\n (3) Моделирование случайных величин с заданным законом распределения\n (4) Моделирование псевдослуч величины, распределенной по нормальному закону \n (5) Выйти из программы\n Введите номер(число): ')
    else:
        if (x == '1') or (x == '2') or (x == '3')  or (x=='4') or (x=='5'):
            z = x
        else:
            z = input('Выберите один из вариантов представленных ниже: \n (1) Запустить генератор псевдослучайных чисел.\n (2) Вызвать список эмпирических тестов\n (3) Моделирование случайных величин с заданным законом распределения\n (4) Выйти из программы\n Введите номер(число): ')
    print(':^_^:*_*'*10)
    if z == '1':
        z_1 = input("Выберите генератор:\n (1) Генератор на методе вычетов\n (2) Генератор на М-последовательности\n (3) Выйти в меню \n")
        print(':^_^:*_*'*10)
        try:
            if z_1 == '1':
                try:
                    gen_one.run_get_one()
                    opros()
                except:
                    print('Error 1.0: Не возможно импортировать: gen_one.py')
                    opros()
                opros()
            elif z_1 == '2':
                try:
                    gen_two.run_gen_two()
                    opros()
                except:
                    print('Error 1.1: Не возможно импортировать: gen_two.py.')
                    opros()
                opros()
            elif z_1 == '3':
                main_menu()
            else:
                print('Введен не корректный запрос.')
                opros()
        except:
            print("Error 1.3: Вы ввели некорректный запрос.")
            opros()
    elif z == '2':
        test_num = input('Выберите эмпирические тесты:\n (1) Частотный тест\n (2) Сериальный тест\n (3) Покер тест\n (4) Корреляционный тест\n (5) Интервальный тест\n (6) Вернуться в меню\n Введи номер(число): ')
        if test_num == '1':
            print(':^_^:*_*' * 10)
            chast_test.run_chast()
            opros()
        elif test_num == '2':
            print(':^_^:*_*' * 10)
            serial_test.run_serial()
            opros()
        elif test_num == '3':
            print(':^_^:*_*' * 10)
            poker_test.run_poker()
            opros()
        elif test_num == '4':
            print(':^_^:*_*' * 10)
            corr_test.run_corr()
            opros()
        elif test_num == '5':
            print(':^_^:*_*' * 10)
            interval_test.run_interval()
            opros()
        elif test_num == '6': main_menu()
        else:
            print('Введен не корректный запрос.')
            opros()
    elif z == '3':
        num_mod = input('Выберите распределение:\n (1) Экспоненциальное распределение\n (2) Распределение Парето\n (3) Распределение Вейбулла \n (4) Гамма-распределение \n Введи номер(число): ')
        if num_mod == '1':
            print(':^_^:*_*' * 10)
            model_exp.run_model_exp()
            opros()
        elif num_mod == '2':
            print(':^_^:*_*' * 10)
            model_par.run_model_par()
            opros()
        elif num_mod == '3':
            print(':^_^:*_*' * 10)
            model_weib.run_model_weib()
            opros()
        elif num_mod == '4':
            print(':^_^:*_*' * 10)
            model_gamma.run_model_gamma()
            opros()
    elif z == '4':
        num_norm = input('Выберите метод моделирования: \n (1) По методу Зелинского \n (2) По методу Брокса - Малера \n (3) Выйти в основное меню  \n Введите номер: ')
        if num_norm == '1' :
            zelin.model_zelin()
            opros()
        elif num_norm == '2':
            broks.model_broks()
            opros()
        elif num_norm == '3':
            main_menu()

    elif z == '5': print ("Пока!"*15)
    else:
        print("Error 1.6: Вы ввели некорректный запрос.")
        opros()
main_menu()
