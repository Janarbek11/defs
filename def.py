# Создайте функцию которая которая берёт лист делит его пополам и обе стороны разворачивает в противоположную сторону. Пример:
# Оригинальный Лист:
# list_1 = ['name', 'age', '1', '19']
# Изменённый Лист:
# list_1 = ['age', 'name', '19', '1']

# list_1 = ['name', 'age', '1', '19']

# def rev():
#     newList = []
#     first = list_1[:2]
#     second = list_1[2:]
#     second.reverse()
#     first.reverse()
#     newList.extend(first)
#     newList.extend(second)
#     print(newList)
#
# rev()

# Создайте функцию которая генерирует 10 чисел Фибоначчи:
# 1,1,2,3,5,8,13,21,34,...          f = f1-n +f2-n
#
# def fibo():
#     f = 1
#     count = 0
#     while count != 10:
#         f = (f - 1) + (f - 2)
#         print(f)
#         count += 1
#
# fibo()

#  Спросите у пользователя имя файла.
#  Создайте функцию которая создаёт файл с именем которое передал пользователь.
#  Присвойте ИМЯ функции к переменной и вызывайте функцию через переменную.

# user = input("Введите название файла: ")
#
# def user_file():
#
#   f = open(user,"w")
#
# my_function = user_file
# my_function()

#  Создайте функцию сложения, затем функцию вычитания двух чисел...
# Создайте 3-ю функцию которая вызывает первые 2 внутри себя.
# a = int(input('Enter a = '))
# b = int(input('Enter b = '))
#
# def plus(a, b):
#   # a = int(input())
#   # b = int(input())
#   res = a + b
#   print(res)
#
# def subtract(a, b):
#   # a = int(input())
#   # b = int(input())
#   res = a - b
#   print(res)
#
# def plussub(a, b):
#   plus(a, b)
#   subtract(a, b)
#
# plussub(a, b)
# plus(a, b)
# subtract(a, b)

# Представьте Вы работаете в Мобильной Компании и вас попросили создать генератор номеров.
# Создайте функцию gen_number() которая генерирует телефонный номер с кодом 0444______.
# Номера которые можете генерировать могут содержать в себе только числа 145790. Пример: 0444150971 0444111777 0444457901
from random import choice
def gen_number():
  intlist = [1, 4, 5, 7, 9, 0]
  num = choice(intlist)
  print(f'0444{num}{num}{num}{num}{num}{num}')  # я здесь еще исправлю (что-то не так :| )

gen_number()



