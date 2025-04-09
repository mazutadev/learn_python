#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Примеры автоматического форматирования кода
"""


# Пример кода до форматирования
def unformatted_code():
    x = 10
    y = 20
    if x > y:
        print("x больше y")
    elif x < y:
        print("x меньше y")
    else:
        print("x равно y")


# Пример кода после форматирования (как должен выглядеть)
def formatted_code():
    x = 10
    y = 20
    if x > y:
        print("x больше y")
    elif x < y:
        print("x меньше y")
    else:
        print("x равно y")


# Пример длинной строки до форматирования
def long_line_before():
    result = "Это очень длинная строка, которая должна быть разделена на несколько строк для соблюдения PEP 8"


# Пример длинной строки после форматирования
def long_line_after():
    result = (
        "Это очень длинная строка, которая "
        "должна быть разделена на несколько "
        "строк для соблюдения PEP 8"
    )


# Пример многострочной структуры до форматирования
def multiline_before():
    my_list = ["первый элемент", "второй элемент", "третий элемент"]
    my_dict = {"ключ1": "значение1", "ключ2": "значение2", "ключ3": "значение3"}


# Пример многострочной структуры после форматирования
def multiline_after():
    my_list = [
        "первый элемент",
        "второй элемент",
        "третий элемент",
    ]

    my_dict = {
        "ключ1": "значение1",
        "ключ2": "значение2",
        "ключ3": "значение3",
    }
