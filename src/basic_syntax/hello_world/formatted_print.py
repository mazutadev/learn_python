#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Примеры форматированного вывода в Python
"""

name = "Python"
version = 3.12

# Старый стиль форматирования (%)
print("Hello, %s!" % name)
print("Hello, %s %s!" % (name, version))

# Метод format()
print("Hello, {}!".format(name))
print("Hello, {} {}!".format(name, version))
print("Hello, {name} {version}!".format(name=name, version=version))

# F-строки (Python 3.6+)
print(f"Hello, {name}!")
print(f"Hello, {name} {version}!")

# Форматирование чисел
pi = 3.14159
print(f"Число Пи: {pi:.2f}")

# Выравнивание текста
text = "Hello"
print(f"{text:>10}")  # Выравнивание по правому краю
print(f"{text:<10}")  # Выравнивание по левому краю
print(f"{text:^10}")  # Выравнивание по центру
