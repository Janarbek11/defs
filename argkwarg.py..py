# def func(l, u = 15, *arg, **kwarg):
#     print(l, u, kwarg, arg)
#
# func(123, 6, 4, 5245, 45, 45532, key = ['values'], day = 'Hello')


# Создайте 4 функции: add(), substract(), multiply(), divide() которые будут принимать по 2 аргумента
# возвращать результат: сложения, вычитания, умножения и деления.

# a = int(input('Enter number: '))
# b = int(input('Enter number: '))
#
# def main():
#     add(a, b)
#     substract(a, b)
#     multiply(a, b)
#     divide(a, b)
#
# def add(a, b):
#     print(a + b)
#
# def substract(a, b):
#     print(a - b)
#
# def multiply(a, b):
#     print(a * b)
#
# def divide(a, d):
#     print(a, b)
#
# main()


# Написать Функцию которая принимает предложение как аргумент, считает количество букв и возвращает сколько символов он ввёл. НЕ ИСПОЛЬЗОВАТЬ функцию len()

# sentence = input('Sentence: ')
#
# def sen(sentence):
#     count = 0
#     for i in sentence:
#         count += 1
#     print("Символов в вашем предложении - ", count)

# sen(sentence)

# Напишите функцию которая принимает 2 Dictionary и добавляет втрорую Dictionary к первой.
# def twodict(**first):
#     my_dicts = []
#     my_dicts.append(first['key1'])
#     my_dicts.append(first['key2'])
#     return my_dicts
# a = {'a': 1, 'b': 2}
# b = {'c': 3, 'd': 4}
#
# print(twodict(key1= a, key2= b))


# Напишите функцию которая спрашивает у вас чтобы вы хотели заказать покушать и выпить. А затем записывает это всё в файл на рабочем столе menu.txt
dinner = input('Что вы хотите покушать?')
drink = input('Что вы хотите выпить?')

with open(r'/home/janarbek/Рабочий стол/menu.txt', 'w') as menu:
    menu.write(''+ dinner)
    menu.write(drink)




