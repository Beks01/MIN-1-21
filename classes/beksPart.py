from self import self

import director
import functions


def return_to_menu():
    return input('Enter для продолжения...'), menu(self)


def menu(self):
    print("Добро пожаловать Директор!")
    choice = int(input('''1. Показать список всех товаров (Показывает список товаров, который есть в магазине)
                            2. Показать количество товаров (Показывает количество товаров по категории)
                            3. Показать товар с самым максимальным количеством
                            4. Показать товар с самым минимальным количеством
                            5. Показать отчет по закупкам товаров 
                            6. Выход ( Выходит из программы)
'''))
    if choice == 1:
        director.Director.listOfPr(self)  # 1 список всех товаров
        return_to_menu()
    elif choice == 2:
        director.Director.numsOfPr(self)  # 2 количество товаров
        return_to_menu()
    elif choice == 3:
        director.Director.maxOfPr(self)  # 3 товар c макс. количеством
        return_to_menu()
    elif choice == 4:
        director.Director.minOfPr(self)  # 4 товар с мин. количеством
        return_to_menu()
    elif choice == 5:
        functions.show_maded_order()    # 5 отчет по закупкам товаров
        return_to_menu()
    elif choice == 6:                   # 6 Выход из программы
        print('Вы вышли из программы !')


