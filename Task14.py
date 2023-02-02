""" Задача 14
Требуется вывести все целые степени двойки (т.е. числа вида 2**k), 
не превосходящие числа N.

Пример:
10 -> 1 2 4 8 """

cut_off_number = int(input('Enter a number: '))
list_of_squares = []
exponential = 0

while 2**exponential < cut_off_number:
    list_of_squares.append(2**exponential)
    exponential +=1

print(*list_of_squares)
