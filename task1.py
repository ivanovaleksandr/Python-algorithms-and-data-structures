"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

import numpy as np
from memory_profiler import profile


@profile()
def f1(n):
    res = list(range(n))
    return res


@profile()
def f2(n):
    res = np.arange(0, n)
    return res


f1(10 ** 5)
f2(10 ** 5)


# Функция, использующая numpy использует гораздо меньше памяти, чем функция, возвращающяя список.

# **************************************************************************************************************

class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate(self):
        return self.length * self.width / 8


class RoadSlots:
    __slots__ = ('length', 'width')

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate(self):
        return self.length * self.width / 8


@profile
def create_road(n):
    return tuple(Road(1, 1) for _ in range(n))


@profile
def create_road_slots(n):
    return tuple(RoadSlots(1, 1) for _ in range(n))


create_road(10 ** 4 * 2)
create_road_slots(10 ** 4 * 2)


# Использование __slots__ может уменьшить используемую память в несколько раз:

# **************************************************************************************************************"""

@profile
def find_pair1(arr):
    res = None
    for pair in arr:
        s = sum(pair)
        if res is None or s > res:
            res = s
    return res


@profile
def find_pair2(arr):
    pair_sums = [sum(pair) for pair in arr]
    return max(pair_sums)


test_arr = np.random.randint(0, 10 ** 4, (10 ** 5, 2), dtype=np.int16)
find_pair1(test_arr)
find_pair2(test_arr)

# Второй способ выглядит лаконичнее, однако использует много памяти, в первом способе память практически не выделяется.
