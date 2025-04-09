#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Примеры форматирования строк в Python
"""

name = "Python"
version = 3.12
pi = 3.14159

# Старый стиль форматирования (%)
print("Hello, %s!" % name)
print("Hello, %s %s!" % (name, version))
print("Число Пи: %.2f" % pi)

# Метод format()
print("Hello, {}!".format(name))
print("Hello, {} {}!".format(name, version))
print("Hello, {name} {version}!".format(name=name, version=version))
print("Число Пи: {:.2f}".format(pi))

# F-строки (Python 3.6+)
print(f"Hello, {name}!")
print(f"Hello, {name} {version}!")
print(f"Число Пи: {pi:.2f}")

# Выравнивание текста
text = "Hello"
print(f"{text:>10}")  # Выравнивание по правому краю
print(f"{text:<10}")  # Выравнивание по левому краю
print(f"{text:^10}")  # Выравнивание по центру

# Форматирование чисел
number = 1234.5678
print(f"{number:,.2f}")  # Разделители тысяч и 2 знака после запятой
print(f"{number:.2e}")  # Экспоненциальная запись
print(f"{number:+.2f}")  # Знак числа
