#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Примеры арифметических операторов в Python
"""

# Базовые арифметические операции
a = 10
b = 3

# Сложение
print(f"{a} + {b} = {a + b}")  # 13

# Вычитание
print(f"{a} - {b} = {a - b}")  # 7

# Умножение
print(f"{a} * {b} = {a * b}")  # 30

# Деление (обычное)
print(f"{a} / {b} = {a / b}")  # 3.333...

# Целочисленное деление
print(f"{a} // {b} = {a // b}")  # 3

# Остаток от деления
print(f"{a} % {b} = {a % b}")  # 1

# Возведение в степень
print(f"{a} ** {b} = {a ** b}")  # 1000

# Унарный минус
print(f"-{a} = {-a}")  # -10

# Приоритет операций
result = 2 + 3 * 4  # Сначала умножение, потом сложение
print(f"2 + 3 * 4 = {result}")  # 14

# Скобки изменяют приоритет
result = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result}")  # 20
