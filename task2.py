"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика)
"""
from memory_profiler import profile
from recordclass import recordclass, make_dataclass
from collections import namedtuple

L_1 = recordclass('L_1', ('x', 'y', 'z'))
L_2 = make_dataclass('L_2', ('x', 'y', 'z'))
L_3 = namedtuple('L_3', ('x', 'y', 'z'))

a = L_3(1, 2, 3)


@profile
def f(name_of_class, n):
    res = [name_of_class(1, 2, 3) for _ in range(n)]
    return res


f(L_1, 20 ** 2)
f(L_2, 20 ** 2)
f(L_3, 20 ** 2)

"""Использование recordclass и make_dataclass позволяет уменьшить используемую память.
recordclass использует меньше памяти и поддерживает изменение значения объектов таким образом можно
связать объект-значение с другим объектом-значением. Если эта функциональность не нужна, то можно использовать
make_dataclass, который использует еще меньше памяти."""
