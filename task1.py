"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
from random import randint
from timeit import timeit

MAX_SIZE = 100
NUMBER_EXECUTIONS = 10_000


def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        flag = True
        for n in range(i):
            if array[n] > array[n + 1]:
                array[n], array[n + 1] = array[n + 1], array[n]
                flag = False

        if flag == True:
            break
    return array


def bubble_sort_no_smart(array):
    for i in range(len(array) - 1, 0, -1):
        for n in range(i):
            if array[n] > array[n + 1]:
                array[n], array[n + 1] = array[n + 1], array[n]

    return array


numbers = [randint(-100, 100) for _ in range(MAX_SIZE)]
print(numbers)
print(bubble_sort(numbers))

time1 = timeit(f'bubble_sort({numbers})',
               setup='from __main__ import bubble_sort',
               number=NUMBER_EXECUTIONS)
time2 = timeit(f'bubble_sort_no_smart({numbers})',
               setup='from __main__ import bubble_sort_no_smart',
               number=NUMBER_EXECUTIONS)
print(time1)
print(time2)
