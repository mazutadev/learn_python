#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Примеры базового ввода и вывода в Python
"""

# Простой вывод
print("Hello, World!")

# Вывод нескольких аргументов
print("Hello", "World", "!")

# Вывод с использованием разделителя
print("Hello", "World", "!", sep="-")

# Вывод с завершающим символом
print("Hello", end=" ")
print("World", end="!\n")

# Простой ввод
name = input("Введите ваше имя: ")
print(f"Привет, {name}!")

# Ввод числа
age = int(input("Введите ваш возраст: "))
print(f"Вам {age} лет")

# Ввод нескольких значений
values = input("Введите числа через пробел: ").split()
numbers = [int(x) for x in values]
print(f"Вы ввели числа: {numbers}")
