""" Задача 12
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных 
числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя 
делает две подсказки. Он называет сумму этих чисел S и их 
произведение P. Помогите Кате отгадать задуманные Петей числа.

Пример:
4 4 -> 2 2
5 6 -> 2 3 """

S = int(input('Summ of the given numers: '))
P = int(input('Multiplication of the given numbers: '))

# for i in range(1, P//2 + 1, 1):
#     if i + (P / i) == S:
#         print(f'Numbers given by Peter "{i}" and "{P // i}"')
#         break

divider = 0
while divider < P//2 + 1:
    divider += 1
    if divider + (P / divider) == S:
        print(f'Numbers given by Peter are "{divider}" and "{P // divider}"')
        break
else:
    print(f'There are no such numbers to make {S} and {P}')

