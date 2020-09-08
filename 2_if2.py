"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def main():
    a = 'sdfgg'
    b = 'фыаф'

    def string(str1, str2):

        if (type(str1) or type(str2)) is not str:
            print('0')
        elif str1 == str2:
            print('1')
        elif str2 == 'learn':
            print('3')
        elif str1 > str2:
            print('2')
        else:
            print('What?!')

    string(a, b)


if __name__ == "__main__":
    main()
