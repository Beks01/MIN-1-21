import dbOfProducts
import functions
import erzhan_first
import func_erzhan


class Director:
    def return_to_menu(self):
        return input()

    def menu(self):
        choice = int(input('''1. Показать список всех товаров (Показывает список товаров, который есть в магазине)
                            2. Показать количество товаров (Показывает количество товаров по категории)
                            3. Показать товар с самым максимальным количеством
                            4. Показать товар с самым минимальным количеством
                            5. Показать отчет по закупкам товаров 
                            6. Выход (Выходит в прошлое меню)
'''))
        if choice == 1:
            Director.listOfPr(self)
        elif choice == 2:
            Director.numsOfPr(self)
        elif choice == 3:
            Director.maxOfPr(self)
        elif choice == 4:
            Director.minOfPr(self)
        elif choice == 5:
            func_erzhan.show_executed_order()

    def listOfPr(self):
        for i in dbOfProducts.productsDb.keys():  # 1)List of all products in the store (Director).
            for j in dbOfProducts.productsDb[i].keys():
                print('List of all products:', i, j)

    def numsOfPr(self):
        for a in dbOfProducts.productsDb.keys():
            for b in dbOfProducts.productsDb[a].keys():  # 2)list of all products and their numbers (Director).
                print('Number of products = ', a, b, dbOfProducts.productsDb[a][b][2])

    def maxOfPr(self):
        listOfNumsOfPr = []
        for x in dbOfProducts.productsDb.keys():
            for y in dbOfProducts.productsDb[x].keys():  # 3)max number of products and their numbers (Director).
                listOfNumsOfPr.append(dbOfProducts.productsDb[x][y][2])
        maxNumber = (max(listOfNumsOfPr))  # We found the max number of product.
        print('Maximum number of products is equal to', maxNumber)

    def minOfPr(self):
        listOfNumsOfPr = []
        for x in dbOfProducts.productsDb.keys():
            for y in dbOfProducts.productsDb[x].keys():  # 4)min number of products and their numbers (Director).
                listOfNumsOfPr.append(dbOfProducts.productsDb[x][y][2])
        minNumber = (min(listOfNumsOfPr))  # We found the min number of product.
        print('Minimum  number of products is equal to', minNumber)
