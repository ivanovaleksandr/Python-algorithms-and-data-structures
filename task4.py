"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
from hashlib import sha256


def memorize(func):
    def g(url, memory={}):
        r = memory.get(sha256(url.encode('utf-8')).hexdigest())
        if r is None:
            r = func(url)
            print(f'url {url} был добавлен в кеш')
            memory[sha256(url.encode('utf-8')).hexdigest()] = r
        return r

    return g


@memorize
def check_url(url):
    return url


check_url('rambler.ru')
check_url('mail.ru')
check_url('mail.ru')
check_url('yandex.ru')
check_url('geekbrains.ru')
check_url('geekbrains.ru')
check_url('yandex.ru')
check_url('rambler.ru')
