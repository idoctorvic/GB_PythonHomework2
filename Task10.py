""" На столе лежат n монеток. Некоторые из них лежат вверх решкой, а 
некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
вверх одной и той же стороной. Выведите минимальное количество монет, 
которые нужно перевернуть.

Пример:
5 -> 1 0 1 1 0
2 """

from random import randint

num_coins = int(input('How many coins in the list: '))       
coin_list = []

for i in range(num_coins):
    coin_list.append(randint(0,1))

print(coin_list)

# reshka = coin_list.count(0)
# orel = coin_list.count(1)
# print(f'reshka = {reshka}, orel = {orel}')

# if reshka < orel:
#     print(f'Mimimum coins to turn {reshka}')
# else:
#     print(f'Mimimum coins to turn {orel}')

count_reshka = 0
count_orel = 0

for i in coin_list:
    if i == 0:
        count_reshka += 1
    else:
        count_orel += 1

if count_reshka < count_orel:
    print(f'Mimimum coins to turn {count_reshka}')
else:
    print(f'Mimimum coins to turn {count_orel}')