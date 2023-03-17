"""Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5"""

from random import randint

N= int(input("Введите число N: "))
X = int(input("Введите число X: "))
list_A = []
difference_X = 100
search_number = -1

for i in range(N):
    list_A.append(randint(1,N))
    if abs(list_A[i]- X)< difference_X:
        difference_X = abs(list_A[i]- X)
        search_number = list_A[i]
print(list_A)
print("->",search_number)